"""
Tic-Tac-Toe Game UI
Handles the visual interface and user interactions
"""

import tkinter as tk

class GameUI:
    """Handles the game user interface"""
    
    def __init__(self, window, game_logic, on_move_callback):
        self.window = window
        self.game_logic = game_logic
        self.on_move_callback = on_move_callback
        
        # Colors with better contrast
        self.bg_color = "#0f0f23"
        self.card_color = "#16213e"
        self.text_color = "#ffffff"
        self.x_color = "#ff4757"  # Bright red for X
        self.o_color = "#2ed573"  # Bright green for O
        self.win_color = "#ffa502"  # Bright orange for wins
        self.button_bg = "#2d3748"
        
        # Create UI elements
        self.create_ui()
    
    def create_ui(self):
        """Create the game UI"""
        # Main container
        main_frame = tk.Frame(self.window, bg=self.bg_color)
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="TIC-TAC-TOE",
            font=("Helvetica", 32, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        title_label.pack(pady=(0, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Classic Game, Modern Design",
            font=("Helvetica", 12),
            fg="#a0a0a0",
            bg=self.bg_color
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Status frame
        self.status_frame = tk.Frame(main_frame, bg=self.card_color, relief="flat", bd=0)
        self.status_frame.pack(fill="x", pady=20, ipady=15, ipadx=20)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Player X's Turn",
            font=("Helvetica", 18, "bold"),
            fg=self.text_color,
            bg=self.card_color
        )
        self.status_label.pack()
        
        # Game board
        board_container = tk.Frame(main_frame, bg=self.bg_color)
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
        
        # Board frame with canvas overlay for winning lines
        self.board_frame = tk.Frame(board_container, bg="#1a1a2e", relief="flat", bd=0)
        self.board_frame.pack(padx=20, pady=10, ipadx=20, ipady=20)
        
        # Create buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Helvetica", 28, "bold"),  # Larger font for better visibility
                    width=6,
                    height=3,
                    bg=self.button_bg,
                    fg=self.text_color,
                    relief="flat",
                    bd=0,
                    command=lambda r=i, c=j: self.on_button_click(r, c)
                )
                btn.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
                row.append(btn)
            self.buttons.append(row)
        
        # Configure grid weights
        for i in range(3):
            self.board_frame.grid_rowconfigure(i, weight=1)
            self.board_frame.grid_columnconfigure(i, weight=1)
        
        # Control buttons
        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.pack(pady=30)
        
        # New game button
        new_game_btn = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=("Helvetica", 14, "bold"),
            bg="#3182ce",
            fg=self.text_color,
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            command=self.on_new_game
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_btn = tk.Button(
            control_frame,
            text="❌ Quit",
            font=("Helvetica", 14, "bold"),
            bg="#e53e3e",
            fg=self.text_color,
            padx=30,
            pady=12,
            relief="flat",
            bd=0,
            command=self.window.quit
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Score display
        score_frame = tk.Frame(main_frame, bg=self.card_color, relief="flat", bd=0)
        score_frame.pack(fill="x", pady=20, ipady=10, ipadx=20)
        
        self.score_label = tk.Label(
            score_frame,
            text="Score: X - 0 | O - 0",
            font=("Helvetica", 12),
            fg="#a0a0a0",
            bg=self.card_color
        )
        self.score_label.pack()
        
        # Initialize score
        self.x_score = 0
        self.o_score = 0
    
    def draw_winning_line(self, combo):
        """Draw a line through the winning combination"""
        if not combo or len(combo) < 3:
            return
            
        # Just rely on the button highlighting for now
        # The orange background with larger font makes it clear enough
        pass
    
    def pulse_winning_squares(self, combo, count):
        """Create a pulsing effect on winning squares"""
        if count >= 6 or not self.game_logic.is_game_over():  # Stop after 3 pulses
            return
            
        if hasattr(self, 'winning_labels'):
            for i, label in enumerate(self.winning_labels):
                if i < len(combo):
                    pos = combo[i]
                    value = self.game_logic.get_board()[pos]
                    
                    # Alternate between bright and slightly dimmer colors
                    if count % 2 == 0:
                        if value == "X":
                            bg_color = "#ff6666"  # Lighter red
                        else:
                            bg_color = "#66ff66"  # Lighter green
                    else:
                        if value == "X":
                            bg_color = "#ff0000"  # Bright red
                        else:
                            bg_color = "#00ff00"  # Bright green
                            
                    label.configure(background=bg_color)
            
        # Schedule next pulse
        self.window.after(300, lambda: self.pulse_winning_squares(combo, count + 1))
    
    
    def on_button_click(self, row, col):
        """Handle button click"""
        position = row * 3 + col
        if self.on_move_callback(position):
            # Update display immediately to show the move
            self.update_display()
    
    def on_new_game(self):
        """Handle new game button click"""
        self.game_logic.reset_game()
        
        # Clean up winning labels
        if hasattr(self, 'winning_labels'):
            for label in self.winning_labels:
                label.destroy()
            self.winning_labels = []
            
        self.update_display()
    
    def update_display(self):
        """Update the game display"""
        # Update status
        if self.game_logic.is_game_over():
            if self.game_logic.get_winner():
                self.status_label.config(
                    text=f"🎉 Player {self.game_logic.get_winner()} Wins!",
                    fg=self.win_color
                )
                # Update score
                if self.game_logic.get_winner() == "X":
                    self.x_score += 1
                else:
                    self.o_score += 1
                self.score_label.config(text=f"Score: X - {self.x_score} | O - {self.o_score}")
                
                # Draw winning line
                winning_combo = self.game_logic.get_winning_combo()
                if winning_combo:
                    self.draw_winning_line(winning_combo)
            else:
                self.status_label.config(
                    text="🤝 It's a Tie!",
                    fg="#a0a0a0"
                )
        else:
            self.status_label.config(
                text=f"Player {self.game_logic.get_current_player()}'s Turn",
                fg=self.text_color
            )
        
        # Get winning combo first to know which buttons to handle differently
        winning_combo = self.game_logic.get_winning_combo()
        winning_positions = set(winning_combo) if winning_combo else set()
        
        # Update buttons with guaranteed visibility and proper contrast
        board = self.game_logic.get_board()
        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                pos = i * 3 + j
                value = board[pos]
                
                # Skip winning buttons for now - they'll be handled separately
                if pos in winning_positions:
                    button.configure(text=value)
                    continue
                
                # Completely reconfigure the button for guaranteed visibility
                if value == "X":
                    # Bright red background with white text for X
                    button.configure(
                        text="X",
                        background="#ff4757",  # Bright red
                        foreground="#ffffff",  # Pure white
                        disabledforeground="#ffffff",  # White when disabled
                        state="disabled",
                        font=("Helvetica", 32, "bold"),  # Even larger font
                        relief="flat",
                        bd=0
                    )
                    # Force immediate update
                    button.update_idletasks()
                    button.update()
                    
                elif value == "O":
                    # Bright green background with white text for O
                    button.configure(
                        text="O",
                        background="#2ed573",  # Bright green
                        foreground="#ffffff",  # Pure white
                        disabledforeground="#ffffff",  # White when disabled
                        state="disabled",
                        font=("Helvetica", 32, "bold"),  # Even larger font
                        relief="flat",
                        bd=0
                    )
                    # Force immediate update
                    button.update_idletasks()
                    button.update()
                    
                else:
                    # Empty button
                    button.configure(
                        text="",
                        background=self.button_bg,
                        foreground=self.text_color,
                        state="normal",
                        font=("Helvetica", 32, "bold"),
                        relief="flat",
                        bd=0
                    )
                    # Force immediate update
                    button.update_idletasks()
                    button.update()
        
        # Highlight winning combination with animation effect
        if winning_combo:
            # Store winning labels for cleanup
            if not hasattr(self, 'winning_labels'):
                self.winning_labels = []
                
            # Apply special styling to winning squares
            for pos in winning_combo:
                row, col = pos // 3, pos % 3
                value = self.game_logic.get_board()[pos]
                button = self.buttons[row][col]
                
                # Hide the button
                button.configure(state="disabled", relief="flat", bd=0)
                
                # Create a label overlay with winning colors
                if value == "X":
                    bg_color = "#ff0000"  # Bright red for X wins
                    fg_color = "#ffffff"  # White text
                else:
                    bg_color = "#00ff00"  # Bright green for O wins
                    fg_color = "#000000"  # Black text
                
                # Create label at button position
                label = tk.Label(
                    self.board_frame,
                    text=value,
                    background=bg_color,
                    foreground=fg_color,
                    font=("Helvetica", 44, "bold"),
                    relief="raised",
                    bd=5
                )
                
                # Place label over button
                label.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                self.winning_labels.append(label)
                
            # Add a pulsing effect by scheduling color changes
            self.pulse_winning_squares(winning_combo, 0)
        
        # Force the entire window to update
        self.window.update_idletasks()
        self.window.update() 