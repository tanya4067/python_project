from turtle import *
state={'turn':0}
#First thing is to create a fidget spinner
def spinner():
    clear()
    angle=state['turn']/10

    left(angle)
    forward(150)
    dot(200,"black")
    back(150)

    left(120)
    forward(150)
    dot(200,"black")
    back(150)

    left(120)
    forward(150)
    dot(200,"black")
    back(150)
    left(120)

def animate():
    if(state['turn']>0):
        state['turn']-=1

    spinner()
    ontimer(animate,20)

def flick():
    state['turn']+=40

def stop():
    print('HI');


bgcolor("pink")
tracer(False)

width(60)
color("white")
onkey(flick,'space')
onkey(stop,'A')
listen()
animate()
done()












