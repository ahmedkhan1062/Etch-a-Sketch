from turtle import Turtle, Screen

turd = Turtle()
turd.color("red")
turd.shape("turtle")
sc = Screen()

def mForward():
    turd.forward(10)

def mBackward():
    turd.backward(10)

def mRight():
    turd.right(10)

def mLeft():
    turd.left(10)

def cClear():
    turd.reset()
    turd.color("red")


sc.listen()
sc.onkey(key= "w", fun=mForward)
sc.onkey(key= "s", fun=mBackward)
sc.onkey(key= "d", fun=mRight)
sc.onkey(key= "a", fun=mLeft)
sc.onkey(key= "c", fun=cClear)
sc.onkey(key= "Up", fun=turd.penup)
sc.onkey(key= "Down", fun=turd.pendown)
sc.exitonclick()


