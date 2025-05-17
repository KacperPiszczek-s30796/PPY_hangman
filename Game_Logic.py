import Database_Logic
import GUI

word = ""
current_word_state = ""
player1 = ""
player2 = ""
turn = 0


def setup_standard_mode(gui: GUI.HangmanGUI):
    global word
    global current_word_state
    word = Database_Logic.get_random_word()
    current_word_state = ""
    for i in range(0, len(word)):
        current_word_state += "_ "
    print(word)
    gui.update_word()


def get_word() -> str:
    global current_word_state
    return current_word_state


def update_statistics(name: str, hits: int = 0, misses: int = 0, wins: int = 0, losses: int = 0):
    statistics = Database_Logic.read_statistics(name).split("\n")
    if len(statistics) < 4:
        statistics = ["0", "0", "0", "0"]
    new_hits = str(int(statistics[0])+hits)
    new_misses = str(int(statistics[1])+misses)
    new_wins = str(int(statistics[2])+wins)
    new_losses = str(int(statistics[3])+losses)
    new_statistics = new_hits+"\n"+new_misses+"\n"+new_wins+"\n"+new_losses
    if Database_Logic.write_statistics(name, new_statistics):
        print("statistics successfully updated")
    else:
        print("Error while updating statistics")


def on_submit(entry: str, gui: GUI.HangmanGUI):
    global current_word_state
    global word
    global player1
    global player2
    global turn
    print("letter/word entered:", entry)
    entry = entry.strip().lower()
    if entry in word.lower():
        if turn % 2 == 0:
            update_statistics(player1, hits=1)
        else:
            update_statistics(player2, hits=1)
        print("correct")
        index = word.find(entry)*2
        entry = " ".join(entry)+" "
        current_word_state = current_word_state[:index]+entry+current_word_state[index+len(entry):]
        gui.update_word()
        if current_word_state == " ".join(word)+" ":
            update_statistics(player1, wins=1)
            update_statistics(player2, wins=1)
            gui.end()
    else:
        if turn % 2 == 0:
            update_statistics(player1, misses=1)
        else:
            update_statistics(player2, misses=1)
        print("incorrect")
        i_counter = gui.next_image()
        if i_counter >= 12:
            update_statistics(player1, losses=1)
            update_statistics(player2, losses=1)
            gui.end()
    turn += 1


def register_player1(name: str, password: str):
    global player1
    if Database_Logic.register(name, password):
        print("successfully registered")
        player1 = name
    else:
        print("failed to register")


def register_player2(name: str, password: str):
    global player2
    if Database_Logic.register(name, password):
        print("successfully registered")
        player2 = name
    else:
        print("failed to register")


def login_player1(name: str, password: str):
    global player1
    if Database_Logic.login(name, password):
        print("successfully logged in")
        player1 = name
    else:
        print("failed to log in")


def login_player2(name: str, password: str):
    global player2
    if Database_Logic.login(name, password):
        print("successfully logged in")
        player2 = name
    else:
        print("failed to log in")
