import turtle



def drawEqshape():
  turtle = turtle.Turtle()
  window = turtle.Screen()
  turtle.shape("turtle")
  turtle.color("green")
  for i in range(0, num_sides):
    turtle.forward(side_length)
    turtle.left(360/num_sides)

num_sides = int(input("How many sides? "))
side_length = int(input("What is the side length? "))




drawEqshape()
  