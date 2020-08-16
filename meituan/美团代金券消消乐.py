n = 5 # 使用双指针
value = [1,1,1,1,1] # 代金券的数量
res = 0 # 获取的奖励金
length = len(value)
flag = 0 # 哨兵，标志是否跳出循环
while True:
    flag = 0
    r = length - 1 # r：为右指针，l：为左指针
    l = r - 1
    while l > -1: # 只要l的值大于等于0，就一直循环
        if value[r] == value[l]: # r,l 所指的值相等时
            res += 1 # 获取的奖励金+1
            value[r] = -1 # 将合并后的右指针的值置为 -1,即设为无效值
            value[l] += 1 # 左指针更新为当前值+1
            flag = 1 # 此时数组更新，则flag的值也改变
        r -= 1
        l -= 1
    # 如果flag的值没有改变，即没有更新数组，则跳出循环
    if flag == 0:
        break
    # 重新整理数组，将所有可用的值往前整理，以便下次循环使用
    i, k = 0, 0
    for i in range(length):
        if value[i] == -1:
            k += 1
        else:
            value[i - k] = value[i]
    i += 1
    # 更新当前数组长度
    length = i - k
print(res)
