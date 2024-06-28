visibility_dict = {
    "All": 1,
    "Friends": 2,
    "Friends of friends": 3
}


class User:
    """
    Class User. Contains attributes.

    :param name: Name of user.
    :param type: str

    :param friends_list: List of friends.
    :param type: list

    :param wall: List of posts posted by user.
    :param type: list
    """
    def __init__(self, name: str, friends_list: list, wall: list) -> None:
        if not name:
            raise ValueError("Name cannot be empty")
        else:
            self.__name = name
        if not friends_list:
            self.__friends_list = []
        else:
            self.__friends_list = friends_list
        if not wall:
            self.__wall = []
        else:
            self.__wall = wall
        self.__vissibility = 1

    @property
    def name(self):
        return self.__name

    @property
    def friends_list(self):
        return self.__friends_list

    @property
    def wall(self):
        return self.__wall

    def set_vissibility(self, who: str):
        self.__vissibility = visibility_dict[who]

    @property
    def vissibility(self):
        return self.__vissibility


class Post:
    """
    Class Post. containst attributes.

    :param text: Text of post.
    :param type: str

    :param autor: Author of the post.
    :param type: User
    """
    def __init__(self, text: str, author: User) -> None:
        if not text:
            self.__text = ""
        else:
            self.__text = text
        if not author:
            raise ValueError("Post must contain author")
        else:
            self.__author = author

    @property
    def text(self):
        return self.__text

    @property
    def author(self):
        return self.__author


class Wall():
    """
    Class Wall. Contain attributes.

    :param users: Contains list of all users.
    :param type: list[User]
    """

    def __init__(self, users: list[User]) -> None:
        self.__users = users

    @property
    def users(self):
        return self.__users

    def create_post(user: User):


    def set_vissibility(self, user: User):
        list_of_posts = []
        for user in self.users:
            for post in user.wall:
                list_of_posts.append(post)
        list_of_vissible = []
        for post in list_of_posts:
            if post.__author.vissibility == 1:
                list_of_vissible = list_of_posts
            elif post.__author.vissibility == 2:
                for friend in user.friends_list:
                    if post.author == friend:
                        list_of_vissible.append(post)
            else:
                for friend in user.friends_list:
                    for friend2 in friend.friends_list:
                        if post.author == friend:
                            list_of_vissible.append(post)
                        if post.author == friend2:
                            list_of_vissible.append(post)
        return list_of_vissible
