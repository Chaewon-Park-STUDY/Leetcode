class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        k=len(nums)
        dp=[1 for _ in range(k)] # dp[i] = nums[i]로 끝나는 연속 수열의 길이
        for i in range(1,k):
            if nums[i]-nums[i-1]==1:
                dp[i]=dp[i-1]+1
            elif nums[i]==nums[i-1]:
                dp[i]=dp[i-1]
        return max(dp)