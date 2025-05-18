import tkinter as tk
from tkinter import ttk


class HangmanGUI:
    def __init__(self):
        import Game_Logic
        self.root = tk.Tk()
        self.root.title("Hang man")
        self.root.geometry("1000x700")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.large_font = ("Arial", 32, "bold")
        self.menu_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)
        self.special_game_frame = tk.Frame(self.root)
        self.end_frame = tk.Frame(self.root)
        self.statistics_frame = tk.Frame(self.root)
        self.settings_frame = tk.Frame(self.root)
        self.settings_category = "random"
        # Menu
        self.menu_label = tk.Label(self.menu_frame, text="Main Menu", font=("Arial", 40))
        self.menu_start = tk.Button(self.menu_frame, text="Start Standard Game")
        self.menu_button2 = tk.Button(self.menu_frame, text="Start Special Game")
        self.menu_settings = tk.Button(self.menu_frame, text="Settings")
        self.menu_player1_label = tk.Label(self.menu_frame, text="Player1", font=("Arial", 24))
        self.menu_player1_name_label = tk.Label(self.menu_frame, text="Name: ", font=("Arial", 24))
        self.menu_player1_name_entry = tk.Entry(self.menu_frame)
        self.menu_player1_Password_label = tk.Label(self.menu_frame, text="Password: ", font=("Arial", 24))
        self.menu_player1_Password_entry = tk.Entry(self.menu_frame, show="*")
        self.menu_player1_login = tk.Button(self.menu_frame, text="Login")
        self.menu_player1_register = tk.Button(self.menu_frame, text="Register")
        self.menu_player1_statistics = tk.Button(self.menu_frame, text="Statistics")

        self.menu_player2_label = tk.Label(self.menu_frame, text="Player2", font=("Arial", 24))
        self.menu_player2_name_label = tk.Label(self.menu_frame, text="Name: ", font=("Arial", 24))
        self.menu_player2_name_entry = tk.Entry(self.menu_frame)
        self.menu_player2_Password_label = tk.Label(self.menu_frame, text="Password: ", font=("Arial", 24))
        self.menu_player2_Password_entry = tk.Entry(self.menu_frame, show="*")
        self.menu_player2_login = tk.Button(self.menu_frame, text="Login")
        self.menu_player2_register = tk.Button(self.menu_frame, text="Register")
        self.menu_player2_statistics = tk.Button(self.menu_frame, text="Statistics")

        self.menu_label.grid(row=0, column=0)
        self.menu_start.grid(row=1, column=0)
        self.menu_button2.grid(row=1, column=1)
        self.menu_settings.grid(row=1, column=2)
        self.menu_player1_label.grid(row=3, column=0)
        self.menu_player1_name_label.grid(row=4, column=0)
        self.menu_player1_name_entry.grid(row=4, column=1)
        self.menu_player1_Password_label.grid(row=4, column=2)
        self.menu_player1_Password_entry.grid(row=4, column=3)
        self.menu_player1_login.grid(row=5, column=0)
        self.menu_player1_register.grid(row=5, column=1)
        self.menu_player1_statistics.grid(row=5, column=2)

        self.menu_player2_label.grid(row=6, column=0)
        self.menu_player2_name_label.grid(row=7, column=0)
        self.menu_player2_name_entry.grid(row=7, column=1)
        self.menu_player2_Password_label.grid(row=7, column=2)
        self.menu_player2_Password_entry.grid(row=7, column=3)
        self.menu_player2_login.grid(row=8, column=0)
        self.menu_player2_register.grid(row=8, column=1)
        self.menu_player2_statistics.grid(row=8, column=2)

        self.menu_start.config(command=lambda: (self.show_frame(self.game_frame), Game_Logic.setup_standard_mode(self, self.settings_category)))
        self.menu_button2.config(command=lambda: (self.show_frame(self.special_game_frame), Game_Logic.setup_special_mode(self, self.settings_category)))
        self.menu_player1_register.config(command=lambda: Game_Logic.register_player1(self.menu_player1_name_entry.get(), self.menu_player1_Password_entry.get()))
        self.menu_player2_register.config(command=lambda: Game_Logic.register_player2(self.menu_player2_name_entry.get(), self.menu_player2_Password_entry.get()))
        self.menu_player1_login.config(command=lambda: Game_Logic.login_player1(self.menu_player1_name_entry.get(), self.menu_player1_Password_entry.get()))
        self.menu_player2_login.config(command=lambda: Game_Logic.login_player2(self.menu_player2_name_entry.get(), self.menu_player2_Password_entry.get()))
        self.menu_player1_statistics.config(command=lambda: (self.show_frame(self.statistics_frame), self.set_statistics_frame(1)))
        self.menu_player2_statistics.config(command=lambda: (self.show_frame(self.statistics_frame), self.set_statistics_frame(2)))
        self.menu_settings.config(command=lambda: self.show_frame(self.settings_frame))
        # end
        self.end_label = tk.Label(self.end_frame, text="Game ended", font=("Arial", 24))
        self.end_button = tk.Button(self.end_frame, text="Back to menu")
        self.end_player1_label = tk.Label(self.end_frame, text="Player1: ", font=("Arial", 24))
        self.end_player1_button = tk.Button(self.end_frame, text="Export results")
        self.end_player2_label = tk.Label(self.end_frame, text="Player2: ", font=("Arial", 24))
        self.end_player2_button = tk.Button(self.end_frame, text="Export results")

        self.end_label.grid(row=0, column=0)
        self.end_button.grid(row=1, column=0)
        self.end_player1_label.grid(row=2, column=0)
        self.end_player1_button.grid(row=2, column=1)
        self.end_player2_label.grid(row=3, column=0)
        self.end_player2_button.grid(row=3, column=1)

        self.end_button.config(command=lambda: (self.show_frame(self.menu_frame), Game_Logic.clear()))
        self.end_player1_button.config(command=lambda: Game_Logic.export_player1())
        self.end_player2_button.config(command=lambda: Game_Logic.export_player2())
        # Game
        self.label = tk.Label(self.game_frame, text="Enter letter/word:")
        self.entry = tk.Entry(self.game_frame)
        self.button = tk.Button(self.game_frame, text="Submit")
        self.image0 = tk.PhotoImage(file="png/hangman0.png")
        self.labelI = tk.Label(self.game_frame, image=self.image0)
        self.I_counter = 0
        self.word = tk.Label(self.game_frame, text=Game_Logic.get_word(), font=self.large_font)

        self.labelI.grid(row=0, column=0)
        self.word.grid(row=0, column=1)
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)

        self.button.config(command=lambda: Game_Logic.on_submit(self.entry.get(), self))

        # statistics
        self.statistics_Label = tk.Label(self.statistics_frame, text="Statistics")
        self.statistics_button = tk.Button(self.statistics_frame, text="Back to menu")
        self.statistics_data = tk.Label(self.statistics_frame, text="")

        self.statistics_Label.grid(row=0, column=0)
        self.statistics_button.grid(row=1, column=0)
        self.statistics_data.grid(row=2, column=0)

        self.statistics_button.config(command=lambda: (self.show_frame(self.menu_frame), self.clear_statistics()))

        # settings
        self.settings_label = tk.Label(self.settings_frame, text="Settings")
        self.settings_button = tk.Button(self.settings_frame, text="Back to menu")
        self.settings_label_category = tk.Label(self.settings_frame, text="Category: ")
        self.settings_combobox_category = ttk.Combobox(self.settings_frame, values=Game_Logic.get_categories())
        self.settings_label_time = tk.Label(self.settings_frame, text="special mode settings:")
        self.settings_label_time_minutes = tk.Label(self.settings_frame, text="minutes: ")
        self.settings_label_time_seconds = tk.Label(self.settings_frame, text="seconds: ")
        self.settings_entry_time_minutes = tk.Entry(self.settings_frame)
        self.settings_entry_time_seconds = tk.Entry(self.settings_frame)
        self.settings_button_time = tk.Button(self.settings_frame, text="Save time")
        self.settings_label_word_number = tk.Label(self.settings_frame, text="number of additional words: ")
        self.settings_entry_word_number = tk.Entry(self.settings_frame)
        self.settings_button_word_number = tk.Button(self.settings_frame, text="Save number of additional words")

        self.settings_label.grid(row=0, column=0)
        self.settings_button.grid(row=1, column=0)
        self.settings_label_category.grid(row=2, column=0)
        self.settings_combobox_category.grid(row=2, column=1)
        self.settings_label_time.grid(row=3, column=0)
        self.settings_label_time_minutes.grid(row=4, column=0)
        self.settings_label_time_seconds.grid(row=4, column=2)
        self.settings_entry_time_minutes.grid(row=4, column=1)
        self.settings_entry_time_seconds.grid(row=4, column=3)
        self.settings_button_time.grid(row=4, column=4)
        self.settings_label_word_number.grid(row=5, column=0)
        self.settings_entry_word_number.grid(row=5, column=1)
        self.settings_button_word_number.grid(row=5, column=2)

        self.settings_button.config(command=lambda: self.show_frame(self.menu_frame))
        self.settings_combobox_category.current(0)
        self.settings_combobox_category.bind("<<ComboboxSelected>>", self.on_select)
        self.settings_button_time.config(command=lambda: self.set_time(self.settings_entry_time_minutes.get(), self.settings_entry_time_seconds.get()))
        self.settings_button_word_number.config(command=lambda: Game_Logic.set_word_number(self.settings_entry_word_number.get()))

        # Special Game
        self.special_label = tk.Label(self.special_game_frame, text="Enter letter/word:")
        self.special_entry = tk.Entry(self.special_game_frame)
        self.special_button = tk.Button(self.special_game_frame, text="Submit")
        self.special_image0 = tk.PhotoImage(file="png/hangman0.png")
        self.special_labelI = tk.Label(self.special_game_frame, image=self.special_image0)
        self.special_I_counter = 0
        self.special_word = tk.Label(self.special_game_frame, text=Game_Logic.get_word(), font=self.large_font, wraplength=350,  justify="left")
        self.special_time = tk.Label(self.special_game_frame, text="")

        self.special_time.grid(row=0, column=0)
        self.special_labelI.grid(row=1, column=0)
        self.special_word.grid(row=1, column=1)
        self.special_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.special_entry.grid(row=2, column=1, padx=10, pady=10)
        self.special_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.special_button.config(command=lambda: Game_Logic.special_on_submit(self.special_entry.get(), self))

    def set_time(self, minutes, seconds):
        import Game_Logic
        try:
            Game_Logic.set_timer(int(minutes), int(seconds))
        except ValueError:
            print("failed to save time")

    def on_select(self, event):
        selected = self.settings_combobox_category.get()
        self.settings_category = selected

    def repeated_over_time_code(self):
        import Game_Logic
        check_time = Game_Logic.check_time_over(self)
        self.special_time.config(text=check_time[1])
        if not check_time[0]:
            self.root.after(1000, self.repeated_over_time_code)

    def next_image(self):
        self.I_counter += 1
        image_path = "png/hangman" + str(self.I_counter) + ".png"
        image = tk.PhotoImage(file=image_path)
        self.labelI.configure(image=image)
        self.labelI.image = image
        return self.I_counter

    def special_next_image(self):
        self.special_I_counter += 1
        image_path = "png/hangman" + str(self.special_I_counter) + ".png"
        image = tk.PhotoImage(file=image_path)
        self.special_labelI.configure(image=image)
        self.special_labelI.image = image
        return self.special_I_counter

    def update_word(self):
        import Game_Logic
        self.word.configure(text=Game_Logic.get_word())

    def special_update_word(self):
        import Game_Logic
        self.special_word.configure(text=Game_Logic.get_word())

    def show_frame(self, frame_to_show):
        import Game_Logic
        if not (not Game_Logic.are_there_players() and (frame_to_show == self.game_frame or frame_to_show == self.special_game_frame)):
            if frame_to_show == self.game_frame or frame_to_show == self.special_game_frame:
                self.entry.delete(0, tk.END)
                self.special_entry.delete(0, tk.END)
                image_path = "png/hangman0.png"
                image = tk.PhotoImage(file=image_path)
                self.labelI.configure(image=image)
                self.labelI.image = image
                self.special_labelI.configure(image=image)
                self.special_labelI.image = image

            for frame in (self.menu_frame, self.game_frame, self.end_frame, self.statistics_frame, self.settings_frame, self.special_game_frame):
                frame.grid_forget()
            frame_to_show.grid(row=0, column=0, sticky="nsew")

    def set_statistics_frame(self, player: int):
        import Game_Logic
        if Game_Logic.is_player_defined(player):
            self.statistics_data.config(text=Game_Logic.get_statistics(player))

    def clear_statistics(self):
        self.statistics_data.config(text="")

    def start(self):
        self.show_frame(self.menu_frame)
        self.root.mainloop()

    def end(self):
        image_path = "png/hangman0.png"
        image = tk.PhotoImage(file=image_path)
        self.special_labelI.configure(image=image)
        self.special_labelI.image = image
        self.labelI.configure(image=image)
        self.labelI.image = image
        self.special_I_counter = 0
        self.I_counter = 0
        self.show_frame(self.end_frame)
