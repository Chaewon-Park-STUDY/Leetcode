class Solution:
    def numDecodings(self, s: str) -> int:
        # Time: O(n), Space: O(n):dp배열
        #dp[i] = i번째 글까지 해석하는 방법의 수
        # 계단 1칸, 2칸 오르는 것과 비슷
        k=len(s)
        dp=[0 for _ in range(k+1)]
        dp[0]=1
        for i in range(1,k+1):
            if int(s[i-1])!=0: #한자리
                dp[i]+=dp[i-1]
            if i>=2 and 10<=int(s[i-2:i])<27: #두자리
                dp[i]+=dp[i-2]
        return dp[-1]
                
            