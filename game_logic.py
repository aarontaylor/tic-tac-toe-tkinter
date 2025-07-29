"""
Tic-Tac-Toe Game Logic
Handles board state, win detection, and game rules
"""

class GameLogic:
    """Handles the game logic and state management"""
    
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.winning_combo = None
    
    def make_move(self, position):
        """Make a move at the given position"""
        if self.game_over or self.board[position] != "":
            return False
        
        # Make the move
        self.board[position] = self.current_player
        
        # Check for win
        if self.check_winner():
            self.game_over = True
            self.winner = self.current_player
            return True
        
        # Check for tie
        if self.check_tie():
            self.game_over = True
            return True
        
        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
        return True
    
    def check_winner(self):
        """Check if current player has won"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] == self.current_player):
                self.winning_combo = combo
                return True
        return False
    
    def check_tie(self):
        """Check if the game is a tie"""
        return all(cell != "" for cell in self.board)
    
    def get_board(self):
        """Get current board state"""
        return self.board.copy()
    
    def get_current_player(self):
        """Get current player"""
        return self.current_player
    
    def is_game_over(self):
        """Check if game is over"""
        return self.game_over
    
    def get_winner(self):
        """Get winner (None if tie or no winner)"""
        return self.winner
    
    def get_winning_combo(self):
        """Get winning combination"""
        return self.winning_combo 