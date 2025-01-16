# My Blackjack Game!

Welcome to my **Blackjack Game** project! This project provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) for the classic card game, implemented in Python.

## Features

- **Command-Line Version**:
  - Play Blackjack in the terminal.
  - Implements game logic with modular, testable code.

- **Graphical Version**:
  - A GUI built with Pygame.
  - Interactive gameplay with graphical card rendering.

- **Comprehensive Unit Tests**:
  - Tests for all key components (deck, cards, hand, player).

## Getting Started

### Prerequisites

- Python 3.8 or later
- Recommended: A virtual environment

### Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/CamVale/Blackjack-Game.git
   cd blackjack-game
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

#### Command-Line Version
To play the CLI version:
```bash
python -m src.blackjack_game
```

#### Graphical Version (Pygame)
To play the GUI version:
```bash
python -m src.pygame_version.blackjack_pygame
```

### Running Tests

Run all tests using:
```bash
python -m unittest discover test
```

## Project Structure

```plaintext
Blackjack-Game/
|
├── src/                    # Source code for the project
│   ├── __init__.py         # Marks the src directory as a Python package
│   ├── blackjack_game.py   # Main CLI version of the game
│   ├── card.py             # Card class implementation
│   ├── deck.py             # Deck class implementation
│   ├── hand.py             # Hand class implementation
│   ├── player.py           # Player class implementation
│   ├── pygame_version/     # Graphical implementation using Pygame
│       ├── __init__.py
│       ├── blackjack_pygame.py  # Main Pygame script
│       ├── constants.py    # Configuration values for Pygame
│       ├── assets/         # Images and resources for Pygame
│       ├── back.png        # Card back image
├── test/                   # Test files for the project
│   ├── test_card.py        # Tests for the Card class
│   ├── test_deck.py        # Tests for the Deck class
│   ├── test_hand.py        # Tests for the Hand class
│   ├── test_player.py      # Tests for the Player class
├── README.md               # Detailed instructions for setup, usage, and testing
├── requirements.txt        # Dependencies for the project
```


- Pygame documentation: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
- Wikipedia: [Blackjack](https://en.wikipedia.org/wiki/Blackjack)

