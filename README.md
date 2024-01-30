# Tic Tac Toe Game - README

Welcome to your Tic Tac Toe Game! This README provides an overview of your Python-based Tic Tac Toe game, a classic two-player game developed using the `uib_inf100_graphics` module. The game features a graphical user interface and interactive gameplay.

## Overview

This Tic Tac Toe game is a graphical Python application where two players take turns to mark the spaces in a 3×3 grid with 'X' and 'O'. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. The game provides a simple yet engaging user interface and checks for the winning conditions automatically.

## Features

- **Graphical User Interface**: The game board and elements are displayed graphically.
- **Interactive Gameplay**: Players interact with the game by clicking on the grid to place their 'X' or 'O'.
- **Automatic Win Detection**: The game automatically detects and announces a winner.
- **Turn Management**: The game keeps track of which player's turn it is and displays the information.

## How to Play

1. **Start the Game**: Run the script to launch the game window.
2. **Gameplay**: Players take turns clicking on a cell in the 3x3 grid to mark it with their symbol ('X' or 'O').
3. **Winning the Game**: The first player to align three of their symbols horizontally, vertically, or diagonally wins. The game announces the winner and displays it on the screen.
4. **Draw**: If all cells are filled without a winning combination, the game ends in a draw.

## Components

### Key Functions

- **`app_started(app)`**: Initializes the game state.
- **`draw_board(app, canvas)`**: Draws the game board on the canvas.
- **`mouse_pressed(app, event)`**: Handles mouse click events to place 'X' or 'O' on the board.
- **`check_winner(app)`**: Checks for a winning combination on the board.
- **`board_full(app)`**: Checks if the board is full without any winner.
- **`draw_x(canvas, x, y)`**: Draws 'X' on the board.
- **`draw_o(canvas, x, y)`**: Draws 'O' on the board.
- **`redraw_all(app, canvas)`**: Redraws the entire game state on the canvas.

## Setup and Execution

1. **Dependencies**: Ensure Python and `uib_inf100_graphics` module are installed on your system.
2. **Running the Game**: Execute the script in a Python environment to open the game window.
3. **Game Controls**: Players use the mouse to interact with the game.

## Conclusion

This Tic Tac Toe Game provides a basic yet fun experience of the classic game. It is an excellent example of graphical user interface programming in Python and is ideal for learning the basics of event-driven programming and game development.

Enjoy the game, and may the best player win!

---

*Note: This README is crafted for the provided Python script and should be adjusted as necessary to fit the specific details and requirements of your project or assignment.*
