class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[0]*(n+1)
        def climb(n):
            if dp[n]!=0:
                return dp[n]
            if n<=2:
                dp[n]=n
            else:
                dp[n]=climb(n-1)+climb(n-2)
            return dp[n]
        return climb(n)


#풀이1) Time, Space: O(n),O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # dp로 접근
#         dp=[0]*(n+1)
#         for i in range(1,n+1):
#             if i==1:
#                 dp[i]=1
#             elif i==2:
#                 dp[i]=2
#             else:
#                 dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]


        