# Battleship Game

## Overview
Players take turns guessing the location of their opponent's fleet, aiming to sink all their ships. The game features a 10x10 grid for each player, with ships strategically placed and hidden from the opponent.

## Features
- **Customizable Boards**: 10x10 grid for each player.
- **Ship Placement**: Players place 5 ships (Carrier, Battleship, Cruiser, Submarine, Destroyer) with no overlaps.
- **Turn-Based Gameplay**: Players alternate turns to fire shots at their opponent's grid.
- **Hit/Miss Tracking**: Displays hits (`HH`), misses (`M`), and hidden areas.
- **Victory Condition**: The game ends when one player sinks all their opponent’s ships.

![battleship1](https://github.com/user-attachments/assets/1dfaf2dd-d296-4006-ae27-88c636a9a3b7)


---

## How to Play

### **Setup Phase**
1. Each player has their own 10x10 grid.
2. Players place their ships by entering:
   - Starting coordinates (`x y`).
   - Direction (`r` for right or `d` for down`).
3. Ships cannot overlap and must fit within the grid.

### **Gameplay**
1. Players alternate turns to fire shots by entering target coordinates (`x y`).
2. Shots result in:
   - **Hit**: If a ship occupies the target cell (`HH`).
   - **Miss**: If no ship is in the target cell (`M`).
3. Players are notified if they sink a ship (e.g., "You sunk the Battleship!").

   ![battleship2](https://github.com/user-attachments/assets/ac70df11-dedd-4e87-bfb7-57ec6b5cbd15)


### **Winning the Game**
- A player wins by sinking all their opponent's ships.
- If no winner is determined after a set number of turns, the game ends in a draw.




