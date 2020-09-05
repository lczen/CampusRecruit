# 求交集
T = int(input())
for _ in range(T):
    num_dict = {}
    n, m = map(int, input().split(" "))

    for i in range(1,n+1):
        num_dict[i] = 0

    for _ in range(m):
        k = int(input())
        for i in range(k):
            l, r = map(int, input().split(' '))
            for i in range(l, r+1):
                num_dict[i] += 1
    count = 0
    battle = ""
    for k, v in num_dict.items():
        if v >= m:
            count += 1

            battle += str(k)

    print(count)
    print(battle)