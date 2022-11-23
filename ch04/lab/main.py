import pygame
import random
import math

pygame.init()

window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

window_size_variable = pygame.display.get_window_size()

window.fill("blue")


pygame.draw.circle(window, "red", (window_size_variable[0]/2, window_size_variable[1]/2), 200)

pygame.display.flip()

x1 = 0
y1 = 200
start_pos = (x1, y1)

x2 = 400
y2 = 200
end_pos = (x2, y2)

pygame.draw.line(window, "black", start_pos, end_pos)

pygame.display.flip()

x3 = 200
y3 = 400
start_pos2 = (x3, y3)

x4 = 200
y4 = 0
end_pos2 = (x4, y4)

pygame.draw.line(window, "black", start_pos2, end_pos2)
pygame.display.flip()

#part B

for i in range (10):
  xcoord = random.randrange(0, window_width)
  ycoord = random.randrange(0, window_height)
  coords = (xcoord, ycoord)
  x = 200
  y = 200
  distance_from_center = math.hypot(xcoord-x, ycoord-y) #the distance formula
  is_in_circle = distance_from_center <= window_width/2 #screen width
  if is_in_circle == True:
    pygame.draw.circle(window, "green", coords, 4)
    pygame.display.flip()
    pygame.time.wait(1000)
  if is_in_circle == False:
    pygame.draw.circle(window, "purple", coords, 4)
    pygame.display.flip()
    pygame.time.wait(1000)
    
#PART C

color = "green"
window.fill(color)
pygame.display.flip()


playerChoice = ""
pygame.draw.rect(window, "red", (0, 10, 50, 50))
pygame.display.flip()


pygame.draw.rect(window, "blue", (350, 10, 50, 50 ))
pygame.display.flip()
pygame.time.wait(1000)


print("Select who will win: player red or player blue?")

pygame.time.wait(5000)

x = 200
y = 200
center = (x, y)
pygame.draw.circle(window, "yellow", center, 200)
pygame.display.flip()

pygame.draw.line(window, "black", start_pos, end_pos, 2)
pygame.display.flip()

pygame.draw.line(window, "black", start_pos2, end_pos2)
pygame.display.flip()

players = ["red", "blue"]
red_points = 0
blue_points = 0


for i in range (10):
  for player in players:
    xcoord = random.randrange(0, window_width)
    ycoord = random.randrange(0, window_height)
    coords = (xcoord, ycoord)
    x = 200
    y = 200
    distance_from_center = math.hypot(xcoord-x, ycoord-y) #the distance formula
    is_in_circle = distance_from_center <= window_width/2 #screen width
    if is_in_circle == True:
      pygame.draw.circle(window, player, coords, 4)
      pygame.display.flip()
      pygame.time.wait(1000)
      if player is players[0]:
          red_points += 1
      if player is players[1]:   
          blue_points += 1
    if is_in_circle == False:
      pygame.draw.circle(window, "purple", coords, 4)
      pygame.display.flip()
      pygame.time.wait(1000)
  if i == 9:
    if red_points > blue_points:
      winner = "red"
      print("Red wins.", "Score: ", red_points, "red to", blue_points , "blue")
    if red_points < blue_points:
      winner = "blue"
      print("Blue wins.", "Score: ", red_points, "red to", blue_points , "blue")
    if red_points == blue_points:
      winner = "no one"
      print("Tie." , "Score: " , red_points, "red to" , blue_points , "blue")

Guess = True
while Guess == True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < x/2:
        playerchoice = "red"
        Guess = False
      if event.pos[0] > x/2:
        playerchoice = "blue"
        Guess = False
print("You selected player", playerchoice)
pygame.display.flip()
pygame.time.wait(1000)

if winner is playerchoice:
  print("You're guess was correct!")
else:
  print("You're guess was wrong.")
pygame.time.wait(2500)


#window.exitonclick()