#Part A/B
n = 101
count = 0
while n != 1:
  if (n % 2 == 0):
    n = n // 2
  else:
    n = (3 * n) + 1
  print(n)

  count += 1

print(count)


upper_limit = 20
iters = {}
for start in range(2, upper_limit + 1):
  count = 0
  while n != 1:
    if (n % 2 == 0):
      n = n // 2
    else:
      n = (3 * n) + 1
  
    count += 1
    iters = {n:count}
    print (iters)
  
  

