import pyxel
import random
import time

pyxel.init(16*34, 16*22, title="Ultrasnake", fps = 100)
#pyxel.load("snake.pyxres")
#pyxel.load("game.pyxres", exclude_images=False, exclude_tilemaps=True, exclude_sounds=True, exclude_musics=True)
pyxel.load("UltraSnake.pyxres", exclude_images=False)
#pyxel.images[0].load(0, 0, "assets/pyxel_logo_38x16.png")


#check if snake dont hit itselve
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

#check if snake hit apple
def checkapple(apple, snake):
    global slow, fast, plusspeed
    for i in apple:
        if i[:2] in snake:
            if i[2] == 2:
                plusspeed += level#slower
                slow += 5
            elif i[2] == 3:
                plusspeed -= level#faster
                fast += 5 
            apple.remove(i)#delate old apple
            return True
    return False

def createapple(snake):
    global apple, maxapple, level
    if (len(apple) < maxapple and random.randint(1, 5) < level) or len(apple) == 0:
        avpos = list()
        ax = 1
        ay = 1
        while ay < 21:
            while ax < 33:
                if [ax, ay] not in snake and [ax, ay] not in apple:#if the possion is availible
                    avpos.append([ax, ay])
                ax += 1
            ax = 1
            ay += 1
        cp = avpos[random.randint(0, len(avpos)-1)]#selekt randome possion
        appletype = random.randint(1, 5)#selekt randome apple type
        if appletype > level:
            appletype = 2
        elif appletype < level:
            appletype = 3
        #appletype = 2
        ta = [1, appletype]
        apple.append([cp[0], cp[1], ta[random.randint(0, 1)]])

#get direction
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

#move snake
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

#draw box borders
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

#draw apple
def drawapple(apple):
    for i in apple:
        if i[2] == 1:#pink
            pyxel.blt(i[0]*16, i[1]*16, 0, 16, 16, 16, 16, colkey=0, rotate=0, scale=1)#normal apple
        elif i[2] == 2:#yellow
            pyxel.blt(i[0]*16, i[1]*16, 0, 48, 16, 16, 16, colkey=0, rotate=0, scale=1)#good apple
        elif i[2] == 3:#violet
            pyxel.blt(i[0]*16, i[1]*16, 0, 0, 32, 16, 16, colkey=0, rotate=0, scale=1)#bad apple

#selekt level            
def chouselevel():
    if pyxel.btn(pyxel.KEY_1):
        return 1
    elif pyxel.btn(pyxel.KEY_2):
        return 2
    elif pyxel.btn(pyxel.KEY_3):
        return 3
    elif pyxel.btn(pyxel.KEY_4):
        return 4
    elif pyxel.btn(pyxel.KEY_5):
        return 5
    return 0

#draw snake
def drawsnake(dir, snake):
    #draw head
    if dir == 0:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 32, 0, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 1:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 16, 0, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 2:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 0, 16, 16, 16, colkey=0, rotate=0, scale=1)
    elif dir == 3:
        pyxel.blt(snake[0][0]*16, snake[0][1]*16, 0, 48, 0, 16, 16, colkey=0, rotate=0, scale=1)
    
    #draw the rest of the boady
    for i in snake[1:]:
        pyxel.blt(i[0]*16, i[1]*16, 0, 0, 0, 16, 16, colkey=0, rotate=0, scale=1)

def update():
    global step, snake, dir, speed, count, score, slow, fast, plusspeed, level
    #chouse level before game start
    if level == 0:  
        level = chouselevel()
        return 0
    if count == max((speed + plusspeed), 5):
        hta = checkapple(apple, snake)#check if hit apple
        dir = getdir(dir, len(snake))#get actual ditection
        if movesnake(snake, dir, hta) == 1 or checksnake(snake):#move snake forvard and check snake
            print("You are dead")
            quit()
        createapple(snake)#create new apple
        if hta:#make speed normal
            if speed > 10:
                speed -= speedstep
            score += 1
        if slow > 0:
            slow -= 1
        if fast > 0:
            fast -= 1
        if slow == 0 and fast == 0:
            plusspeed = 0
        count = -1
    
    count += 1

def draw():
    global snake, apple, dir, level
    pyxel.cls(0)
    if level == 0:
        pyxel.blt(14*16, 8*16, 0, 16, 32, 6*16, 3*16, colkey=0, rotate=0, scale=1)
        return 0

    drawborder()
    drawapple(apple)
    drawsnake(dir, snake)

maxapple = 15#maximal number of apples
slow = 0#turns left with slow speed
fast = 0#turns left with fast speed
level = 0#1-5
count = 0#count fps
score = 0
x = 330#10-320
y = 190#10-200
step = 1
speedstep = 5
snake = [[1, 20]]#snake cords list
apple = [[random.randint(2, 32), random.randint(2, 21), random.randint(1, 3)]]#apple cords list
dir = 0#0-3
speed = 50
plusspeed = 0

pyxel.run(update, draw)