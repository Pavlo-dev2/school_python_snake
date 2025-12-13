<h1 align="center">🐍 Ultrasnake</h1>

<p align="center">
  <b>A retro Snake-style arcade game built with Python and Pyxel</b>
</p>

<hr>

Ultrasnake is a classic Snake-style arcade game written in **Python** using the **Pyxel** retro game engine. The goal is to control the snake, eat apples, and survive as long as possible without hitting the walls or your own body.

The game includes different apple types that can speed up or slow down the snake, as well as multiple difficulty levels.

---

<h2>⚙️ Requirements</h2>

* Python **3.8+**
* Pyxel game engine

To install Pyxel(Windows):

```bash
pip install -U pyxel
```

---

<h2>▶️ How to Run the Game</h2>

1. Make sure both files are in the same folder:

   * `UltraSnake.py`
   * `UltraSnake.pyxres`

2. Open a terminal (Command Prompt / PowerShell / Linux terminal) in that folder.

3. Run the game with:

```bash
python3 UltraSnake.py ls
```

The game window will open automatically.

---

<h2>🎮 Controls</h2>

You can control the snake using either **WASD** or **Arrow keys**:

* **W / ↑** – Move up
* **D / →** – Move right
* **S / ↓** – Move down
* **A / ←** – Move left

The snake cannot instantly move in the opposite direction unless its length is 1.

---

<h2>🎚️ Choosing a Difficulty Level</h2>

Before the game starts, you must select a difficulty level:

* Press **1** – Level 1 (easy)
* Press **2** – Level 2
* Press **3** – Level 3
* Press **4** – Level 4
* Press **5** – Level 5 (hard)

Higher levels increase the game difficulty and affect apple behavior.

---

<h2>🕹️ Gameplay Rules</h2>

* Eat apples to grow longer and increase your score.
* The game ends if:

  * You hit the wall
  * You collide with your own body

### Apple Types

* **Pink apple** – Normal apple
* **Yellow apple** – Slows down the snake
* **Violet apple** – Speeds up the snake

Different apple types appear depending on the selected level.

---

<h2>🏆 Objective</h2>

Survive as long as possible and get the highest score by eating apples while managing your speed and avoiding collisions.

---

<h2>📝 Notes</h2>

* The game uses a grid of **16×16 pixel tiles**.
* Maximum number of apples on the field is limited.
* The game speed dynamically changes based on apple effects.

---

Have fun playing **Ultrasnake** 🐍
