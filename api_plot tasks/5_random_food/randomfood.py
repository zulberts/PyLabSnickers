import requests
from dataclasses import dataclass, field
from typing import List, Optional
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


@dataclass
class Meal:
    idMeal: str
    strMeal: str
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: Optional[str]
    strYoutube: Optional[str]
    ingredients: List[str] = field(default_factory=list)
    measures: List[str] = field(default_factory=list)


def get_random_meal() -> Optional[Meal]:
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    if response.status_code == 200:
        meal_data = response.json()["meals"][0]
        ingredients = [
            meal_data[f"strIngredient{i}"]
            for i in range(1, 21)
            if meal_data[f"strIngredient{i}"]
        ]
        measures = [
            meal_data[f"strMeasure{i}"]
            for i in range(1, 21)
            if meal_data[f"strMeasure{i}"]
        ]
        meal = Meal(
            idMeal=meal_data["idMeal"],
            strMeal=meal_data["strMeal"],
            strCategory=meal_data["strCategory"],
            strArea=meal_data["strArea"],
            strInstructions=meal_data["strInstructions"],
            strMealThumb=meal_data["strMealThumb"],
            strTags=meal_data.get("strTags"),
            strYoutube=meal_data.get("strYoutube"),
            ingredients=ingredients,
            measures=measures,
        )
        return meal
    else:
        print("Failed to retrieve meal details.")
        return None


def display_meal(meal: Meal):
    root = tk.Tk()
    root.title(meal.strMeal)
    response = requests.get(meal.strMealThumb)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((250, 250), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=img_tk)
    img_label.grid(row=0, column=0, columnspan=2)
    name_label = tk.Label(root, text=f"Name: {meal.strMeal}", font=("Helvetica", 16))
    name_label.grid(row=1, column=0, columnspan=2)
    category_label = tk.Label(root, text=f"Category: {meal.strCategory}")
    category_label.grid(row=2, column=0, sticky=tk.W)
    area_label = tk.Label(root, text=f"Area: {meal.strArea}")
    area_label.grid(row=2, column=1, sticky=tk.W)
    instructions_label = tk.Label(root, text="Instructions:")
    instructions_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
    instructions_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
    instructions_text.insert(tk.END, meal.strInstructions)
    instructions_text.config(state=tk.DISABLED)
    instructions_text.grid(row=4, column=0, columnspan=2)
    ingredients_label = tk.Label(root, text="Ingredients:")
    ingredients_label.grid(row=5, column=0, columnspan=2, sticky=tk.W)
    for i, (ingredient, measure) in enumerate(zip(meal.ingredients, meal.measures)):
        ingredient_label = tk.Label(root, text=f"{ingredient}: {measure}")
        ingredient_label.grid(row=6 + i, column=0, columnspan=2, sticky=tk.W)
    root.mainloop()


random_meal = get_random_meal()
if random_meal:
    display_meal(random_meal)
