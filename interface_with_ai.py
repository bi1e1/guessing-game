import random as rd
import tkinter as tk

LOW, HIGH, MAX_TRIES = 1, 200, 10

BG = "#0f172a"
CARD = "#1e293b"
TEXT = "#e2e8f0"
MUTED = "#94a3b8"
ACCENT = "#38bdf8"
GREEN = "#22c55e"
RED = "#ef4444"
AMBER = "#f59e0b"


def hint(player, secret):
    if secret > player:
        return "small"
    elif secret < player:
        return "big"
    return "right"


class GuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guess the Number")
        self.geometry("460x680")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.build_ui()
        self.new_game()

    # ---------- UI ----------
    def build_ui(self):
        tk.Label(self, text="GUESS THE NUMBER", bg=BG, fg=ACCENT,
                 font=("Helvetica", 24, "bold")).pack(pady=(30, 0))
        tk.Label(self, text=f"Pick a number between {LOW} and {HIGH}",
                 bg=BG, fg=MUTED, font=("Helvetica", 12)).pack(pady=(4, 20))

        # attempts dots
        self.dots = tk.Canvas(self, width=MAX_TRIES * 30, height=24,
                              bg=BG, highlightthickness=0)
        self.dots.pack()
        tk.Label(self, text="attempts", bg=BG, fg=MUTED,
                 font=("Helvetica", 10)).pack(pady=(2, 20))

        # message card
        card = tk.Frame(self, bg=CARD)
        card.pack(padx=30, fill="x")
        self.message = tk.Label(card, text="", bg=CARD, fg=TEXT,
                                font=("Helvetica", 20, "bold"), height=2)
        self.message.pack(pady=(14, 0))
        self.range_label = tk.Label(card, text="", bg=CARD, fg=MUTED,
                                    font=("Helvetica", 12))
        self.range_label.pack(pady=(0, 16))

        # input
        self.entry = tk.Entry(self, justify="center", font=("Helvetica", 28, "bold"),
                              bg=CARD, fg=TEXT, insertbackground=TEXT,
                              relief="flat", highlightthickness=2,
                              highlightbackground=CARD, highlightcolor=ACCENT, width=6)
        self.entry.pack(pady=(26, 14), ipady=8)
        self.entry.bind("<Return>", lambda e: self.on_guess())

        self.guess_btn = self.make_button("Guess", ACCENT, self.on_guess)
        self.guess_btn.pack(pady=4)

        # history
        tk.Label(self, text="your guesses", bg=BG, fg=MUTED,
                 font=("Helvetica", 10)).pack(pady=(24, 6))
        self.history = tk.Frame(self, bg=BG)
        self.history.pack()

        self.again_btn = self.make_button("New game", AMBER, self.new_game)
        self.again_btn.pack(side="bottom", pady=(0, 14))
        tk.Label(self, text="built by bilel k. - 2026", bg=BG, fg=MUTED,
                 font=("Helvetica", 9)).pack(side="bottom", pady=(0, 8))

    def make_button(self, text, color, command):
        btn = tk.Label(self, text=text, bg=color, fg=BG, cursor="hand2",
                       font=("Helvetica", 14, "bold"), padx=36, pady=10)
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", lambda e: btn.config(bg=TEXT))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        btn.base_color = color
        return btn

    # ---------- game ----------
    def new_game(self):
        self.secret = rd.randint(LOW, HIGH)
        self.guesses = []
        self.lo, self.hi = LOW, HIGH
        self.over = False
        self.entry.config(state="normal")
        self.entry.delete(0, "end")
        self.entry.focus_set()
        self.message.config(text="Make your first guess", fg=TEXT)
        self.range_label.config(text=f"The number is between {self.lo} and {self.hi}")
        for w in self.history.winfo_children():
            w.destroy()
        self.draw_dots()

    def draw_dots(self, color=ACCENT):
        self.dots.delete("all")
        for i in range(MAX_TRIES):
            x = i * 30 + 4
            fill = color if i < len(self.guesses) else CARD
            self.dots.create_oval(x, 2, x + 20, 22, fill=fill, outline="")

    def add_chip(self, number, color):
        i = len(self.guesses) - 1
        tk.Label(self.history, text=str(number), bg=CARD, fg=color,
                 font=("Helvetica", 12, "bold"), width=5, pady=4
                 ).grid(row=i // 5, column=i % 5, padx=4, pady=4)

    def on_guess(self):
        if self.over:
            return
        try:
            player = int(self.entry.get())
        except ValueError:
            self.show_error()
            return
        if player < LOW or player > HIGH:
            self.show_error()
            return

        self.entry.delete(0, "end")
        self.guesses.append(player)
        result = hint(player, self.secret)

        if result == "small":
            self.lo = max(self.lo, player + 1)
            self.message.config(text="Too small  ↑", fg=AMBER)
            self.add_chip(player, AMBER)
        elif result == "big":
            self.hi = min(self.hi, player - 1)
            self.message.config(text="Too big  ↓", fg=RED)
            self.add_chip(player, RED)
        else:
            self.message.config(text=f"Bravo! {len(self.guesses)} guesses", fg=GREEN)
            self.add_chip(player, GREEN)
            self.draw_dots(GREEN)
            self.finish()
            return

        self.range_label.config(text=f"The number is between {self.lo} and {self.hi}")
        self.draw_dots()
        if len(self.guesses) == MAX_TRIES:
            self.message.config(text=f"Game over! It was {self.secret}", fg=RED)
            self.draw_dots(RED)
            self.finish()

    def finish(self):
        self.over = True
        self.entry.config(state="disabled")

    def show_error(self):
        self.entry.delete(0, "end")
        self.message.config(text=f"Numbers {LOW} to {HIGH} only", fg=RED)


if __name__ == "__main__":
    GuessGame().mainloop()
