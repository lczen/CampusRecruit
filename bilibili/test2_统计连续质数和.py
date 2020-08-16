number = int(input())
def is_zhishu(num):
    if num == 2:
        return 1
    elif num == 0 or num == 1:
        return 0
    else:
        c = 0
        for i in range(2, num):
            if num % i == 0:
                c += 1
        if c > 1:
            return 0
        else:
            return 1

zhishus = [] # 存储所以质数
for i in range(2,number+1):
    if is_zhishu(i) == 1:
        zhishus.append(i)

count = 0
for j in range(len(zhishus)):
    total = 0
    begin = j
    while total < number and begin < len(zhishus):
        total += zhishus[begin]
        begin += 1
        if total == number:
            count += 1
print(count)
