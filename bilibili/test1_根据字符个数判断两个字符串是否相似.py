
def test():

    a = input()
    b = input()
    # 判断边际条件
    if len(a)>=1000 or len(a) <=0 or len(b)>=1000 or len(b) <= 0:
        return 0

    if len(a) != len(b):
        return 0
    ca = list(a)
    cb = list(b)
    count = {}

    for i in ca:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for j in cb:
        if j not in count: # 如果有不同的元素，则
            return 0
        else:
            count[j] -= 1

    for k,v in count.items():
        if v != 0:
            return 0
        return 1
if __name__ == '__main__':
    print(test())

