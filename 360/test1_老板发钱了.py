n = 5

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for t in range(3, n+1):
    list2 = []
    for i in range(1, t+1):
        list2.append(dp[t - i])
    dp[t] = sum(list2)
print(dp)

'''
dp[3]

11 1
2  1

12

3
'''

# 0 1(两种) 2
'''
dp[4]

1111
121
211
31

112
22

13

4
'''