import machine
import ssd1306
from hcsr04 import HCSR04
from time import sleep, ticks_ms, ticks_diff


# Inicjacja czujników (r - prawy, l - lewy, c - środkowy)
sensor_r = HCSR04(trigger_pin=32, echo_pin=33, echo_timeout_us=10000)
sensor_l = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)
sensor_c = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000)

# Inicjacja elementów do komunikacji - buzzer i dwa silniki wibracyjne
beeper = machine.Pin(4, machine.Pin.OUT)
vib_l1 = machine.Pin(14, machine.Pin.OUT)
vib_r1 = machine.Pin(25, machine.Pin.OUT)

# Inicjacja potencjometru do regulacji zasięgu detekcji przeszkód
pot = machine.ADC(machine.Pin(35))
pot.atten(machine.ADC.ATTN_11DB)


# Inicjacja wyświetlacza OLED (element prezentacji)
display_interval = 100
last_display_update = ticks_ms()
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


while True:
    # Odczyt odległości od przeszkód i wartości potencjometru
    distance_c = sensor_c.distance_cm()
    distance_r = sensor_r.distance_cm()
    distance_l = sensor_l.distance_cm()
    pot_value = pot.read()

    # Przeliczenie wartości potencjometru na zasięg detekcji
    pot_distance = (pot_value / 4096) * 190 + 10

    # Sterowanie buzzerem w zależności od odległości od przeszkód
    if distance_c > pot_distance:
        beeper.value(0)
    else:
        beeper.value(1)


# Aktualizacja wyświetlacza OLED co określony interwał czasowy
current_time = ticks_ms()
if ticks_diff(current_time, last_display_update) >= display_interval:
    oled.fill(0)
    oled.text(f"Prawy: {round(distance_r)}", 0, 0)
    oled.text(f"Lewy: {round(distance_l)}", 0, 10)
    oled.text(f"Srodkowy: {round(distance_c)}", 0, 20)
    oled.text(f"Zasieg: {round(pot_distance)}", 0, 30)
    oled.show()
    last_display_update = current_time
