SMALL = 0.000001

tests = int(input())

for i in range(tests):
  n, s, y = [int(x) for x in input().split()]
  V = [int(x) for x in input().split()]

  # -1 for left movement, 1 for right movement
  D = [(2*int(x) - 1) for x in input().split()]
  P = [int(x) for x in input().split()]
  C = [int(x) for x in input().split()]

  chefTime = 0

  for lane in range(n):
    time, leftover = y/s, C[lane] - abs(P[lane])
    movingAway = True if P[lane] * D[lane] >= 0 else False
    
    # if car on chef's path and moving away, let the car pass
    if leftover > 0 and movingAway:
      time += leftover/V[lane]
    
    # if car is far enough and moving towards chef
    elif not movingAway:
      carTime = abs(P[lane])/V[lane]
      distDiff = abs(P[lane]) - (V[lane] * time)
      
      if carTime < time:
        time += carTime + C[lane]/V[lane]
      
      elif distDiff < SMALL:
        time += time + (distDiff + C[lane])/V[lane]
    chefTime += time

    # update position
    if lane < n - 1:
      distance = V[lane + 1] * chefTime
      P[lane + 1] += D[lane + 1] * distance

  print("{:.6f}".format(chefTime))