class Solution:
    def numDecodings(self, s: str) -> int:
        k=len(s)
        dp=[0 for _ in range(k+1)]
        dp[0]=1
        for i in range(1,k+1):
            if int(s[i-1])!=0:
                dp[i]+=dp[i-1]
            if i>=2 and 10<=int(s[i-2:i])<27:
                dp[i]+=dp[i-2]
        return dp[-1]
                
            