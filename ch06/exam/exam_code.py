import turtle
import time

window = turtle.Screen() 
window.bgcolor('darkviolet')

turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.color('white')

def star_1(angle_1, side_length, angle_2):
  turtle.right(angle_1)
  turtle.forward(side_length)
  
  for i in range (4):
    turtle.right(angle_2)
    turtle.forward(side_length)

  is_star = True
  return is_star
  
def star_2(angle_1, angle_3, side_length, angle_2):
  turtle.right(angle_1)
  turtle.penup()
  turtle.forward(30)
  turtle.right(angle_3)
  turtle.pendown()
  turtle.forward(side_length)

  for i in range (4):
    turtle.right(angle_2)
    turtle.forward(side_length)



star_1(72, 100, 144)
star_2(72, 108, 100, 144)

time.sleep(5)

window.exitonclick()