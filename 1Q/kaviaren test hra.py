import tkinter as tk
from tkinter import messagebox
import random

class CoffeeGame:
    def __init__(self, root):
        self.root = root
        root.title("Coffee Tycoon ☕")
        root.geometry("500x500")
        root.resizable(False, False)

        # Game variables
        self.N = 1           # Number of cafes
        self.C = 5           # Coffee price
        self.M = 500         # Customers
        self.a = 80          # Coffee appeal
        self.V = 3           # Coffee quality
        self.q = 70          # Salary
        self.Z = 1           # Workers
        self.rent = 50       # Rent
        self.moneyz = 500    # Money saved
        self.D = 1           # Day counter
        self.last_profit = 0 # Last profit

        self.create_ui()
        self.update_display()

    def create_ui(self):
        # Labels
        self.info_label = tk.Label(self.root, text="", justify="left", font=("Consolas", 12))
        self.info_label.pack(pady=10)

        # Buttons
        actions = [
            ("Ad campaign (-100)", self.ad_campaign),
            ("Improve quality (-15 cost)", self.quality_plus),
            ("Lower quality (+15 cost)", self.quality_minus),
            ("Recruit (+1 worker, +500)", self.recruit),
            ("Fire (-1 worker)", self.fire),
            ("Expand café (-1000)", self.expand),
            ("Make it fancy (-500)", self.make_fancy),
            ("Next Day →", self.next_day)
        ]
        for text, command in actions:
            tk.Button(self.root, text=text, command=command, width=25).pack(pady=2)

    def update_display(self):
        text = (
            f"📅 Day: {self.D}\n"
            f"💰 Money: {self.moneyz:.2f}\n"
            f"📈 Last Profit: {self.last_profit:.2f}\n"
            f"🏪 Cafés: {self.N}\n"
            f"☕ Coffee price: {self.C}\n"
            f"👷 Workers: {self.Z}\n"
            f"💵 Salary: {self.q}\n"
            f"✨ Quality: {self.V}\n"
            f"🏠 Rent: {self.rent}\n"
        )
        self.info_label.config(text=text)

    def calculate_profit(self):
        Ml = 1000 + self.Z * 500
        if self.q > 100:
            Ml *= 1.2
        elif self.q > 80:
            Ml *= 1.1
        elif self.q < 60:
            Ml *= 0.9
        elif self.q < 50:
            Ml *= 0.8
        elif self.q < 40:
            Ml = 0

        I = random.uniform(0.8, 1.2)
        P = I * self.N * (self.C * (self.M - self.a * self.C) - self.V * (self.M - self.a * self.C) - self.q * self.Z - self.rent)
        return P

    # Actions
    def ad_campaign(self):
        if self.moneyz >= 100:
            self.moneyz -= 100
            self.M += 50
            self.update_display()
        else:
            messagebox.showinfo("Not enough money!", "You need at least 100.")

    def quality_plus(self):
        self.a -= 15
        self.V += 1
        self.update_display()

    def quality_minus(self):
        self.a += 15
        self.V = max(1, self.V - 1)
        self.update_display()

    def recruit(self):
        self.moneyz -= 500
        self.Z += 1
        self.update_display()

    def fire(self):
        if self.Z > 0:
            self.Z -= 1
            self.update_display()
        else:
            messagebox.showinfo("Error", "You have no workers to fire!")

    def expand(self):
        if self.moneyz >= 1000:
            self.moneyz -= 1000
            self.N += 1
            self.update_display()
        else:
            messagebox.showinfo("Not enough money!", "You need at least 1000.")

    def make_fancy(self):
        if self.moneyz >= 500:
            self.moneyz -= 500
            self.a -= 15
            self.M += 100
            self.rent += 50
            self.update_display()
        else:
            messagebox.showinfo("Not enough money!", "You need at least 500.")

    def next_day(self):
        profit = self.calculate_profit()
        self.last_profit = profit
        self.moneyz += profit
        self.D += 1
        self.update_display()

        if self.moneyz < -100:
            messagebox.showinfo("Game Over", "You went bankrupt! ☠️")
            self.root.destroy()

# Run the game
root = tk.Tk()
app = CoffeeGame(root)
root.mainloop()
