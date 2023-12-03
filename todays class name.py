import tkinter as tk
import random

class RandomFriendPickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Friend Picker")

        self.friends = ["Friend 1", "Friend 2", "Friend 3", "Friend 4", "Friend 5"]

        self.label = tk.Label(master, text="Click 'Pick a Friend' to get a random friend!")
        self.label.pack(pady=10)

        self.pick_button = tk.Button(master, text="Pick a Friend", command=self.pick_random_friend)
        self.pick_button.pack(pady=10)

    def pick_random_friend(self):
        random_friend = random.choice(self.friends)
        self.display_result(random_friend)

    def display_result(self, friend):
        result_window = tk.Toplevel(self.master)
        result_window.title("Result")
        result_label = tk.Label(result_window, text=f"Random Friend: {friend}")
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomFriendPickerApp(root)
    root.mainloop()
