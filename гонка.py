
import turtle
import time
turtle.Screen().listen()
import random


road = turtle.Turtle()
turtle.Screen().addshape('pics/RoadTile/01/1.gif')
road.shape('pics/RoadTile/01/1.gif')
road.stamp()

r = 0
te = turtle.Screen().setup(800, 800)
turtle.Screen().colormode(255)
t5 = turtle.Turtle()
z=random.randint(1,16)
x=random.randint(1,16)
y=random.randint(1,16)
z2=random.randint(1,16)
x2=random.randint(17 ,20)
m=random.randint(-700,700)
z1 = random.randint(1, 255)
x1 = random.randint(1, 255)
y1 = random.randint(1, 255)
t5.penup()
t5.setpos(m,-40)
t5.pendown()
t5.speed(0)
t5.pencolor((x1, y1, z1))
for i in range(10):
    t5.forward(i)
    t5.right(127)
def f() :
    #global r
    #x,_=t.pos()
    t.forward(x2)
    #x1,_=t.pos()
    #for i in range(int(x),int(x1)+1):
        #if i==m:
            #r=1
def v() :
    t.forward(2)
t =turtle.Turtle()
turtle.Screen().addshape('pics/Motorcycle Body/1.gif')
t.shape('pics/Motorcycle Body/1.gif')

t.penup()
t1=turtle.Turtle()
turtle.Screen().addshape('pics/Motorcycle Body/2.gif')
t1.shape('pics/Motorcycle Body/2.gif')

t1.penup()
t2=turtle.Turtle()
turtle.Screen().addshape('pics/Motorcycle Body/3.gif')
t2.shape('pics/Motorcycle Body/3.gif')
t2.penup()
t3=turtle.Turtle()
turtle.Screen().addshape('pics/Motorcycle Body/4.gif')
t3.shape('pics/Motorcycle Body/4.gif')
t.penup()
t3.penup()
t4=turtle.Turtle()
turtle.Screen().addshape('pics/Motorcycle Body/5.gif')
t4.shape('pics/Motorcycle Body/5.gif')

t4.penup()
turtle.Screen().onkey(f, "Right")
turtle.Screen().onkey(v, "Up")
t.left(180)
t1.left(180)
t2.left(180)
t3.left(180)
t4.left(180)
t.forward(800)
t1.forward(800)
t2.forward(800)
t3.forward(800)
t4.forward(800)
t.left(180)
t1.left(180)
t2.left(180)
t3.left(180)
t4.left(180)
t.left(90)
t1.left(90)
t2.right(90)
t3.right(90)
t.forward(200)
t1.forward(100)
t2.forward(200)
t3.forward(100)
t.right(90)
t1.right(90)
t2.left(90)
t3.left(90)
time.sleep(5)
while True:
    t1.forward(x)
    t2.forward(y)
    t3.forward(z)
    t4.forward(z2)
    time.sleep(0.1)
    #if r==1:
        #break
#print("вы проиграли")
