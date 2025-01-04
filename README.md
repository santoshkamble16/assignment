`README.txt`

# Game of Tic-Tac-Toe  
**Author:** Mr. Santosh Kamble  


## **Introduction**
This project implements the classic **Tic Tac Toe** game in two versions:  
1. A **text-based version** using basic Python for terminal gameplay.  
2. A **graphical version** using Pygame for an interactive experience.

Both versions allow two players to play alternately until a winner is determined or the game ends in a draw.


## **Project Directories**
- **`text_based/`**  
  Contains the **text-based Tic Tac Toe** implementation in Python.  
  File: `tic_tac_toe_text.py`
  
- **`pygame_version/`**  
  Contains the **graphical Tic Tac Toe** implementation using Pygame.  
  File: `tic_tac_toe_pygame.py`


## **How to Run the Game**

### **1. Prerequisites**
- **Python 3.x** installed on your system.  
- Install Pygame for the graphical version:
  ```bash
  pip install pygame
  ```

### **2. Running the Text-Based Version**
1. Navigate to the `text_based/` directory:
   ```bash
   cd text_based
   ```
2. Run the game:
   ```bash
   python tic_tac_toe_text.py
   ```
3. Follow the terminal prompts to play the game.

### **3. Running the Graphical Version**
1. Navigate to the `pygame_version/` directory:
   ```bash
   cd pygame_version
   ```
2. Run the game:
   ```bash
   python tic_tac_toe_pygame.py
   ```
3. Enjoy the interactive game by clicking on the cells to play.


## **Features**

### **Text-Based Version**
- **Turn-Based Gameplay:** Players "X" and "O" take alternate turns.
- **Winner Detection:** Automatically detects a winner or a draw.
- **Input Validation:** Ensures valid input for row and column numbers.

### **Graphical Version**
- **Interactive Gameplay:** Players click on cells to place their marks.
- **Smooth Graphics:** Uses Pygame to render a visually appealing grid and symbols.
- **Automatic Restart:** Resets the game after a win or draw.
- **Winner/Draw Announcement:** Displays a message before restarting.
