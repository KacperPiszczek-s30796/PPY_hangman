import random
import os


def get_random_word() -> str:
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


def register(name: str, password: str) -> bool:
    path = "players/"+name+".txt"
    if os.path.exists(path):
        return False
    else:
        with open(path, "w") as file:
            file.write(password)
        return True


def login(name: str, password: str) -> bool:
    path = "players/" + name + ".txt"
    if os.path.exists(path):
        with open(path, "r") as file:
            text = file.read()
        rows = text.strip().split("\n")
        if rows[0].strip() == password.strip():
            return True
        else:
            return False
    else:
        return False


def read_statistics(name: str) -> str:
    path = "players/" + name + ".txt"
    with open(path, "r") as file:
        text = file.read()
    statistics = text.strip().split("\n", 1)
    if len(statistics) == 1:
        return "0\n0\n0\n0"
    return statistics[1]


def write_statistics(name: str, statistics: str) -> bool:
    path = "players/" + name + ".txt"
    with open(path, "r") as file:
        lines = file.readlines()
    first_line = lines[0].strip()
    with open(path, "w") as file:
        file.write(first_line+"\n"+statistics)
    return True


def export(name: str, text: str) -> bool:
    path = "exports/" + name + ".txt"
    with open(path, "w") as file:
        file.write(text)
    return True
