# Rock Paper Scissors Game

## Overview
This project is a **Rock, Paper, Scissors** game implemented in Python. It allows a human player to compete against the computer in a classic game of chance, using simple rules and Python functions to handle the gameplay. This is my third project, and I'm proud to have utilized custom functions for the first time in Python to make the program cleaner and more modular.

## Features
- **Winning Rules Display**: The game starts by explaining the rules of Rock, Paper, Scissors.
- **Human vs Computer Gameplay**: The user selects their choice, and the computer's choice is randomly generated.
- **Scorekeeping**: The program tracks:
  - Number of games won by the human player.
  - Number of games won by the computer.
  - Number of ties.
- **Replay Option**: The user can decide to play again or quit the game.
- **Summary**: At the end of the session, the game displays the total games played, human wins, computer wins, and tie games.

## How It Works
1. **User Input**: The user selects their move by choosing 1 (Rock), 2 (Paper), or 3 (Scissors).
2. **Computer's Choice**: The computer's move is randomly generated using the `random` module.
3. **Comparison**: The `rules` function compares the human's and computer's choices to determine the winner.
4. **Score Update**: Scores for the human, computer, and ties are updated based on the result of each round.
5. **Replay**: After each round, the user is asked if they want to play again.
6. **Game Summary**: When the user exits, the game prints the final scores and thanks the player.

## Functions
- `rules(Human, Computer)`: Determines the winner of a round and updates scores.
- `computerrand()`: Generates a random choice for the computer and returns it as text.

## Key Learnings
- This was my first time using functions in a Python project, though I had learned about them previously in C++.
- Breaking the program into smaller functions made the code easier to read, understand, and manage.
- I feel more confident in my Python fundamentals and look forward to tackling more challenging projects in the future.

## Future Improvements
- Add more detailed feedback for each round.
- Include a graphical user interface (GUI) to make the game more interactive.
- Allow for multiplayer mode where two users can compete.

## Acknowledgments
This project helped me enhance my understanding of Python functions, randomization, and user input validation. I can't wait to explore more advanced concepts in future projects. 😊

