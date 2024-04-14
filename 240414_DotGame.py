#ボールをパッドに当てて跳ね返して色を変えるゲーム
import pyxel
import random
import math

pyxel.init(200, 200)

#一段目ｘ、ｙ、colorのリスト
circ1x_list = []
circ1y_list = []
circ1color_list = []
#2
circ2x_list = []
circ2y_list = []
circ2color_list = []
#3
circ3x_list = []
circ3y_list = []
circ3color_list = []
#4
circ4x_list = []
circ4y_list = []
circ4color_list = []
#5
circ5x_list = []
circ5y_list = []
circ5color_list = []
#6
circ6x_list = []
circ6y_list = []
circ6color_list = []
#7
circ7x_list = []
circ7y_list = []
circ7color_list = []
#8
circ8x_list = []
circ8y_list = []
circ8color_list = []
#9
circ9x_list = []
circ9y_list = []
circ9color_list = []
#10
circ10x_list = []
circ10y_list = []
circ10color_list = []

ball_color = 10 #ballの色
Y = 10


for i in range(10): #1段目の円
    for a in range(10,200,20):
      circ1x_list.append(a)
    circ1y_list.append(Y)
    circ1color_list.append(0)

for i in range(10): #2
    for a in range(10,200,20):
      circ2x_list.append(a)
    circ2y_list.append(Y-20)
    circ2color_list.append(0)

for i in range(10): #3
    for a in range(10,200,20):
      circ3x_list.append(a)
    circ3y_list.append(Y-40)
    circ3color_list.append(0)

for i in range(10): #4
    for a in range(10,200,20):
      circ4x_list.append(a)
    circ4y_list.append(Y-60)
    circ4color_list.append(0)

for i in range(10): #5
    for a in range(10,200,20):
      circ5x_list.append(a)
    circ5y_list.append(Y-80)
    circ5color_list.append(0)

for i in range(10): #6
    for a in range(10,200,20):
      circ6x_list.append(a)
    circ6y_list.append(Y-100)
    circ6color_list.append(0)

for i in range(10): #7
    for a in range(10,200,20):
      circ7x_list.append(a)
    circ7y_list.append(Y-120)
    circ7color_list.append(0)

for i in range(10): #8
    for a in range(10,200,20):
      circ8x_list.append(a)
    circ8y_list.append(Y-140)
    circ8color_list.append(0)

for i in range(10): #9
    for a in range(10,200,20):
      circ9x_list.append(a)
    circ9y_list.append(Y-160)
    circ9color_list.append(0)

for i in range(10): #10
    for a in range(10,200,20):
      circ10x_list.append(a)
    circ10y_list.append(Y-180)
    circ10color_list.append(0)


class Ball:#ballのクラス
    speed = 3

    def __init__(self):
      self.x = pyxel.mouse_x
      self.y = 185
      angle = math.radians(random.randint(30, 150))
      self.vx = -math.cos(angle)
      self.vy = math.sin(angle)
      self.touch = False
balls = [Ball()]



class Pad:#padのクラス
    def __init__(self):
      self.x = 100
pad = Pad()



def update():
    global touch, circ1x_list, circ1y_list, circ1color_list, ball_color,Y

    if pyxel.btnp(pyxel.KEY_A):#keyに色を対応させている
                ball_color = 8
    if pyxel.btnp(pyxel.KEY_S):
                ball_color = 9
    if pyxel.btnp(pyxel.KEY_D):
                ball_color = 10
    if pyxel.btnp(pyxel.KEY_F):
                ball_color = 11
    if pyxel.btnp(pyxel.KEY_G):
                ball_color = 12

    for ball in balls:
      ball.x += ball.vx * Ball.speed
      ball.y += ball.vy * Ball.speed
      if ball.x <= 0 or ball.x >= 200:
         ball.vx = -ball.vx

      if ball.y <= 20:
        ball.vy = -ball.vy

      if ball.y >= 190 and ball.x >= pad.x - 20 and ball.x <= pad.x + 20:

         ball.vy = -ball.vy
      if ball.y >= 200:
         ball.x = pyxel.mouse_x
         ball.y = 185
         angle = math.radians(random.randint(30, 150))
         ball.vx = -math.cos(angle)
         ball.vy = math.sin(angle)

    #当たったボールの色を変える
    if circ1y_list[i] == 10:#一段目
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ1color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
         circ1color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ1color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ1color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ1color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ1color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ1color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ1color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ1color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ1color_list[9] = ball_color

    if circ2y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ2color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ2color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ2color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ2color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ2color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ2color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ2color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ2color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ2color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ2color_list[9] = ball_color#2

    if circ3y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ3color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ3color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ3color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ3color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ3color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ3color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ3color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ3color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ3color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ3color_list[9] = ball_color#3

    if circ4y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ4color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ4color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ4color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ4color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ4color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ4color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ4color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ4color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ4color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ4color_list[9] = ball_color#4

    if circ5y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ5color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ5color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ5color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ5color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ5color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ5color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ5color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ5color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ5color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ5color_list[9] = ball_color#5

    if circ6y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ6color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ6color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ6color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ6color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ6color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ6color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ6color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ6color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ6color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ6color_list[9] = ball_color#6

    if circ7y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ7color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ7color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ7color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ7color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ7color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ7color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ7color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ7color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ7color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ7color_list[9] = ball_color#7

    if circ8y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ8color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ8color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ8color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ8color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ8olor_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ8color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ8color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ8color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ8color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ8color_list[9] = ball_color#8

    if circ9y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ9color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ9color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ9color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ9color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circc9olor_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ9color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ9color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ9color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ9color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ9color_list[9] = ball_color#9

    if circ10y_list[i] == 10:
      if ball.x > 0 and 20 > ball.x and ball.y <=20:
        circ10color_list[0] = ball_color
      if ball.x > 20 and 40 > ball.x and ball.y <=20:
        circ10color_list[1] = ball_color
      if ball.x > 40 and 60 > ball.x and ball.y <=20:
        circ10color_list[2] = ball_color
      if ball.x > 60 and 80 > ball.x and ball.y <=20:
        circ10color_list[3] = ball_color
      if ball.x > 80 and 100 > ball.x and ball.y <=20:
        circ10color_list[4] = ball_color
      if ball.x > 100 and 120 > ball.x and ball.y <=20:
        circ10color_list[5] = ball_color
      if ball.x > 120 and 140 > ball.x and ball.y <=20:
        circ10color_list[6] = ball_color
      if ball.x > 140 and 160 > ball.x and ball.y <=20:
        circ10color_list[7] = ball_color
      if ball.x > 160 and 180 > ball.x and ball.y <=20:
        circ10color_list[8] = ball_color
      if ball.x >  180and 200 > ball.x and ball.y <=20:
        circ10color_list[9] = ball_color#10

    pad.x = pyxel.mouse_x

    if pyxel.btnp(pyxel.KEY_SPACE):#SPACEを押すと段が下に下がる
        Y += 20
        for b in range(10):
            #Y += 20
            circ1y_list[b]= Y
            circ2y_list[b]= Y-20
            circ3y_list[b]= Y-40
            circ4y_list[b]= Y-60
            circ5y_list[b]= Y-80
            circ6y_list[b]= Y-100
            circ7y_list[b]= Y-120
            circ8y_list[b]= Y-140
            circ9y_list[b]= Y-160
            circ10y_list[b]= Y-180

    if pyxel.btnp(pyxel.KEY_Z):#Zを押すと段が上に上がる
        Y -= 20
        for b in range(10):
          circ1y_list[b]= Y
          circ2y_list[b]= Y-20
          circ3y_list[b]= Y-40
          circ4y_list[b]= Y-60
          circ5y_list[b]= Y-80
          circ6y_list[b]= Y-100
          circ7y_list[b]= Y-120
          circ8y_list[b]= Y-140
          circ9y_list[b]= Y-160
          circ10y_list[b]= Y-180
    if pyxel.btnp(pyxel.KEY_E):
        finish = True

def draw():
    global circ1x_list, circ1y_list, circ1color_list,ball_color

    pyxel.cls(0)
    for ball in balls:
      pyxel.circ(ball.x, ball.y, 10, ball_color)

    for i in range(10):
        pyxel.circ(circ1x_list[i], circ1y_list[i], 10, circ1color_list[i])
        pyxel.circ(circ2x_list[i], circ2y_list[i], 10, circ2color_list[i])
        pyxel.circ(circ3x_list[i], circ3y_list[i], 10, circ3color_list[i])
        pyxel.circ(circ4x_list[i], circ4y_list[i], 10, circ4color_list[i])
        pyxel.circ(circ5x_list[i], circ5y_list[i], 10, circ5color_list[i])
        pyxel.circ(circ6x_list[i], circ6y_list[i], 10, circ6color_list[i])
        pyxel.circ(circ7x_list[i], circ7y_list[i], 10, circ7color_list[i])
        pyxel.circ(circ8x_list[i], circ8y_list[i], 10, circ8color_list[i])
        pyxel.circ(circ9x_list[i], circ9y_list[i], 10, circ9color_list[i])
        pyxel.circ(circ10x_list[i], circ10y_list[i], 10, circ10color_list[i])

    pyxel.rect(pad.x - 20, 195, 40, 5, ball_color)

    pyxel.text(5, 5, 'A', 8)
    pyxel.text(10, 5, 'S', 9)
    pyxel.text(15, 5, 'D', 10)
    pyxel.text(20, 5, 'F', 11)
    pyxel.text(25, 5, 'G', 12)
    pyxel.text(5, 188, '  UP Z', 7)
    pyxel.text(5, 195, 'DOWN SPACE', 7)

pyxel.run(update, draw)
