class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        k=len(nums)
        prev=nums[0]
        max_val=prev
        for i in range(1,k):
            if nums[i]>=prev+nums[i]:
                prev=nums[i]
            else:
                prev+=nums[i]
            max_val = max(max_val, prev)
        return max_val
    


        