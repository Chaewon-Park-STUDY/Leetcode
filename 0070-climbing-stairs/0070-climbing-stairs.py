class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up DP
        # 사실상 피보나치 수열 
        # 시간 복잡도: O(n), 공간 복잡도: O(1)
        if n <= 2:
            return n
        first, second = 1, 2          # 1번째, 2번째 계단 오르는 방법수 
        for i in range(3, n + 1):
            first, second = second, first + second
        return second


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


        