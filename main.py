import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("500x650")
        self.window.resizable(False, False)
        
        # Modern dark theme with gradient-like appearance
        self.bg_color = "#0f0f23"  # Deep dark blue
        self.accent_color = "#1a1a2e"  # Slightly lighter dark blue
        self.primary_color = "#16213e"  # Dark blue for cards
        self.text_color = "#ffffff"  # Pure white text
        self.x_color = "#ff6b6b"  # Coral red for X
        self.o_color = "#4ecdc4"  # Teal for O
        self.win_color = "#ffd93d"  # Golden yellow for wins
        self.button_bg = "#2d3748"  # Dark gray for buttons
        self.button_hover = "#4a5568"  # Lighter gray for hover
        
        self.window.configure(bg=self.bg_color)
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main container with padding
        main_container = tk.Frame(self.window, bg=self.bg_color)
        main_container.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Title with modern styling
        title_frame = tk.Frame(main_container, bg=self.bg_color)
        title_frame.pack(fill="x", pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="TIC-TAC-TOE", 
            font=("Helvetica", 32, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Classic Game, Modern Design",
            font=("Helvetica", 12),
            fg="#a0a0a0",
            bg=self.bg_color
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Current player display with card-like appearance
        status_frame = tk.Frame(main_container, bg=self.primary_color, relief="flat", bd=0)
        status_frame.pack(fill="x", pady=20, ipady=15, ipadx=20)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"Player {self.current_player}'s Turn",
            font=("Helvetica", 18, "bold"),
            fg=self.text_color,
            bg=self.primary_color
        )
        self.status_label.pack()
        
        # Game board with modern styling
        board_container = tk.Frame(main_container, bg=self.bg_color)
        board_container.pack(pady=30)
        
        # Board title
        board_title = tk.Label(
            board_container,
            text="Game Board",
            font=("Helvetica", 14, "bold"),
            fg="#a0a0a0",
            bg=self.bg_color
        )
        board_title.pack(pady=(0, 15))
        
        # Game board frame with rounded appearance
        board_frame = tk.Frame(board_container, bg=self.accent_color, relief="flat", bd=0)
        board_frame.pack(padx=20, pady=10, ipadx=20, ipady=20)
        
        # Create 3x3 grid of buttons with modern styling
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    board_frame,
                    text="",
                    font=("Helvetica", 24, "bold"),
                    width=6,
                    height=3,
                    bg=self.button_bg,
                    fg=self.text_color,
                    relief="flat",
                    bd=0,
                    activebackground=self.button_hover,
                    activeforeground=self.text_color,
                    command=lambda r=i, c=j: self.make_move(r, c)
                )
                btn.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
                row.append(btn)
            self.buttons.append(row)
        
        # Configure grid weights for responsive layout
        for i in range(3):
            board_frame.grid_rowconfigure(i, weight=1)
            board_frame.grid_columnconfigure(i, weight=1)
        
        # Control buttons with modern design
        control_container = tk.Frame(main_container, bg=self.bg_color)
        control_container.pack(fill="x", pady=30)
        
        # Control buttons frame
        control_frame = tk.Frame(control_container, bg=self.bg_color)
        control_frame.pack()
        
        # New game button with gradient-like appearance
        new_game_btn = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=("Helvetica", 14, "bold"),
            bg="#3182ce",  # Modern blue
            fg=self.text_color,
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            activebackground="#2c5aa0",
            activeforeground=self.text_color,
            command=self.reset_game
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button with modern red styling
        quit_btn = tk.Button(
            control_frame,
            text="❌ Quit",
            font=("Helvetica", 14, "bold"),
            bg="#e53e3e",  # Modern red
            fg=self.text_color,
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            activebackground="#c53030",
            activeforeground=self.text_color,
            command=self.window.quit
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Score display (optional enhancement)
        score_frame = tk.Frame(main_container, bg=self.primary_color, relief="flat", bd=0)
        score_frame.pack(fill="x", pady=20, ipady=10, ipadx=20)
        
        self.score_label = tk.Label(
            score_frame,
            text="Score: X - 0 | O - 0",
            font=("Helvetica", 12),
            fg="#a0a0a0",
            bg=self.primary_color
        )
        self.score_label.pack()
        
        # Initialize score
        self.x_score = 0
        self.o_score = 0
    
    def make_move(self, row, col):
        if self.game_over:
            return
            
        index = row * 3 + col
        
        # Check if cell is already occupied
        if self.board[index] != "":
            return
        
        # Make the move
        self.board[index] = self.current_player
        
        # Enhanced styling for X and O with better contrast
        if self.current_player == "X":
            self.buttons[row][col].config(
                text=self.current_player,
                state="disabled",
                bg=self.x_color,
                fg="#ffffff",
                disabledforeground="#ffffff",
                font=("Helvetica", 28, "bold")
            )
        else:  # Player O
            self.buttons[row][col].config(
                text=self.current_player,
                state="disabled",
                bg=self.o_color,
                fg="#ffffff",
                disabledforeground="#ffffff",
                font=("Helvetica", 28, "bold")
            )
        
        # Check for win or tie
        if self.check_winner():
            self.game_over = True
            self.x_score += 1 if self.current_player == "X" else 0
            self.o_score += 1 if self.current_player == "O" else 0
            self.update_score()
            self.status_label.config(
                text=f"🎉 Player {self.current_player} Wins!",
                fg=self.win_color,
                font=("Helvetica", 18, "bold"),
                bg=self.primary_color
            )
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        elif self.check_tie():
            self.game_over = True
            self.status_label.config(
                text="🤝 It's a Tie!",
                fg="#a0a0a0",
                font=("Helvetica", 18, "bold"),
                bg=self.primary_color
            )
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(
                text=f"Player {self.current_player}'s Turn",
                fg=self.text_color,
                bg=self.primary_color
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
                # Highlight winning combination with animation-like effect
                for i in combo:
                    row, col = i // 3, i % 3
                    self.buttons[row][col].config(
                        bg=self.win_color, 
                        fg="#000000",
                        font=("Helvetica", 32, "bold")
                    )
                return True
        return False
    
    def check_tie(self):
        return all(cell != "" for cell in self.board)
    
    def update_score(self):
        self.score_label.config(text=f"Score: X - {self.x_score} | O - {self.o_score}")
    
    def reset_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Reset status label
        self.status_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg=self.text_color,
            font=("Helvetica", 18, "bold"),
            bg=self.primary_color
        )
        
        # Reset all buttons with smooth transition
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text="",
                    state="normal",
                    bg=self.button_bg,
                    fg=self.text_color,
                    disabledforeground=self.text_color,
                    font=("Helvetica", 24, "bold")
                )
    
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()