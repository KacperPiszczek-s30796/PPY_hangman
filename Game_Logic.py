import Database_Logic
import GUI

word = ""
current_word_state = ""


def setup_standard_mode(gui: GUI.HangmanGUI):
    global word
    global current_word_state
    word = Database_Logic.get_random_word()
    current_word_state = ""
    for i in range(0, len(word)):
        current_word_state += "_ "
    print(word)
    gui.update_word()


def get_word():
    global current_word_state
    return current_word_state


def on_submit(entry: str, gui: GUI.HangmanGUI):
    global current_word_state
    global word
    print("letter/word entered:", entry)
    entry = entry.strip().lower()
    if entry in word.lower():
        print("correct")
        index = word.find(entry)*2
        entry = " ".join(entry)+" "
        current_word_state = current_word_state[:index]+entry+current_word_state[index+len(entry):]
        gui.update_word()
        if current_word_state == " ".join(word)+" ":
            gui.end()
    else:
        print("incorrect")
        i_counter = gui.next_image()
        if i_counter >= 12:
            gui.end()
