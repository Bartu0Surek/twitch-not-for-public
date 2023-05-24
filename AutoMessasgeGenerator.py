import random
from time import sleep
import pyperclip

def ran():
    x = ["Привет", "Как дела", "Аххах", "Хахахахах", "Тащи", "Топ", "Ты топ", "Имба", "У тебя имба скины", "Рил","Блин", "Айайайайай", "Нажми alt f4", "Го эйс с ножа",
         "Го эйс с ссг", "Го эйс с дигла", "!myaccount", "Тащии", "Фаст", "Харош", "Найс", "Эльпримо", "Ты бот"]
    return random.choice(x)


while True:
    pyperclip.copy(ran())
    sleep(1)