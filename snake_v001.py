import pyxel
import random
import time

pyxel.init(160, 200, title="Ultrasnake", fps = 100)

count = 0#count fps
score = 0
x = 150#0-150
y = 190#0-190
step = 1
speedstep = 5
snake = [[0, 19]]#snake len
apple = [[5, 5]]
dir = "u"
speed = 40

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
    return apple[0] == snake[0]

def createapple(snake):
    avpos = list()
    ax = 0
    ay = 0
    while ay < 19:
        while ax < 15:
            if [ay, ay] not in snake:
                avpos.append([ax, ay])
            ax += 1
        ax = 0
        ay += 1 
    apple[0] = avpos[random.randint(0, len(avpos)-1)]

def getdir(ad):
    if pyxel.btn(pyxel.KEY_W):
        return "u"
    elif pyxel.btn(pyxel.KEY_D):
        return "r"
    elif pyxel.btn(pyxel.KEY_S):
        return "d"
    elif pyxel.btn(pyxel.KEY_A):
        return "l"
    else:
        return ad

def movesnake(snake, dir, hta):
    snake.insert(0, [0, 0])
    if dir == "u":
        snake[0][0] = snake[1][0]
        snake[0][1] = snake[1][1]-step
    elif dir == "r":
        snake[0][0] = snake[1][0]+step
        snake[0][1] = snake[1][1]
    elif dir == "d":
        snake[0][0] = snake[1][0]
        snake[0][1] = snake[1][1]+step
    elif dir == "l":
        snake[0][0] = snake[1][0]-step
        snake[0][1] = snake[1][1]
    if hta == False:
        snake.pop()
    if snake [0][0] < 0 or snake[0][0] > 15 or snake[0][1] < 0 or snake[0][1] > 19:
        return 1

def update():
    global step, snake, dir, speed, count, score
    if count == speed:
        hta = checkapple(apple, snake)
        dir = getdir(dir)
        if movesnake(snake, dir, hta) == 1 or checksnake(snake):
            print("You are dead")
            quit()
        if hta:
            createapple(snake)
            if speed > 20:
                speed -= speedstep
            score += 1
        count = -1
        #time.sleep(speed)
    
    print(f"Snake: {snake}")
    print(f"Apple: {apple}")
    count += 1

def draw():
    global snake, apple
    pyxel.cls(0)
    pyxel.rect(apple[0][0]*10, apple[0][1]*10, 10, 10, 8)
    for i in snake:
        pyxel.rect(i[0]*10, i[1]*10, 10, 10, 11)

pyxel.run(update, draw)