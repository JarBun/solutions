workers = int(input())
coins = [int(x) for x in input().split()]
types = [int(x) for x in input().split()]

# find the cheapest type1, type2 and type3 workers
t1Min, t2Min, t3Min = 100000, 100000, 100000
for i in range(len(types)):
	if types[i] == 1 and coins[i] < t1Min: # translator
		t1Min = coins[i]
	elif types[i] == 2 and coins[i] < t2Min: # author
		t2Min = coins[i]
	elif types[i] == 3 and coins[i] < t3Min: # author-translator
		t3Min = coins[i]

print(min(t1Min + t2Min, t3Min))