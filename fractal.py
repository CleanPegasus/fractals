import turtle as tu
import time

foo = tu.Turtle()

foo.left(90)
foo.speed(1000)

val = 60

theta = int(360/val)

def draw(l):

    if(l<10):

        return
        
    else:

        foo.forward(l)
        foo.left(30)
        draw(3 * l/4)
        foo.right(60)
        draw(3 * l/4)
        foo.left(30)
        foo.backward(l)


for i in range(theta):

    draw(100)
    foo.left(val)


time.sleep(30)