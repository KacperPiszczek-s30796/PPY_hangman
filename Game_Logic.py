import textwrap
from datetime import datetime, timedelta
import Database_Logic
import GUI

word = ""
current_word_state = ""
player1 = ""
player2 = ""
turn = 0
hits1 = 0
misses1 = 0
hits2 = 0
misses2 = 0
win = True
clock_start = datetime.now()
timer = timedelta(minutes=2)
word_number = 1
guessed_words = ""


def get_guessed_words() -> str:
    """Returns the string of guessed letters or words so far.

        Returns:
            str: A comma-separated string of guessed entries.
        """
    global guessed_words
    return guessed_words


def set_timer(minutes: int = 2, seconds: int = 0):
    """Sets the countdown timer for the game.

        Args:
            minutes (int): Minutes to set. Defaults to 2.
            seconds (int): Seconds to set. Defaults to 0.
        """
    global timer
    timer = timedelta(minutes=minutes, seconds=seconds)


def set_word_number(number: str):
    """Sets how many words will be used in special mode.

        Args:
            number (str): The number of words as a string.
        """
    global word_number
    try:
        word_number = int(number)
    except ValueError:
        print("failed to save number")


def setup_standard_mode(gui: GUI.HangmanGUI, category: str):
    """Initializes the game in standard mode with a word from a given category.

        Args:
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
            category (str): The category to select the word from. Can be 'random'.
        """
    if are_there_players():
        global word
        global current_word_state
        if category == "random":
            word = Database_Logic.get_random_word()
        else:
            word = Database_Logic.get_word_from_category(category)
        for i in word.strip():
            current_word_state += "_"
        print(word)
        print(current_word_state)
        gui.update_word()


def setup_special_mode(gui: GUI.HangmanGUI, category: str):
    """Initializes the game in special mode with multiple words.

       Args:
           gui (GUI.HangmanGUI): The GUI instance to update the interface.
           category (str): The category to select words from. Can be 'random'.
       """
    if are_there_players():
        global word, current_word_state, clock_start, word_number
        clock_start = datetime.now()
        gui.repeated_over_time_code()
        if category == "random":
            word = Database_Logic.get_random_word()
        else:
            word = Database_Logic.get_word_from_category(category)
        for i in range(word_number):
            if category == "random":
                word += " "+Database_Logic.get_random_word()
            else:
                word += " "+Database_Logic.get_word_from_category(category)
        word = word.strip()
        for i in word:
            if i == ' ':
                current_word_state += " "
            else:
                current_word_state += "_"
        print(word)
        print(current_word_state)
        gui.special_update_word()


def check_time_over(gui: GUI.HangmanGUI) -> [bool, str]:
    """Checks whether the game timer has run out.

        Args:
            gui (GUI.HangmanGUI): The GUI instance to call game-end behavior.

        Returns:
            list[bool, str]: [True, remaining_time_str] if time is up, else [False, remaining_time_str].
        """
    global clock_start, player1, player2, win, timer
    remaining_time = timer - (datetime.now() - clock_start)
    if remaining_time.total_seconds() < 0:
        update_statistics(player1, losses=1)
        update_statistics(player2, losses=1)
        win = False
        gui.end(win)
        return [True, str(remaining_time)]
    return [False, str(remaining_time)]


def are_there_players() -> bool:
    """Checks if both players are registered or logged in.

        Returns:
            bool: True if both players are set, False otherwise.
        """
    if player1 != "" and player2 != "":
        return True
    else:
        return False


def is_player_defined(player: int) -> bool:
    """Checks if a player is defined (registered or logged in).

        Args:
            player (int): Player number (1 or 2).

        Returns:
            bool: True if the specified player is set, False otherwise.
        """
    if player == 1 and player1 != "":
        return True
    elif player == 2 and player2 != "":
        return True
    else:
        return False


def get_word() -> str:
    """Formats and returns the current masked word with line breaks.

        Returns:
            str: The formatted masked word with line breaks every 10 characters.
        """
    global current_word_state
    result = "\n".join(textwrap.wrap(current_word_state, width=10))
    return " ".join(result)


def get_categories() -> list[str]:
    """Fetches the list of word categories including 'random'.

        Returns:
            list[str]: A list of category names.
        """
    result = Database_Logic.get_categories()
    result.insert(0, "random")
    return result


def update_statistics(name: str, hits: int = 0, misses: int = 0, wins: int = 0, losses: int = 0):
    """Updates the player statistics in the database.

        Args:
            name (str): Player name.
            hits (int): Number of hits to add. Defaults to 0.
            misses (int): Number of misses to add. Defaults to 0.
            wins (int): Number of wins to add. Defaults to 0.
            losses (int): Number of losses to add. Defaults to 0.
        """
    statistics = Database_Logic.read_statistics(name).split("\n")
    new_hits = str(int(statistics[0])+hits)
    new_misses = str(int(statistics[1])+misses)
    new_wins = str(int(statistics[2])+wins)
    new_losses = str(int(statistics[3])+losses)
    new_statistics = new_hits+"\n"+new_misses+"\n"+new_wins+"\n"+new_losses
    if Database_Logic.write_statistics(name, new_statistics):
        print("statistics successfully updated")
    else:
        print("Error while updating statistics")


def get_statistics(player: int) -> str:
    """Retrieves and formats the statistics for the specified player.

        Args:
            player (int): Player number (1 or 2).

        Returns:
            str: A formatted string of player statistics.
        """
    global player1, player2
    if player == 1:
        name = player1
    else:
        name = player2
    stats = Database_Logic.read_statistics(name).split("\n")
    result = "hits: "+stats[0]+"\nmisses: "+stats[1]+"\nwins: "+stats[2]+"\nlosses: "+stats[3]
    return result


def update_word_state(w, c_w_s, e):
    """Updates the masked word state based on a correct guess.

        Args:
            w (str): The full word or phrase.
            c_w_s (str): Current masked word state.
            e (str): The guessed letter or word.

        Returns:
            str: Updated masked word state.
        """
    print("uws: "+w+" "+c_w_s+" "+e)
    w = w.lower()
    e = e.lower()
    result = list(c_w_s)
    start = 0
    while True:
        idx = w.find(e, start)
        if idx == -1:
            break
        for i in range(len(e)):
            result[idx + i] = e[i]
        start = idx + 1
    return ''.join(result)


def on_submit(entry: str, gui: GUI.HangmanGUI):
    """Handles user input during standard mode and updates the game state.

        Args:
            entry (str): The guessed letter or word.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """
    global word, current_word_state, player1, player2, turn, hits1, hits2, misses1, misses2, win, guessed_words
    print("letter/word entered:", entry)
    entry = entry.strip().lower()
    if entry in word.lower():
        if turn % 2 == 0:
            update_statistics(player1, hits=1)
            hits1 += 1
        else:
            update_statistics(player2, hits=1)
            hits2 += 1
        print("correct")
        current_word_state = update_word_state(word, current_word_state, entry)
        gui.update_word()
        if current_word_state == word:
            update_statistics(player1, wins=1)
            update_statistics(player2, wins=1)
            gui.end(win)
    else:
        guessed_words += entry+", "
        gui.update_word()
        if turn % 2 == 0:
            update_statistics(player1, misses=1)
            misses1 += 1
        else:
            update_statistics(player2, misses=1)
            misses2 += 1
        print("incorrect")
        i_counter = gui.next_image()
        if i_counter >= 12:
            update_statistics(player1, losses=1)
            update_statistics(player2, losses=1)
            win = False
            gui.end(win)
    turn += 1


def special_on_submit(entry: str, gui: GUI.HangmanGUI):
    """Handles user input during special mode and updates the game state.

        Args:
            entry (str): The guessed letter or word.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """
    global word, current_word_state, player1, player2, turn, hits1, hits2, misses1, misses2, win, guessed_words
    print("letter/word entered:", entry)
    entry = entry.strip().lower()
    if entry in word.lower():
        if turn % 2 == 0:
            update_statistics(player1, hits=1)
            hits1 += 1
        else:
            update_statistics(player2, hits=1)
            hits2 += 1
        print("correct")
        current_word_state = current_word_state = update_word_state(word, current_word_state, entry)
        gui.special_update_word()
        if current_word_state == word:
            update_statistics(player1, wins=1)
            update_statistics(player2, wins=1)
            gui.end(win)
    else:
        guessed_words += entry + ", "
        gui.special_update_word()
        if turn % 2 == 0:
            update_statistics(player1, misses=1)
            misses1 += 1
        else:
            update_statistics(player2, misses=1)
            misses2 += 1
        print("incorrect")
        i_counter = gui.special_next_image()
        if i_counter >= 12:
            update_statistics(player1, losses=1)
            update_statistics(player2, losses=1)
            win = False
            gui.end(win)
    turn += 1


def register_player1(name: str, password: str, gui: GUI.HangmanGUI):
    """Registers player 1 using the provided credentials.

        Args:
            name (str): Username.
            password (str): Password.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """
    global player1
    if Database_Logic.register(name, password):
        print("successfully registered")
        gui.player1_logged_in()
        player1 = name
    else:
        print("failed to register")


def register_player2(name: str, password: str, gui: GUI.HangmanGUI):
    """Registers player 2 using the provided credentials.

        Args:
            name (str): Username.
            password (str): Password.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """
    global player2
    if Database_Logic.register(name, password):
        print("successfully registered")
        gui.player2_logged_in()
        player2 = name
    else:
        print("failed to register")


def login_player1(name: str, password: str, gui: GUI.HangmanGUI):
    """Logs in player 1 using the provided credentials.

        Args:
            name (str): Username.
            password (str): Password.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """

    global player1
    if Database_Logic.login(name, password):
        print("successfully logged in")
        gui.player1_logged_in()
        player1 = name
    else:
        print("failed to log in")


def login_player2(name: str, password: str, gui: GUI.HangmanGUI):
    """Logs in player 2 using the provided credentials.

        Args:
            name (str): Username.
            password (str): Password.
            gui (GUI.HangmanGUI): The GUI instance to update the interface.
        """
    global player2
    if Database_Logic.login(name, password):
        print("successfully logged in")
        gui.player2_logged_in()
        player2 = name
    else:
        print("failed to log in")


def export_player1():
    """Exports player 1's game result and statistics to the database."""
    if win:
        result = "\nresult: won"
    else:
        result = "\nresult: lost"
    if Database_Logic.export(player1, "hits: "+str(hits1)+"\nmisses: "+str(misses1)+result):
        print("player successfully exported")
    else:
        print("failed to export player")


def export_player2():
    """Exports player 2's game result and statistics to the database."""
    if win:
        result = "\nresult: won"
    else:
        result = "\nresult: lost"
    if Database_Logic.export(player2, "hits: " + str(hits2) + "\nmisses: " + str(misses2) + result):
        print("player successfully exported")
    else:
        print("failed to export player")


def clear(gui: GUI.HangmanGUI):
    """Resets the game state and clears player information.

        Args:
            gui (GUI.HangmanGUI): The GUI instance to reset interface state.
        """
    global player1, player2, word, current_word_state, turn, hits1, misses1, hits2, misses2, win
    player1 = ""
    player2 = ""
    word = ""
    current_word_state = ""
    turn = 0
    hits1 = 0
    misses1 = 0
    hits2 = 0
    misses2 = 0
    win = True
    gui.player1_not_logged_in()
    gui.player2_not_logged_in()
