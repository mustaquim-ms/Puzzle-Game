import tkinter as tk
import random

class PuzzleGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Puzzle Game")
        self.geometry("400x400")

        self.puzzle_size = 4
        self.puzzle_pieces = []
        self.empty_row = self.puzzle_size - 1
        self.empty_col = self.puzzle_size - 1

        self.create_puzzle()
        self.draw_puzzle()

    def create_puzzle(self):
        numbers = list(range(1, self.puzzle_size * self.puzzle_size))
        random.shuffle(numbers)
        self.puzzle_pieces = [numbers[i:i+self.puzzle_size] for i in range(0, len(numbers), self.puzzle_size)]

    def draw_puzzle(self):
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        piece_size = 400 // self.puzzle_size
        for row in range(self.puzzle_size):
            for col in range(self.puzzle_size):
                x1 = col * piece_size
                y1 = row * piece_size
                x2 = x1 + piece_size
                y2 = y1 + piece_size
                if row == self.empty_row and col == self.empty_col:
                    fill_color = "white"
                else:
                    fill_color = "lightblue"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
                self.canvas.create_text(x1 + piece_size // 2, y1 + piece_size // 2, text=str(self.puzzle_pieces[row][col]), font=("Arial", 20))

        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        row = event.y // (400 // self.puzzle_size)
        col = event.x // (400 // self.puzzle_size)

        if (abs(row - self.empty_row) + abs(col - self.empty_col)) == 1:
            self.puzzle_pieces[self.empty_row][self.empty_col] = self.puzzle_pieces[row][col]
            self.puzzle_pieces[row][col] = 0
            self.empty_row = row
            self.empty_col = col
            self.draw_puzzle()

            if self.is_puzzle_solved():
                tk.messagebox.showinfo("Congratulations", "You solved the puzzle!")

    def is_puzzle_solved(self):
        correct_order = list(range(1, self.puzzle_size * self.puzzle_size))
        current_order = [self.puzzle_pieces[row][col] for row in range(self.puzzle_size) for col in range(self.puzzle_size)]
        return current_order == correct_order

if __name__ == "__main__":
    app = PuzzleGame()
    app.mainloop()
