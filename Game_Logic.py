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


def setup_standard_mode(gui: GUI.HangmanGUI):
    if are_there_players():
        global word
        global current_word_state
        word = Database_Logic.get_random_word()
        for i in range(0, len(word)):
            current_word_state += "_ "
        print(word)
        gui.update_word()


def are_there_players() -> bool:
    if player1 != "" and player2 != "":
        return True
    else:
        return False


def is_player_defined(player: int) -> bool:
    if player == 1 and player1 != "":
        return True
    elif player == 2 and player2 != "":
        return True
    else:
        return False


def get_word() -> str:
    global current_word_state
    return current_word_state


def update_statistics(name: str, hits: int = 0, misses: int = 0, wins: int = 0, losses: int = 0):
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
    global player1, player2
    if player == 1:
        name = player1
    else:
        name = player2
    stats = Database_Logic.read_statistics(name).split("\n")
    result = "hits: "+stats[0]+"\nmisses: "+stats[1]+"\nwins: "+stats[2]+"\nlosses: "+stats[3]
    return result


def on_submit(entry: str, gui: GUI.HangmanGUI):
    global word, current_word_state, player1, player2, turn, hits1, hits2, misses1, misses2, win
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


def export_player1():
    if win:
        result = "\nresult: won"
    else:
        result = "\nresult: lost"
    if Database_Logic.export(player1, "hits: "+str(hits1)+"\nmisses: "+str(misses1)+result):
        print("player successfully exported")
    else:
        print("failed to export player")


def export_player2():
    if win:
        result = "\nresult: won"
    else:
        result = "\nresult: lost"
    if Database_Logic.export(player2, "hits: " + str(hits2) + "\nmisses: " + str(misses2) + result):
        print("player successfully exported")
    else:
        print("failed to export player")


def clear():
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
