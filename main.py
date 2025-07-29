"""
Tic-Tac-Toe Game
Main entry point - sets up the game window and connects components
"""

import tkinter as tk
from game_logic import GameLogic
from game_ui import GameUI

class TicTacToeGame:
    """Main game class that connects logic and UI"""
    
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("500x900")
        self.window.resizable(False, False)
        self.window.configure(bg="#0f0f23")
        
        # Create game logic
        self.game_logic = GameLogic()
        
        # Create UI with callback
        self.ui = GameUI(self.window, self.game_logic, self.on_move)
    
    def on_move(self, position):
        """Handle a move from the UI"""
        return self.game_logic.make_move(position)
    
    def run(self):
        """Start the game"""
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()