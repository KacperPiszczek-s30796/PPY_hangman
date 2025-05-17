import tkinter as tk


class HangmanGUI:
    def __init__(self):
        import Game_Logic
        self.root = tk.Tk()
        self.root.title("Hang man")
        self.root.geometry("1000x700")
        self.large_font = ("Arial", 32, "bold")
        self.menu_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)
        self.end_frame = tk.Frame(self.root)
        # Menu
        self.menu_label = tk.Label(self.menu_frame, text="Main Menu", font=("Arial", 40))
        self.menu_button = tk.Button(self.menu_frame, text="Start Standard Game")
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
        self.menu_button.grid(row=1, column=0)
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

        self.menu_button.config(command=lambda: (self.show_frame(self.game_frame), Game_Logic.setup_standard_mode(self)))
        self.menu_player1_register.config(command=lambda: Game_Logic.register_player1(self.menu_player1_name_entry.get(), self.menu_player1_Password_entry.get()))
        self.menu_player2_register.config(command=lambda: Game_Logic.register_player2(self.menu_player2_name_entry.get(), self.menu_player2_Password_entry.get()))
        self.menu_player1_login.config(command=lambda: Game_Logic.login_player1(self.menu_player1_name_entry.get(), self.menu_player1_Password_entry.get()))
        self.menu_player2_login.config(command=lambda: Game_Logic.login_player2(self.menu_player2_name_entry.get(), self.menu_player2_Password_entry.get()))
        # end
        self.end_label = tk.Label(self.end_frame, text="Game ended", font=("Arial", 24))
        self.end_button = tk.Button(self.end_frame, text="Back to menu", command=lambda: self.show_frame(self.menu_frame))

        self.end_label.grid(row=0, column=0)
        self.end_button.grid(row=1, column=0)

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

    def next_image(self):
        self.I_counter += 1
        image_path = "png/hangman" + str(self.I_counter) + ".png"
        image = tk.PhotoImage(file=image_path)
        self.labelI.configure(image=image)
        self.labelI.image = image
        return self.I_counter

    def update_word(self):
        import Game_Logic
        self.word.configure(text=Game_Logic.get_word())

    def show_frame(self, frame_to_show):
        if frame_to_show == self.game_frame:
            self.entry.delete(0, tk.END)
            image_path = "png/hangman0.png"
            image = tk.PhotoImage(file=image_path)
            self.labelI.configure(image=image)
            self.labelI.image = image

        for frame in (self.menu_frame, self.game_frame, self.end_frame):
            frame.pack_forget()
        frame_to_show.pack(fill="both", expand=True)

    def start(self):
        self.show_frame(self.menu_frame)
        self.root.mainloop()

    def end(self):
        self.show_frame(self.end_frame)
