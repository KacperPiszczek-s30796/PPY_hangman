import random
import os


def encrypt(text: str) -> str:
    """
        Encrypts a string by shifting letters and digits forward by 1.
        Wraps around alphabetically and numerically.

        :param text: The input string to encrypt.
        :return: The encrypted string.
        """
    result = []
    for c in text:
        if 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + 1) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') + 1) % 10 + ord('0')))
        else:
            result.append(c)
    return ''.join(result)


def decrypt(text: str) -> str:
    """
        Decrypts a string that was encrypted with the `encrypt` function,
        shifting letters and digits backward by 1.

        :param text: The encrypted string to decrypt.
        :return: The original decrypted string.
        """
    result = []
    for c in text:
        if 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') - 1) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') - 1) % 26 + ord('a')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') - 1) % 10 + ord('0')))
        else:
            result.append(c)
    return ''.join(result)


def get_random_word() -> str:
    """
        Returns a random word from a randomly selected category file listed in 'Categories.txt'.

        :return: A random word, or "Error" if something fails.
        """
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


def get_word_from_category(category: str) -> str:
    """
        Returns a random word from a given category file.

        :param category: The name of the category file (without extension).
        :return: A random word from the category, or "Error" if it fails.
        """
    path = "Words/"+category+".txt"
    try:
        with open(path, "r") as file:
            word = file.read()
        words = word.strip().split("\n")
        rand = random.randint(0, len(words)-1)
        return words[rand]
    except Exception as e:
        print("Error while loading word", e)
        return "Error"


def get_categories() -> list[str]:
    """
        Returns a list of all available word categories from 'Categories.txt'.

        :return: A list of category names.
        """
    with open("Categories.txt", "r") as file:
        category = file.read()
    categories = category.strip().split("\n")
    return categories


def register(name: str, password: str) -> bool:
    """
        Registers a new player by encrypting and storing their password.

        :param name: The username of the player.
        :param password: The password of the player.
        :return: True if registration succeeds, False if the user already exists.
        """
    name = encrypt(name)
    password = encrypt(password)
    path = "players/"+name+".txt"
    if os.path.exists(path):
        return False
    else:
        with open(path, "w") as file:
            file.write(password)
        return True


def login(name: str, password: str) -> bool:
    """
        Validates a player's login credentials.

        :param name: The username of the player.
        :param password: The password to check.
        :return: True if login is successful, False otherwise.
        """
    name = encrypt(name)
    password = encrypt(password)
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
    """
        Reads and decrypts the game statistics of a player.

        :param name: The username of the player.
        :return: A decrypted statistics string, or default stats if none exist.
        """
    name = encrypt(name)
    path = "players/" + name + ".txt"
    with open(path, "r") as file:
        text = file.read()
    statistics = text.strip().split("\n", 1)
    if len(statistics) == 1:
        return "0\n0\n0\n0"
    return decrypt(statistics[1])


def write_statistics(name: str, statistics: str) -> bool:
    """
        Writes encrypted game statistics for a player.

        :param name: The username of the player.
        :param statistics: A string containing player statistics to store.
        :return: True if write was successful.
        """
    name = encrypt(name)
    statistics = encrypt(statistics)
    path = "players/" + name + ".txt"
    with open(path, "r") as file:
        lines = file.readlines()
    first_line = lines[0].strip()
    with open(path, "w") as file:
        file.write(first_line+"\n"+statistics)
    return True


def export(name: str, text: str) -> bool:
    """
        Exports a given text to a file in the 'exports/' directory.

        :param name: The name of the export file (without extension).
        :param text: The content to write into the file.
        :return: True if export was successful.
        """
    path = "exports/" + name + ".txt"
    with open(path, "w") as file:
        file.write(text)
    return True
