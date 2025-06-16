ans = 0
for i in range(1, 100000001):
  le = len(str(i))
  print(i)
  print(le)
  if (le % 2) == 0:
    print("here")
    sum1 = 0
    sum2 = 0
    print(le)
    print(le/2)
    for j in range(le//2):
      ge = i % 10
      sum1 += ge
      i // 10
    for k in range(le//2):
      ge = i % 10
      sum2 += ge
      i // 10
    if sum1 == sum2:
      ans += 1
print(ans)
