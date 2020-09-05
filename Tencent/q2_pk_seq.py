ans = []
def printAllSub(str, i, res):
    if i == len(str):
        ans.append(res)
        return
    else:
        printAllSub(str, i + 1, res); #不要下标为i + 1的字符
        printAllSub(str, i + 1, res + str[i]); #要第i + 1个字符

list_str = list(input())
k = int(input())
printAllSub(list_str, 0, "")
ans.remove("")
ans = list(set(ans))
ans.sort()
print(ans[k-1])