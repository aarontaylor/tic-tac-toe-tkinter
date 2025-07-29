import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.window, 
            text="Tic-Tac-Toe", 
            font=("Arial", 24, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Current player display
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Arial", 16),
            fg="#34495e"
        )
        self.status_label.pack(pady=10)
        
        # Game board frame
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    width=4,
                    height=2,
                    bg="#ecf0f1",
                    fg="#2c3e50",
                    relief="raised",
                    bd=3,
                    command=lambda r=i, c=j: self.make_move(r, c)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)
        
        # Control buttons frame
        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=30)
        
        # New game button
        new_game_btn = tk.Button(
            control_frame,
            text="New Game",
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            command=self.reset_game
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_btn = tk.Button(
            control_frame,
            text="Quit",
            font=("Arial", 14),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            command=self.window.quit
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
    
    def make_move(self, row, col):
        if self.game_over:
            return
            
        index = row * 3 + col
        
        # Check if cell is already occupied
        if self.board[index] != "":
            return
        
        # Make the move
        self.board[index] = self.current_player
        self.buttons[row][col].config(
            text=self.current_player,
            state="disabled",
            bg="#bdc3c7" if self.current_player == "X" else "#95a5a6",
            fg="#2c3e50"
        )
        
        # Check for win or tie
        if self.check_winner():
            self.game_over = True
            self.status_label.config(
                text=f"Player {self.current_player} wins!",
                fg="#27ae60",
                font=("Arial", 16, "bold")
            )
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        elif self.check_tie():
            self.game_over = True
            self.status_label.config(
                text="It's a tie!",
                fg="#f39c12",
                font=("Arial", 16, "bold")
            )
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(
                text=f"Player {self.current_player}'s turn",
                fg="#34495e"
            )
    
    def check_winner(self):
        # Define winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] == self.current_player):
                # Highlight winning combination
                for i in combo:
                    row, col = i // 3, i % 3
                    self.buttons[row][col].config(bg="#2ecc71")
                return True
        return False
    
    def check_tie(self):
        return all(cell != "" for cell in self.board)
    
    def reset_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Reset status label
        self.status_label.config(
            text=f"Player {self.current_player}'s turn",
            fg="#34495e",
            font=("Arial", 16)
        )
        
        # Reset all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text="",
                    state="normal",
                    bg="#ecf0f1",
                    fg="#2c3e50"
                )
    
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
