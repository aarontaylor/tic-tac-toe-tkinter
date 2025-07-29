# Tic-Tac-Toe Game

A modern, graphical implementation of the classic Tic-Tac-Toe game built with Python and tkinter. Features a dark theme, animated winning combinations, and a clean user interface.

## Features

- Two-player gameplay (X vs O)
- Modern dark-themed interface
- Animated winning combinations with colored highlights
- Score tracking across multiple games
- Play Again functionality
- Visual feedback for game state
- Responsive UI with fixed-size game board

## Requirements

- Python 3.6 or higher
- tkinter (included with most Python installations)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tic-tac-toe-tkinter.git
cd tic-tac-toe-tkinter
```

2. Run the game:
```bash
python main.py
```

## Code Structure

The application is organized into four main modules:

### main.py
The entry point of the application. Contains the `TicTacToeGame` class which:
- Creates and configures the main window
- Initializes the game logic and UI components
- Handles the connection between UI events and game logic
- Manages the main game loop

### game_logic.py
Contains the `GameLogic` class which manages:
- Game state and board representation
- Move validation and execution
- Win condition detection (rows, columns, diagonals)
- Tie game detection
- Player turn management
- Game reset functionality

### game_ui.py
Contains the `GameUI` class responsible for:
- Creating and managing all visual elements
- Handling user input (button clicks)
- Updating the display based on game state
- Managing winning animations and highlights
- Score display and tracking
- Play Again button functionality

### styles.py
Centralized styling configuration including:
- Color palette definitions
- Font specifications
- Button styling functions
- Layout configurations
- Theme consistency helpers

## Game Flow

1. **Initialization**: The main window is created with a fixed size (500x900px)
2. **Game Setup**: Empty 3x3 grid is displayed with Player X starting
3. **Gameplay**: Players alternate clicking empty squares
4. **Move Processing**: Each click validates the move, updates the board, and checks for win/tie
5. **Game End**: Winning combinations are highlighted, Play Again button is enabled
6. **Reset**: New game clears the board and resets all states

## Key Features Implementation

### Winning Detection
The game checks for wins after each move by examining:
- All three rows (positions 0-2, 3-5, 6-8)
- All three columns (positions 0,3,6 / 1,4,7 / 2,5,8)
- Both diagonals (positions 0,4,8 / 2,4,6)

### Visual Feedback
- **Normal squares**: Gray background with white/colored text
- **Winning squares**: Bright colored backgrounds (red for X, green for O)
- **Game status**: Dynamic status bar showing current player or winner
- **Score tracking**: Persistent score display across games

### UI Responsiveness
- Fixed button dimensions prevent layout shifts during gameplay
- Consistent font sizes maintain visual stability
- Proper state management ensures UI reflects game state accurately

## Customization

### Colors
Modify the color scheme by editing values in `game_ui.py`:
- `self.bg_color`: Main background color
- `self.button_bg`: Game button background
- `self.text_color`: Primary text color
- Player colors in the winning highlight section

### Board Size
To change the game board size:
1. Modify button dimensions in the `create_ui` method
2. Update window geometry in `main.py`
3. Adjust padding and spacing values as needed

### Fonts
Font settings can be modified in the button creation sections:
- Game buttons: Currently set to "Helvetica", 24pt, bold
- UI elements: Various sizes defined per component

## Development Notes

### Architecture Decisions
- **Separation of Concerns**: Logic, UI, and styling are kept in separate modules
- **Event-Driven Design**: UI events trigger logic updates through callbacks
- **State Management**: Game state is centralized in the GameLogic class
- **Fixed Layout**: Button dimensions are fixed to prevent UI shifting

### Potential Enhancements
- Add computer AI opponent
- Implement different difficulty levels
- Add sound effects
- Create different visual themes
- Add game statistics tracking
- Implement network multiplayer

## Testing

The game can be tested by:
1. Running `python main.py`
2. Playing complete games to verify win detection
3. Testing all winning combinations (rows, columns, diagonals)
4. Verifying tie game scenarios
5. Testing the Play Again functionality
6. Checking score persistence across games

## Contributing

When contributing to this project:
1. Maintain the existing code structure and separation of concerns
2. Follow the established naming conventions
3. Test all game scenarios before submitting changes
4. Update this README if adding new features
5. Ensure compatibility with the existing UI layout

## License

This project is open source and available under the MIT License.