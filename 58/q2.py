# import math
# a, b = map(int, input().split(','))
#
# def test(A, B):
#     res = None
#     for i in range(1,501):
#         if int(math.sqrt(i+a)) == math.sqrt(i+a) and int(math.sqrt(i+b)) == math.sqrt(i+b):
#             res = i
#             break
#         else:
#             continue
#
#     return res
# a = test(a,b)
# print(a)
class Solution:
    def translateNum(self , num ):
        # write code here
        s = str(num)
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            temp = (s[i-1]-'0')*10 + s[i]-'0';
            if temp > 25:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[len(s)]
Solution().translateNum(12158)