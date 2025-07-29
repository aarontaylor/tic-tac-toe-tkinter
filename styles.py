"""
Tic-Tac-Toe Game Styling Configuration
Contains all colors, fonts, and styling for the game interface
"""

class GameStyles:
    """Centralized styling configuration for the Tic-Tac-Toe game"""
    
    # Color Palette
    COLORS = {
        # Background colors
        'bg_primary': '#0f0f23',      # Deep dark blue background
        'bg_secondary': '#1a1a2e',    # Slightly lighter dark blue
        'bg_card': '#16213e',         # Dark blue for cards/containers
        'bg_button': '#2d3748',       # Dark gray for buttons
        'bg_button_hover': '#4a5568', # Lighter gray for hover
        
        # Text colors
        'text_primary': '#ffffff',     # Pure white text
        'text_secondary': '#a0a0a0',  # Light gray text
        'text_muted': '#6b7280',      # Muted gray text
        
        # Player colors
        'player_x': '#ff6b6b',        # Coral red for X
        'player_o': '#4ecdc4',        # Teal for O
        'win_highlight': '#ffd93d',   # Golden yellow for wins
        
        # Button colors
        'btn_primary': '#3182ce',     # Modern blue
        'btn_primary_hover': '#2c5aa0',
        'btn_danger': '#e53e3e',      # Modern red
        'btn_danger_hover': '#c53030',
    }
    
    # Font configurations
    FONTS = {
        'title': ('Helvetica', 32, 'bold'),
        'subtitle': ('Helvetica', 12),
        'status': ('Helvetica', 18, 'bold'),
        'board_label': ('Helvetica', 14, 'bold'),
        'button_large': ('Helvetica', 28, 'bold'),
        'button_medium': ('Helvetica', 24, 'bold'),
        'button_small': ('Helvetica', 14, 'bold'),
        'score': ('Helvetica', 12),
    }
    
    # Layout configurations
    LAYOUT = {
        'window_size': '500x650',
        'button_size': (6, 3),
        'padding': 30,
        'grid_padding': 3,
    }
    
    @classmethod
    def get_button_style(cls, player=None, state='normal'):
        """Get button styling based on player and state"""
        if player == 'X':
            return {
                'bg': cls.COLORS['player_x'],
                'fg': cls.COLORS['text_primary'],
                'disabledforeground': cls.COLORS['text_primary'],
                'font': cls.FONTS['button_large'],
                'relief': 'flat',
                'bd': 0
            }
        elif player == 'O':
            return {
                'bg': cls.COLORS['player_o'],
                'fg': cls.COLORS['text_primary'],
                'disabledforeground': cls.COLORS['text_primary'],
                'font': cls.FONTS['button_large'],
                'relief': 'flat',
                'bd': 0
            }
        else:
            return {
                'bg': cls.COLORS['bg_button'],
                'fg': cls.COLORS['text_primary'],
                'disabledforeground': cls.COLORS['text_primary'],
                'font': cls.FONTS['button_medium'],
                'relief': 'flat',
                'bd': 0,
                'activebackground': cls.COLORS['bg_button_hover'],
                'activeforeground': cls.COLORS['text_primary']
            }
    
    @classmethod
    def get_win_style(cls):
        """Get styling for winning combination"""
        return {
            'bg': cls.COLORS['win_highlight'],
            'fg': '#000000',
            'font': cls.FONTS['button_large'],
            'relief': 'flat',
            'bd': 0
        }
    
    @classmethod
    def get_status_style(cls, message_type='normal'):
        """Get status label styling"""
        if message_type == 'win':
            return {
                'fg': cls.COLORS['win_highlight'],
                'font': cls.FONTS['status'],
                'bg': cls.COLORS['bg_card']
            }
        elif message_type == 'tie':
            return {
                'fg': cls.COLORS['text_secondary'],
                'font': cls.FONTS['status'],
                'bg': cls.COLORS['bg_card']
            }
        else:
            return {
                'fg': cls.COLORS['text_primary'],
                'font': cls.FONTS['status'],
                'bg': cls.COLORS['bg_card']
            } 