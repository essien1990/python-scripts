import turtle

# square

nana = turtle.Turtle()
print('========================Turtle===============================')

def square():
    nana.forward(100)
    nana.right(90)
    nana.forward(100)
    nana.right(90)
    nana.forward(100)
    nana.right(90)
    nana.forward(100)


# square()
# nana.forward(100)
# square()

elephant_weight = 200
ant_weight = 0.1

if elephant_weight > ant_weight:
    square()
else:
    nana.forward(90)
