def star_pyramid():
  print("How many rows?")
  num_rows = int(input(":"))

  for i in range(1, num_rows + 1):
    print(i * ("*"))

def rstar_pyramid():
  print("How many rows?")
  num_rows = int(input(":"))
  for i in range(num_rows, 0, -1):
    print(i * "*")



star_pyramid()
rstar_pyramid()



