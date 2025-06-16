import os
import sys
from itertools import accumulate

# 请在此输入您的代码
#标记c2的位置，遍历c1，利用前缀和处理有多少c2符合条件
k = int(input())
s,c1,c2 = input().split()
count2 = [0]*500010

for i in range(1, len(s)):
    if s[i] == c2:
        count2[i] = 1
    count2[i] += count2[i - 1]

ans = 0
for i in range(len(s)):
    if s[i] == c1:
        for j in range(i, len(s)):
            if s[j]==c2:
                if (j - i + 1) >= k:
                    ans += count2[len(s)-1]-count2[j-1]
                    break


print(ans)

