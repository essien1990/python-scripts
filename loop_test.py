import turtle

# square

sqr = turtle.Turtle()

print('========================For Loop===============================')


def square():
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)


for i in range(40):
    square()
