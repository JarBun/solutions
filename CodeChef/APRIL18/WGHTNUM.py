MOD = 1000000007

for i in range(int(input())):
	N, W = [int(x) for x in input().split()]

	weights = {-9: 1, -8: 2, -7: 3, -6: 4, -5: 5, -4: 6, -3: 7,
	-2: 8, -1: 9, 0: 9, 1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

	print((weights.get(W, 0)*pow(10, N-2, MOD))%MOD)
