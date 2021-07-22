for i in range(1):
    import turtle
    import time
    turtle.Screen().listen()
    import random
    r = 0
    te = turtle.Screen().setup(800, 800)
    turtle.Screen().colormode(255)
    t5 = turtle.Turtle()
    t5.setpos(-900, 0)
    t5.forward(1800)
    t5.penup()
    t5.setpos(0, -500)
    t5.pendown()
    t5.left(90)
    t5.forward(1000)
    z = random.randint(4, 100)
    z1 = random.randint(1, 255)
    x1 = random.randint(1, 255)
    y1 = random.randint(1, 255)
    t5.penup()
    t5.setpos(100,-40)
    t5.pendown()
    t5.speed(0)
    t5.pencolor((x1, y1, z1))
    for i in range(10):
        t5.forward(i)
        t5.right(127)
    def f() :
        global r
        x,_=t.pos()
        t.forward(19)
        x1,_=t.pos()
        for i in range(int(x),int(x1)+1):
            if i==100:
                r=1
        time.sleep(0.1)
    def v() :
        t.forward(2)
    t =turtle.Turtle()
    t1=turtle.Turtle()
    t2=turtle.Turtle()
    t3=turtle.Turtle()
    t4=turtle.Turtle()
    turtle.Screen().onkey(f, "Right")
    turtle.Screen().onkey(v, "Up")
    t.right(90)
    t1.right(90)
    t2.right(90)
    t3.right(90)
    t.forward(40)
    t1.forward(30)
    t2.forward(20)
    t3.forward(10)
    t.left(90)
    t1.left(90)
    t2.left(90)
    t3.left(90)
    time.sleep(5)
    while True:
        t1.forward(2)
        t2.forward(4)
        t3.forward(8)
        t4.forward(16)
        time.sleep(0.1)
        if r==1:
            break
print("вы проиграли")