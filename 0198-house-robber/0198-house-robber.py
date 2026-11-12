class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return sum(nums)
        elif len(nums)==2:
            return max(nums)
        dp=nums.copy()
        for i in range(2,len(nums)):
            prev3 = dp[i-3] if i >= 3 else 0
            dp[i] += max(dp[i-2], prev3)
        return max(dp)