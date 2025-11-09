import pyxel
import random
import time

pyxel.init(16*34, 16*25, title="Ultrasnake", fps = 100)
#pyxel.load("snake.pyxres")
#pyxel.load("game.pyxres", exclude_images=False, exclude_tilemaps=True, exclude_sounds=True, exclude_musics=True)
pyxel.load("snake2.pyxres", exclude_images=False)

maxapple = 10
level = 3#1-5
count = 0#count fps
score = 0
x = 330#10-320
y = 190#10-200
step = 1
speedstep = 5
snake = [[1, 20]]#snake len
apple = [[random.randint(2, 32), random.randint(2, 23), random.randint(1, 3)]]
dir = 0#0-3
speed = 30

def checksnake(snake):
    a = 0
    b = a
    while a < len(snake):
        b = a
        while b < len(snake):
            for i in snake[b+1:]:
                if snake[b] == i:
                    return True
            b += 1
        a += 1
    return False

def checkapple(apple, snake):
    for i in apple:
        if i[:2] in snake:
            apple.remove(i)
            return True
    return False

def createapple(snake):
    global apple, maxapple, level
    if len(apple) < maxapple and random.randint(1, 5) < level:
        avpos = list()
        ax = 1
        ay = 1
        while ay < 20:
            while ax < 33:
                if [ax, ay] not in snake:
                    avpos.append([ax, ay])
                ax += 1
            ax = 1
            ay += 1
        cp = avpos[random.randint(0, len(avpos)-1)]
        apple.append([cp[0], cp[1], random.randint(1, 3)])

def getdir(ad, snakelen):
    if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and (ad != 2 or snakelen == 1):
        return 0
    elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) and (ad != 3 or snakelen == 1):
        return 1
    elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) and (ad != 0 or snakelen == 1):
        return 2
    elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT) and (ad != 1 or snakelen == 1):
        return 3
    else:
        return ad

def movesnake(snake, dir, hta):
    snake.insert(0, [0, 0])
    if dir == 0:
        snake[0][0] = snake[1][0]
        snake[0][1] = snake[1][1]-step
    elif dir == 1:
        snake[0][0] = snake[1][0]+step
        snake[0][1] = snake[1][1]
    elif dir == 2:
        snake[0][0] = snake[1][0]
        snake[0][1] = snake[1][1]+step
    elif dir == 3:
        snake[0][0] = snake[1][0]-step
        snake[0][1] = snake[1][1]
    if hta == False:
        snake.pop()
    if snake [0][0] < 1 or snake[0][0] > 32 or snake[0][1] < 1 or snake[0][1] > 20:
        return 1

def update():
    global step, snake, dir, speed, count, score
    if count == speed:
        hta = checkapple(apple, snake)
        dir = getdir(dir, len(snake))
        if movesnake(snake, dir, hta) == 1 or checksnake(snake):
            print("You are dead")
            quit()
        createapple(snake)
        if hta:
            if speed > 20:
                speed -= speedstep
            score += 1
        count = -1
        #time.sleep(speed)
    
    #print(f"Snake: {snake}")
    print(f"Apple: {apple}")
    count += 1
    
def drawborder():
    a = 0
    b = 0
    while a < 34:
        pyxel.blt(a*16, 0, 0, 32, 16, 16, 16, colkey=0, rotate=0, scale=1)
        pyxel.blt(a*16, 21*16, 0, 32, 16, 16, 16, colkey=0, rotate=0, scale=1)
        a += 1
    while b < 22:
        pyxel.blt(0, b*16, 0, 32, 16, 16, 16, colkey=0, rotate=0, scale=1)
        pyxel.blt(33*16, b*16, 0, 32, 16, 16, 16, colkey=0, rotate=0, scale=1)
        b += 1

def drawinfo():
    global speed, score
    pyxel.rect(0, 22*16, 34*16, 3*16, 5)
    pyxel.text(16, 22*16, f"Score: {score}", 7)

def drawapple(apple):
    for i in apple:
        if i[2] == 1:
            pyxel.blt(i[0]*16, i[1]*16, 0, 16, 16, 16, 16, colkey=0, rotate=0, scale=1)#normal apple
        elif i[2] == 2:
            pyxel.blt(i[0]*16, i[1]*16, 0, 48, 16, 16, 16, colkey=0, rotate=0, scale=1)#good apple
        elif i[2] == 3:
            pyxel.blt(i[0]*16, i[1]*16, 0, 0, 32, 16, 16, colkey=0, rotate=0, scale=1)#bad apple
    
def draw():
    global snake, apple, dir
    pyxel.cls(0)
    #print(dir)
    #pyxel.blt(0, 0, 0, 0, 0, 16, 16, colkey=12, rotate=0, scale=1)
    
    drawinfo()
    drawborder()
    drawapple(apple)

    if dir == 0:
            pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 32, 0, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 1:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 16, 0, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 2:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 0, 16, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 3:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 48, 0, 16, 16, colkey=0, rotate=0, scale=1)
    
    for i in snake[1:]:
        pyxel.blt(i[0]*16, i[1]*16, 0, 0, 0, 16, 16, colkey=0, rotate=0, scale=1)
        #pyxel.rect(i[0]*10, i[1]*10, 10, 10, 11)

pyxel.run(update, draw)