import pyxel

s = 0
speed = 1
score = 0
length = 0
pyxel.init(160, 200, title="Ultrasnake")
snake = list()
apples = list()
woals = list()

def update():
    global s
    if s == 0:
        snake.append([0, 0])
        s = 1
    if pyxel.btn(pyxel.KEY_W):
        

def draw():
    pyxel.cls(0)
    pyxel.rect(x, y, 8, 8, 11)

pyxel.run(update, draw)