# 7.3 Turtle Graphics
# I am going with H for honglin

# importing turtle, changing name, changing colors and pen size
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")
jim = turtle.Turtle()
jim.shape("turtle")
jim.color("red")
jim.pensize(17)

# bottom left H stem
jim.right(90)
jim.forward(80)
jim.right(90)
jim.forward(15)
jim.right(180)
jim.forward(15)
jim.right(90)

# moving up to top left H stem
jim.right(180)
jim.forward(160)
jim.left(90)
jim.forward(15)
jim.left(180)
jim.forward(15)
jim.right(90)
jim.forward(80)

# middle step with tail up near the end
jim.left(90)
jim.forward(50)
jim.penup()
jim.forward(30)
jim.pendown()
jim.left(90)

# top right stem
jim.forward(80)
jim.right(90)
jim.forward (15)
jim.right(180)
jim.forward(15)
jim.left(90)

# bottom right stem
jim.forward(160)
jim.left(90)
jim.forward(15)

# click to exit program
wn.exitonclick()