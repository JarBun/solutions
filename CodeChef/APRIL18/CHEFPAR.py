import random
from itertools import islice, count
from operator import mul
 
N, M, K = [int(x) for x in raw_input().split()]
numbers = [int(x) for x in raw_input().split()]
P = [int(x) for x in raw_input().split()]
 
red = lambda x: x + int(random.random()*K) + 1 
maximum, counts = 0, 0
while(counts < 350):
  
	current, prod, sigma = random.getstate(), reduce(mul, map(red, numbers)), 0
	for prime in P:
		sigma += prod%prime
 
	if sigma > maximum:
		maximum = sigma
		state = current
	counts += 1
 
random.setstate(state)
for i in range(N):
  print numbers[i] + (random.random()*K) + 1,
