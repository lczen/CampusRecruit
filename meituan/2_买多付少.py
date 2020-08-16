n = int(input())
x = []
y = []
for i in range(n):
    string = input()
    x.append(int(string.split(" ")[0]))
    y.append(int(string.split(" ")[1]))
value = 0 # value代表总金额
count = 0 # count代表代金券的金额
sum = 0 # sum代表实际支付金额
for i in range(n):
    if x[i] < y[i]:
        value += y[i]
        count += y[i]
        continue
    value += x[i]
    count += y[i]
sum = value - count
print(str(value)+' '+str(sum))
