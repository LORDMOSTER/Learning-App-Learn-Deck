import random
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# Leaderboard File
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

leaderboard = load_leaderboard()

def update_leaderboard(player, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    leaderboard.append({"player": player, "score": score, "timestamp": timestamp})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    save_leaderboard(leaderboard)

def display_leaderboard():
    leaderboard_text = "\n--- Leaderboard ---\n"
    leaderboard_text += "Rank | Player       | Score | Timestamp\n"
    leaderboard_text += "--------------------------------------------\n"
    for rank, entry in enumerate(leaderboard, start=1):
        leaderboard_text += f"{rank:<4} | {entry['player']:<12} | {entry['score']:<5} | {entry['timestamp']}\n"
    leaderboard_text += "--------------------------------------------\n"
    return leaderboard_text

def reset_leaderboard():
    global leaderboard
    leaderboard = []
    save_leaderboard(leaderboard)
    messagebox.showinfo("Reset", "Leaderboard has been reset.")

class PythonQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Programming Quest")
        self.score = 0
        self.player_name = ""

        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack(pady=20)

        self.intro_label = tk.Label(self.intro_frame, text="Welcome to the Python Programming Quest!", font=("Arial", 16))
        self.intro_label.pack()

        self.start_button = tk.Button(self.intro_frame, text="Start Quest", command=self.start_quest)
        self.start_button.pack(pady=10)

        self.leaderboard_button = tk.Button(self.intro_frame, text="View Leaderboard", command=self.show_leaderboard)
        self.leaderboard_button.pack(pady=10)

    def start_quest(self):
        self.player_name = simpledialog.askstring("Input", "Enter your name:")
        if self.player_name:
            self.intro_frame.pack_forget()
            self.level_1()

    def level_1(self):
        self.level_frame = tk.Frame(self.root)
        self.level_frame.pack(pady=20)

        self.level_label = tk.Label(self.level_frame, text="Level 1: Operators", font=("Arial", 14))
        self.level_label.pack()

        self.question1_label = tk.Label(self.level_frame, text="Question 1: What is the result of 5 + 3 * 2?")
        self.question1_label.pack()

        self.answer1_entry = tk.Entry(self.level_frame)
        self.answer1_entry.pack()

        self.submit1_button = tk.Button(self.level_frame, text="Submit", command=self.check_level_1)
        self.submit1_button.pack(pady=10)

    def check_level_1(self):
        answer = self.answer1_entry.get()
        if answer == "11":
            self.score += 10
            messagebox.showinfo("Correct", "Correct! The multiplication is performed first, then addition.")
        else:
            messagebox.showerror("Incorrect", "Incorrect. Remember: *, /, //, % are evaluated before +, -.")

        self.level_frame.pack_forget()
        self.level_2()

    def level_2(self):
        self.level_frame = tk.Frame(self.root)
        self.level_frame.pack(pady=20)

        self.level_label = tk.Label(self.level_frame, text="Level 2: Conditional Statements", font=("Arial", 14))
        self.level_label.pack()

        self.question2_label = tk.Label(self.level_frame, text="Question: Write a condition to check if a number is even.")
        self.question2_label.pack()

        self.answer2_entry = tk.Entry(self.level_frame)
        self.answer2_entry.pack()

        self.submit2_button = tk.Button(self.level_frame, text="Submit", command=self.check_level_2)
        self.submit2_button.pack(pady=10)

    def check_level_2(self):
        answer = self.answer2
