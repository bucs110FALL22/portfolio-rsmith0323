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
    pygame.time.wait(2500)
  if is_in_circle == False:
    pygame.draw.circle(window, "purple", coords, 4)
    pygame.display.flip()
    pygame.time.wait(2500)
  print(coords)
  
  
#PART C

window.fill("white")
pygame.draw.rect(window, "red", (50, 60, 100, 50))
pygame.display.flip()
pygame.time.wait(2500)

pygame.draw.rect(window, "blue", (50, 160, 100, 50 ))
pygame.display.flip()
pygame.time.wait(2500)




if event in pygame.event.get():
  if event.type == pygame. MOUSEBUTTONDOWN:
    if event.pos[0] < x / 2:
      

  















#window.exitonclick()