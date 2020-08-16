def knapsack(B, minutes, bonuses, n, m):
    for k in range(1, n+1):
        for C in range(1, m):
            if minutes[k] > C:
                B[k][C] = B[k-1][C]
            else:
                value1 = B[k-1][C-minutes[k]] + bonuses[k]
                value2 = B[k-1][C]
                if value1 > value2:
                    B[k][C] = value1
                else:
                    B[k][C] = value2
    return B
def main():
    n, m = map(int, input().split())
    if 0 < n <= 100 and 1 <= m <= 120:
        B = [[0 for _ in range(0, m)] for _ in range(0, n + 1)]
        minutes = [0]
        bonuses = [0]
        for _ in range(n):
            minute, bonus = map(int, input().split())
            if 1 <= minute <= 10 and 1 <= bonus <= 100:
                minutes.append(minute)
                bonuses.append(bonus)
            else:
                return False
        knapsack(B, minutes, bonuses, n, m)
        print(B[n][m-1])
    else:
        return False
if __name__ == "__main__":
    main()