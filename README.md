# breakout-game
*A simple rendition of the classic Breakout game.*

## What does this project do?
This project uses an Object-Oriented Approach to recreate this popular arcade game in PyGame. OOP is especially useful as different sprites such as the tiles, the ball, and the paddle can be represented with objects. It also allowed me to inherit from PyGame’s base ‘Sprite’ class to utilise its methods and be able to add objects to sprite groups later on. This approach also facilitated development and testing as each class is mostly self-contained. Finally, it makes the code more maintainable because each sprite can be adapted simply by adjusting the attributes and methods in its class.

Overview of each code file:
- 'main.py': contains the PyGame event loop.
- 'game.py': contains the Game class, which handles game logic, sprites, collisions, and user inputs.
- 'paddle.py': contains the Paddle class, which creates a paddle rect and handles user inputs.
- 'ball.py': contains the Ball class, which creates a ball rect.
- 'tile.py': contains the Tile class, which creates a tile rect.
- 'settings.py': contains a list of constants used throughout the program.

---

## System requirements
- Software: Python 3, PyGame
- Memory: 4GB RAM
- OS: 64-bit Windows 7 or later or OS X 10.11 or later
- Processor: 1.5GHz
- Free HDD space: 3GB
- Hardware: keyboard, mouse

---

## Using the application
1. Open 'settings.py' and adjust constants if necessary.
2. Install PyGame: `$ pip install pygame`
3. `$ python main.py`

---

## How to play
- Use the arrow keys to move the paddle left and right, so you can redirect the ball to break the tiles.
- The aim of the game is to break all of the tiles and get a maximum of 80 points.
- You will lose a life if the ball falls past the bottom of the screen.
- You only have 5 lives before you lose the game.
- After the game ends, press space to play again.

---

## Bugs and Future Improvements
Bugs:
- Making the ball move at any angle: since the ball can only move at 45 degree angles, it sometimes becomes stuck in a loop and the player cannot finish the game.

Potential improvements and additions:
- Main menu: this will make the application more user-friendly, as it will not start immediately.
- Pause option: this can improve usability of the application.
- Sound effects: sounds could play whenever the ball bounces off a surface, so the game is more complete.
- Settings screen: will allow players to adjust sound and colour scheme settings, so the application is more user-friendly.
- Selection of difficulty levels at the beginning: will make the game easier for beginners and less boring for expert players.
- Multiplayer support: players can compete against each other, to make it more similar to the original version.
- Increase ball speed as the game progresses: increases difficulty.
- Playing with multiple balls at once: increases difficulty.
- Allowing the paddle to be controlled with the mouse position: alternative controls will improve ease of use.
- Nickname and leaderboard features: this will make it more similar to an arcade game. Scores could be stored temporarily, or permanently in a database.

---

## Code Source
I have a little prior experience with PyGame, having made a 2D platformer and a drawing pad in the past. My understanding of the basic concepts meant that I was able to write all of the code for this Breakout game from scratch.

---
