import turtle as tu
import time

foo = tu.Turtle()

foo.left(90)
foo.speed(1000)

val = 45

theta = int(360/val)

def draw(l):

    if(l<10):

        return
        
    else:

        foo.forward(l)
        foo.left(20)
        draw(7 * l/11)
        foo.right(40)
        draw(7 * l/11)
        foo.left(20)
        foo.backward(l)


for i in range(theta):

    draw(100)
    foo.left(val)


time.sleep(30)