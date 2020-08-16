# 小强的矩阵
# 最多有多少个d表示
N, d = map(int, input().split())
B = [[0 for _ in range(N)] for _ in range(N)]
max_val = -1
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        B[i][j] = tmp[j]
        max_val = max(max_val, tmp[j])
count = 0
for i in range(N):
    for j in range(N):
        if B[i][j] == max_val:
            continue
        else:
            if (max_val - B[i][j]) % d != 0:
                print(-1)
                break
            else:
                count += (max_val - B[i][j]) / d
print(int(count))
