from collections import defaultdict

for case in range(int(input())):
  N = int(input())
  A = [int(x) for x in input().split()]
  A.sort()
  
  table, hi, lo, pairs = defaultdict(int), A[-1], A[0], 0
  for elem in A:
    table[elem] += 1

  for elem in table:
    m = table[elem]
    pairs += m*(m-1)//2

    a, b = elem + 1, elem - 1
    while a <= hi and b >= lo:
      pairs += table.get(a, 0) * table.get(b, 0)
      a, b = a + 1, b - 1
  print(pairs)
