import turtle
import time


scr=turtle.Screen()
scr.title("tictactoe")
scr.setup(600,600)
scr.bgcolor("black")
scr.tracer(0)
g=1
rw=0
gw=0


def game():
    global g
    global rw
    global gw


    pen=turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize("3")
    pen.color("white")
    pen.penup()
    c=["green","red"]

    ink=turtle.Turtle()
    ink.hideturtle()
    ink.speed(0)
    ink.penup()


    def plusmaker(x,y,a):
        for i in range(4):
            pen.goto(x, y)
            pen.pendown()
            pen.setheading(90*i)
            pen.fd(2*a)
            pen.penup()
    def gridmaker(a):
        plusmaker(a,a,a)
        plusmaker(-a,a,a)
        plusmaker(a, -a,a)
        plusmaker(-a, -a,a)



    def cross(x,y):
        for i in range(4):
            pen.goto(x,y)
            pen.pensize(2)
            pen.pendown()
            pen.setheading(45+90*i)
            if g%2==0:
                pen.pencolor(c[0])
            else:
                pen.pencolor(c[1])
            pen.fd(40)
            pen.penup()
    def circle(x,y):
        pen.goto(x-35/(2**(1/2)),y-35/(2**(1/2)))
        pen.pendown()
        if g % 2 == 0:
            pen.pencolor(c[1])
        else:
            pen.pencolor(c[0])
        pen.circle(35)
        pen.penup()
    a=[0,0,0,0,0,0,0,0,0]
    m=0
    for i in a:
        if i!=0:
            m=m+1

    def nw():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[0]==0:
            cross(-100,100)
            a[0]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[0]==0:
            circle(-100,100)
            a[0]=-1
            return
    def n():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[1]==0:
            cross(0,100)
            a[1]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[1]==0:
            circle(0,100)
            a[1]=-1
            return
    def ne():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[2]==0:
            cross(100,100)
            a[2]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[2]==0:
            circle(100,100)
            a[2]=-1
            return
    def w():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[3]==0:
            cross(-100,0)
            a[3]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[3]==0:
            circle(-100,0)
            a[3]=-1
            return
    def p():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[4]==0:
            cross(0,0)
            a[4]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[4]==0:
            circle(0,0)
            a[4]=-1
            return
    def e():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[5]==0:
            cross(100,0)
            a[5]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[5]==0:
            circle(100,0)
            a[5]=-1
            return
    def sw():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[6]==0:
            cross(-100,-100)
            a[6]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[6]==0:
            circle(-100,-100)
            a[6]=-1
            return
    def s():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[7]==0:
            cross(0,-100)
            a[7]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[7]==0:
            circle(0,-100)
            a[7]=-1
            return
    def se():
        if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]==0 and a[8]==0:
            cross(100,-100)
            a[8]=1
            return
        if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] != 0 and a[8]==0:
            circle(100,-100)
            a[8]=-1
            return
    #def ai(m):


    gridmaker(50)
    plusmaker(450, 50, 50)
    plusmaker(550, 50, 50)
    plusmaker(450, -50, 50)
    plusmaker(550, -50, 50)
    pen.goto(520, 200)
    pen.pendown()
    pen.write("use your num keys as given to move on the specific area ", font=("courier", 10, "bold"), align="center")
    pen.penup()
    pen.goto(400,50)
    pen.pendown()
    pen.write("7", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(500, 50)
    pen.pendown()
    pen.write("8", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(600, 50)
    pen.pendown()
    pen.write("9", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(400, -50)
    pen.pendown()
    pen.write("4", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(500, -50)
    pen.pendown()
    pen.write("5", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(600, -50)
    pen.pendown()
    pen.write("6", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(400, -150)
    pen.pendown()
    pen.write("1", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(500, -150)
    pen.pendown()
    pen.write("2", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(600, -150)
    pen.pendown()
    pen.write("3", font=("courier", 50, "bold"), align="center")
    pen.penup()
    pen.goto(-500, 50)
    pen.pendown()
    pen.write("this is a local multiplayer game", font=("courier", 15, "bold"), align="center")
    pen.penup()


    pen.goto(-500, 20)
    pen.pendown()
    pen.write("both players have to play", font = ("courier", 15, "bold"), align = "center")
    pen.penup()
    pen.goto(-500, -10)
    pen.pendown()
    pen.write("on the same computer and must wait", font=("courier", 15, "bold"), align="center")
    pen.penup()
    pen.goto(-500, -40)
    pen.pendown()
    pen.write("for the other player to play", font=("courier", 15, "bold"), align="center")
    pen.penup()
    pen.goto(-500, 250)
    pen.pendown()
    pen.write("HELP", font=("courier", 30, "bold"), align="center")
    pen.penup()
    pen.goto(-500, -70)
    pen.pendown()
    pen.write("LOOK AT THE RIGHT SIDE", font=("courier", 15, "bold"), align="center")
    pen.penup()
    pen.goto(480, -350)
    pen.pendown()
    pen.write("NOW PLEASE RETURN TO THE WINDOW SCREEN MODE", font=("courier", 15, "bold"), align="center")
    pen.penup()




    pen.goto(0,250)
    pen.pendown()
    pen.write("TIC TAC TOE", font=("courier",30,"bold") ,align="center")
    pen.penup()
    pen.goto(0,200)
    pen.pendown()
    pen.write("switch to full screen for help", font=("courier", 10, "bold"), align="center")
    pen.penup()
    gridmaker(50)



    turtle.listen()
    turtle.onkeypress(nw,"7")
    turtle.onkeypress(n,"8")
    turtle.onkeypress(ne,"9")
    turtle.onkeypress(w,"4")
    turtle.onkeypress(p,"5")
    turtle.onkeypress(e,"6")
    turtle.onkeypress(sw,"1")
    turtle.onkeypress(s,"2")
    turtle.onkeypress(se,"3")
    winner=" "


    while True:
        scr.update()

        if a[0]+a[1]+a[2]==3 or a[3]+a[4]+a[5]==3 or a[6]+a[7]+a[8]==3 or a[0]+a[3]+a[6]==3 or a[1]+a[4]+a[7]==3 or a[2]+a[5]+a[8]==3 or a[0]+a[4]+a[8]==3 or a[2]+a[4]+a[6]==3:
            print("cross wins")
            if g%2==0:
                gw=gw+1
                winner = c[0]
            else:
                rw=rw+1
                winner = c[1]

            print(a,g)
            break


        if a[0] + a[1] + a[2] == -3 or a[3] + a[4] + a[5] == -3 or a[6] + a[7] + a[8] == -3 or a[0] + a[3] + a[6] == -3 or a[1] + a[
            4] + a[7] == -3 or a[2] + a[5] + a[8] == -3 or a[0] + a[4] + a[8] == -3 or a[2] + a[4] + a[6] == -3:
            print("circle wins")
            if g%2==0:
                rw=rw+1
                winner = c[1]
            else:
                gw=gw+1
                winner = c[0]

            print(a,g)
            break


        if a[0]!=0 and a[1]!=0 and a[2]!=0 and a[3]!=0 and a[4]!=0 and a[5]!=0 and a[6]!=0 and a[7]!=0 and a[8]!=0:
            print("nobody wins")
            winner="nobody"
            print(a,g)
            break
        
        ink.goto(-200,150)
        ink.pendown()
        ink.pencolor(c[1])
        ink.write(" {} : {}  ".format(c[1],str(rw)), font=("courier", 15, "bold"), align="center")
        ink.penup()
        ink.goto(200, 150)
        ink.pendown()
        ink.pencolor(c[0])
        ink.write("{} : {}  ".format(c[0],str(gw)), font=("courier", 15, "bold"), align="center")
        ink.penup()
        ink.goto(0,200)
        


        


    pen.goto(0,-220)
    pen.pendown()
    pen.write("{} wins ".format(winner), font=("courier", 30, "bold"), align="center")
    pen.penup()
    pen.goto(0, -260)
    pen.pencolor(c[(g+1)%2])
    pen.pendown()
    pen.write("next move : {} ".format(c[(g+1)%2]), font=("courier", 30, "bold"), align="center")
    pen.penup()
    time.sleep(3)
    scr.clearscreen()
    scr.bgcolor("black")

    scr.tracer(0)

    g=g+1
    print(rw,gw)
    game()




game()




        
    
        
        
                    





