import random
import os


def get_random_word():
    with open("Categories.txt", "r") as file:
        category = file.read()
    categories = category.strip().split("\n")
    rand = random.randint(0, len(categories)-1)
    path = "Words/"+categories[rand]+".txt"
    try:
        with open(path, "r") as file:
            word = file.read()
        words = word.strip().split("\n")
        rand = random.randint(0, len(words)-1)
        return words[rand]
    except Exception as e:
        print("Error while loading word", e)
        return "Error"


def register(name: str, password: str):
    path = "players/"+name+".txt"
    if os.path.exists(path):
        return False
    else:
        with open(path, "w") as file:
            file.write(password)
        return True
