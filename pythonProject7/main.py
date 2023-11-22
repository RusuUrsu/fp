import turtle
import json
import os


def move_pen(pen,x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

def A(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(65)
    p.forward(40)
    p.right(130)
    p.forward(40)
    p.left(180)
    p.forward(20)
    p.left(65)
    p.forward(20)
    p.hideturtle()


def B(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(90)
    p.forward(12)
    p.circle(-8,180)
    p.left(180)
    p.circle(-11,180)
    p.forward(15)
    p.hideturtle()

def C(x,y):
    p=turtle.Pen()
    move_pen(p,x+20,y)
    p.circle(18,-190)
    p.hideturtle()

def D(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(90)
    p.circle(-18,180)
    p.hideturtle()

def E(x,y):
    p=turtle.Pen()
    move_pen(p,x+20,y)
    p.left(180)
    p.forward(20)
    p.right(90)
    p.forward(36)
    p.right(90)
    p.forward(20)
    p.left(180)
    move_pen(p,p.xcor(),p.ycor()-18)
    p.forward(20)
    p.hideturtle()


def F(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(90)
    p.forward(20)
    p.left(180)
    move_pen(p,p.xcor(),p.ycor()-15)
    p.forward(20)
    p.hideturtle()

def G(x,y):
    p = turtle.Pen()
    p2=turtle.Pen()
    move_pen(p2,x+20,y)
    move_pen(p, x + 20, y)
    p.circle(18, -210)
    p2.circle(18,90)
    p2.left(90)
    p2.forward(20)
    p.hideturtle()
    p2.hideturtle()


def H(x,y):
    p=turtle.Pen()
    p2=turtle.Pen()
    p.left(90)
    p2.left(90)
    move_pen(p,x,y)
    move_pen(p2,x+20,y)
    p.forward(36)
    p2.forward(36)
    move_pen(p,p.xcor(),p.ycor()-18)
    p.right(90)
    p.forward(20)
    p.hideturtle()
    p2.hideturtle()


def I(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.hideturtle()

def J(x,y):
    p=turtle.Pen()
    move_pen(p,x,y+10)
    p.right(90)
    p.circle(10,180)
    p.forward(26)
    p.hideturtle()

def K(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p2=turtle.Pen()
    move_pen(p2,p.xcor(),p.ycor()-18)
    move_pen(p,p.xcor(),p.ycor()-18)
    p.right(25)
    p2.right(55)
    p.forward(21)
    p2.forward(23)
    p.hideturtle()
    p2.hideturtle()

def L(x,y):
    p=turtle.Pen()
    move_pen(p,x,y+36)
    p.right(90)
    p.forward(36)
    p.left(90)
    p.forward(20)
    p.hideturtle()


def M(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(135)
    p.forward(20)
    p.left(90)
    p.forward(20)
    p.right(135)
    p.forward(36)
    p.hideturtle()

def N(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(150)
    p.forward(40)
    p.left(150)
    p.forward(36)
    p.hideturtle()

def O(x,y):
    p=turtle.Pen()
    move_pen(p,x+18,y)
    p.circle(18)
    p.hideturtle()

def P(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(90)
    p.forward(36)
    p.right(90)
    p.circle(-12,180)
    p.hideturtle()

def Q(x,y):
    p = turtle.Pen()
    move_pen(p, x + 18, y)
    p.circle(18)
    p.right(45)
    move_pen(p,p.xcor()+5,p.ycor()+11)
    p.forward(17)
    p.hideturtle()


def R(x,y):
    p = turtle.Pen()
    move_pen(p, x, y)
    p.left(90)
    p.forward(36)
    p.right(90)
    p.circle(-12, 180)
    p.left(135)
    p.forward(20)
    p.hideturtle()

def S(x,y):
    p=turtle.Pen()
    move_pen(p,x,y+10)
    p.right(90)
    p.circle(9,230)
    p.forward(15)
    p.circle(-9,230)
    p.hideturtle()

def T(x,y):
    p=turtle.Pen()
    move_pen(p,x+13,y)
    p.left(90)
    p.forward(36)
    p.left(90)
    p.forward(13)
    p.left(180)
    p.forward(26)
    p.hideturtle()

def U(x,y):
    p=turtle.Pen()
    move_pen(p,x,y+36)
    p.right(90)
    p.forward(26)
    p.circle(10,180)
    p.forward(26)
    p.hideturtle()

def V(x,y):
    p=turtle.Pen()
    p2=turtle.Pen()
    move_pen(p,x+15,y)
    move_pen(p2,x+15,y)
    p.left(115)
    p2.left(65)
    p.forward(40)
    p2.forward(40)
    p.hideturtle()
    p2.hideturtle()

def W(x,y):
    p = turtle.Pen()
    p2 = turtle.Pen()
    move_pen(p, x + 15, y)
    move_pen(p2, x + 15, y)
    p.left(110)
    p2.left(75)
    p.forward(38)
    p2.forward(18)
    p2.right(150)#130
    p2.forward(18)
    p2.left(145)
    p2.forward(38)
    p.hideturtle()
    p2.hideturtle()


def X(x,y):
    p=turtle.Pen()
    p2=turtle.Pen()
    move_pen(p,x,y)
    move_pen(p2,x+20,y)
    p.left(65)
    p.forward(40)
    p2.left(115)
    p2.forward(40)
    p.hideturtle()
    p2.hideturtle()

def Y(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.left(65)
    p.forward(40)
    move_pen(p,p.xcor()-9,p.ycor()-15)
    p.left(60)
    p.forward(18)
    p.hideturtle()

def Z(x,y):
    p=turtle.Pen()
    move_pen(p,x+20,y)
    p.left(180)
    p.forward(20)
    p.right(120)
    p.forward(40)
    p.left(120)
    p.forward(20)
    p.hideturtle()


def punkt(x,y):
    p=turtle.Pen()
    move_pen(p,x,y)
    p.circle(2)
    p.hideturtle()

def excl(x,y):
    p = turtle.Pen()
    move_pen(p, x, y)
    p.circle(2)
    move_pen(p,x,y+8)
    p.left(90)
    p.forward(30)
    p.hideturtle()

def intre(x,y):
    p = turtle.Pen()
    move_pen(p, x, y)
    p.circle(2)
    move_pen(p, x, y + 8)
    p.left(90)
    p.forward(16)
    p.right(80)
    p.circle(11,240)
    p.hideturtle()


def on_W_key():
    turtle.forward(10)
    drawn_keys.append('W')


def on_S_key():
    turtle.back(10)
    drawn_keys.append('S')


def on_A_key():
    turtle.left(45)
    drawn_keys.append('A')


def on_D_key():
    turtle.right(45)
    drawn_keys.append('D')


def on_F_key():
    turtle.penup()
    drawn_keys.append('F')


def on_G_key():
    turtle.pendown()
    drawn_keys.append('G')



def on_Enter_key():
    turtle.clear()
    turtle.hideturtle()
    aux={}
    if ch not in user_signs.keys():#schreibt in einer Datei der benutzerdefinierte Worterbuch
        aux[ch]=drawn_keys
        with open('user_defined.txt', 'a') as cnv_f:
            cnv_f.write(json.dumps(aux)+"\n")
    exit()



def draw(x, y, keys):
    p = turtle.Pen()
    move_pen(p, x, y)
    for key in keys:
        if key == 'W':
            p.forward(10)
        elif key == 'S':
            p.back(10)
        elif key == 'A':
            p.left(45)
        elif key == 'D':
            p.right(45)
        elif key == 'F':
            p.penup()
        elif key == 'G':
            p.pendown()
    p.hideturtle()

def draw_custom_character():
    turtle.showturtle()
    turtle.listen()
    turtle.onkey(on_W_key, 'w')
    turtle.onkey(on_S_key, 's')
    turtle.onkey(on_A_key, 'a')
    turtle.onkey(on_D_key, 'd')
    turtle.onkey(on_F_key,'f')
    turtle.onkey(on_G_key,'g')
    turtle.onkey(on_Enter_key,'Return')
    turtle.mainloop()


drawn_keys = []

alphabet = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M,
                'N': N, 'O': O, 'P': P, 'Q': Q,
                'R': R, 'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z, '.': punkt, '!':excl, '?':intre}
user_signs={}

x, y = -350, 270
def main():
    global x,y
    if os.stat("written_words.txt").st_size>0:
        with open('written_words.txt', 'r') as fl:
            lns=fl.readlines()

    if os.stat("user_defined.txt").st_size > 0:
        with open('user_defined.txt', 'r') as file:
            lines=file.readlines()
        aux={}
        for line in lines:
            aux=json.loads(line)
            user_signs.update(aux)

    if os.stat("written_words.txt").st_size > 0:
        for l in lns:
            l_ch = list(l)
            for i in l_ch:
                if i in alphabet.keys():
                    alphabet[i](x, y)
                elif i in user_signs.keys():
                    draw(x, y, user_signs[i])

                if x > 350:
                    x = -350
                    y -= 50
                else:
                    x += 40
            x = -350
            y -= 50
    n = input("""
                    0 -> Exit
                    1 -> Draw String
                    2 -> Add Charachter
                """)
    if n=='0':
        exit()
    elif n == '1':
        chr = input("Enter String: ")
        chr=chr.upper()
        with open('written_words.txt', 'a') as file1:#speichert die Worter in einer Datei
            file1.write(chr+"\n")
        word = list(chr)

        for i in word:
            if i in alphabet.keys():
                alphabet[i](x, y)
            elif i in user_signs.keys():
                draw(x, y, user_signs[i])

            if x > 350:
                x = -350
                y -= 50
            else:
                x += 40
    elif n == '2':
        global ch
        while True:
            ch= input()
            if ch not in alphabet and ch not in user_signs:
                drawn_keys.clear()
                draw_custom_character()
                break
            else:
                print("Is in dictionary, try an other")
    turtle.mainloop()

main()