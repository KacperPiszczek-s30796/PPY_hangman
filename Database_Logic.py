import random


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
