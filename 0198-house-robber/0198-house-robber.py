class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return sum(nums)
        elif len(nums)==2:
            return max(nums)
        dp=nums.copy()
        for i in range(2,len(nums)):
            if i!=2:
                dp[i]+=max(dp[i-3],dp[i-2])
            else:
                dp[i]+=dp[i-2]
        return max(dp)