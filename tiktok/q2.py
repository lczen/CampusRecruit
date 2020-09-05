def sub(arr):
 finish=[]
 size = len(arr)
 end = 1 << size #end=2**size
 for index in range(end): # shift index
  array = []
  for j in range(size):
   # 00,01,10,11 is symmetrical
   if (index >> j) % 2: # this result is 1, so do not have to write ==
    array.append(arr[j])
  # print(array)
  finish.append(array)
 return finish

def anyway(arr):
    for item in arr:
        if len(item) == 0 or len(item) == 1:
            ans.append(0)
            list2.append(item)
        elif len(item) == 2:
            if (item[0]+item[1])% k != 0:
                ans.append(0)
                list2.append(item)
        else:
            tag = 0
            for i in range(0,len(item)-1):
                for j in range(i+1,len(item)):
                    if (item[i] + item[j]) % k == 0:
                        tag = 1
            if tag == 0:
                ans.append(0)
                list2.append(item)
    return len(ans)

#arr = []
n, k = map(int, input().split())

if 0< n <=100000 and 0 <k<= 1000:
    arr = list(map(int, input().split()))

    if min(arr)>0 and max(arr)<= 100000:
        arr2 = sub(arr)

        list2 = []
        ans = []
        print(anyway(arr2))

print(list2)