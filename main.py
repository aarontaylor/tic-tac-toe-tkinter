import tkinter as tk
from tkinter import messagebox
from styles import GameStyles

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry(GameStyles.LAYOUT['window_size'])
        self.window.resizable(False, False)
        self.window.configure(bg=GameStyles.COLORS['bg_primary'])
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Initialize score
        self.x_score = 0
        self.o_score = 0
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main container with padding
        main_container = tk.Frame(self.window, bg=GameStyles.COLORS['bg_primary'])
        main_container.pack(expand=True, fill="both", padx=GameStyles.LAYOUT['padding'], pady=GameStyles.LAYOUT['padding'])
        
        # Title with modern styling
        title_frame = tk.Frame(main_container, bg=GameStyles.COLORS['bg_primary'])
        title_frame.pack(fill="x", pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="TIC-TAC-TOE", 
            font=GameStyles.FONTS['title'],
            fg=GameStyles.COLORS['text_primary'],
            bg=GameStyles.COLORS['bg_primary']
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Classic Game, Modern Design",
            font=GameStyles.FONTS['subtitle'],
            fg=GameStyles.COLORS['text_secondary'],
            bg=GameStyles.COLORS['bg_primary']
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Current player display with card-like appearance
        status_frame = tk.Frame(main_container, bg=GameStyles.COLORS['bg_card'], relief="flat", bd=0)
        status_frame.pack(fill="x", pady=20, ipady=15, ipadx=20)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"Player {self.current_player}'s Turn",
            font=GameStyles.FONTS['status'],
            fg=GameStyles.COLORS['text_primary'],
            bg=GameStyles.COLORS['bg_card']
        )
        self.status_label.pack()
        
        # Game board with modern styling
        board_container = tk.Frame(main_container, bg=GameStyles.COLORS['bg_primary'])
        board_container.pack(pady=30)
        
        # Board title
        board_title = tk.Label(
            board_container,
            text="Game Board",
            font=GameStyles.FONTS['board_label'],
            fg=GameStyles.COLORS['text_secondary'],
            bg=GameStyles.COLORS['bg_primary']
        )
        board_title.pack(pady=(0, 15))
        
        # Game board frame with rounded appearance
        board_frame = tk.Frame(board_container, bg=GameStyles.COLORS['bg_secondary'], relief="flat", bd=0)
        board_frame.pack(padx=20, pady=10, ipadx=20, ipady=20)
        
        # Create 3x3 grid of buttons with modern styling
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    board_frame,
                    text="",
                    **GameStyles.get_button_style(),
                    width=GameStyles.LAYOUT['button_size'][0],
                    height=GameStyles.LAYOUT['button_size'][1],
                    command=lambda r=i, c=j: self.make_move(r, c)
                )
                btn.grid(row=i, column=j, padx=GameStyles.LAYOUT['grid_padding'], pady=GameStyles.LAYOUT['grid_padding'], sticky="nsew")
                # Ensure proper initial rendering
                btn.update()
                row.append(btn)
            self.buttons.append(row)
        
        # Configure grid weights for responsive layout
        for i in range(3):
            board_frame.grid_rowconfigure(i, weight=1)
            board_frame.grid_columnconfigure(i, weight=1)
        
        # Control buttons with modern design
        control_container = tk.Frame(main_container, bg=GameStyles.COLORS['bg_primary'])
        control_container.pack(fill="x", pady=30)
        
        # Control buttons frame
        control_frame = tk.Frame(control_container, bg=GameStyles.COLORS['bg_primary'])
        control_frame.pack()
        
        # New game button with gradient-like appearance
        new_game_btn = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=GameStyles.FONTS['button_small'],
            bg=GameStyles.COLORS['btn_primary'],
            fg=GameStyles.COLORS['text_primary'],
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            activebackground=GameStyles.COLORS['btn_primary_hover'],
            activeforeground=GameStyles.COLORS['text_primary'],
            command=self.reset_game
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button with modern red styling
        quit_btn = tk.Button(
            control_frame,
            text="❌ Quit",
            font=GameStyles.FONTS['button_small'],
            bg=GameStyles.COLORS['btn_danger'],
            fg=GameStyles.COLORS['text_primary'],
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            activebackground=GameStyles.COLORS['btn_danger_hover'],
            activeforeground=GameStyles.COLORS['text_primary'],
            command=self.window.quit
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Score display
        score_frame = tk.Frame(main_container, bg=GameStyles.COLORS['bg_card'], relief="flat", bd=0)
        score_frame.pack(fill="x", pady=20, ipady=10, ipadx=20)
        
        self.score_label = tk.Label(
            score_frame,
            text="Score: X - 0 | O - 0",
            font=GameStyles.FONTS['score'],
            fg=GameStyles.COLORS['text_secondary'],
            bg=GameStyles.COLORS['bg_card']
        )
        self.score_label.pack()
    
    def make_move(self, row, col):
        if self.game_over:
            return
            
        index = row * 3 + col
        
        # Check if cell is already occupied
        if self.board[index] != "":
            return
        
        # Make the move
        self.board[index] = self.current_player
        
        # Apply proper styling with colored backgrounds
        if self.current_player == "X":
            self.apply_button_style(row, col, "X", GameStyles.COLORS['player_x'])
        else:  # Player O
            self.apply_button_style(row, col, "O", GameStyles.COLORS['player_o'])
        
        # Check for win or tie
        if self.check_winner():
            self.game_over = True
            self.x_score += 1 if self.current_player == "X" else 0
            self.o_score += 1 if self.current_player == "O" else 0
            self.update_score()
            self.status_label.config(
                text=f"🎉 Player {self.current_player} Wins!",
                **GameStyles.get_status_style('win')
            )
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        elif self.check_tie():
            self.game_over = True
            self.status_label.config(
                text="🤝 It's a Tie!",
                **GameStyles.get_status_style('tie')
            )
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(
                text=f"Player {self.current_player}'s Turn",
                **GameStyles.get_status_style()
            )
    
    def apply_button_style(self, row, col, text, color):
        """Apply proper styling to button with guaranteed visibility"""
        button = self.buttons[row][col]
        button.config(
            text=text,
            state="disabled",
            bg=color,
            fg=GameStyles.COLORS['text_primary'],
            disabledforeground=GameStyles.COLORS['text_primary'],
            font=GameStyles.FONTS['button_large'],
            relief="flat",
            bd=0
        )
        button.update()
        # Force a small delay to ensure rendering
        self.window.after(10, lambda: button.update())
    
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
                    self.buttons[row][col].config(**GameStyles.get_win_style())
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
            **GameStyles.get_status_style()
        )
        
        # Reset all buttons with consistent styling
        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.config(
                    text="",
                    state="normal",
                    **GameStyles.get_button_style()
                )
                button.update()
    
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()