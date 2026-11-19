class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer=set()
        nums.sort()
        k=len(nums)
        for i in range(k-2):
            candid=set()
            for j in range(i+1,k):
                target=-(nums[i]+nums[j])
                if target not in candid:
                    candid.add(nums[j])
                else:
                    answer.add(tuple((nums[i],nums[j],target)))
        return list(answer)








# 첫번째 풀이: TLE 
# brute force 방식
# 재귀  및 백트래킹 nums를 오름차순으로 정렬한 이유는 tuple은 (-1,-1,2) (2,-1,-1) 서로 다른 쌍으로 봐서
#Time:O(n^3) Space:O(n)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         answer=set()
#         k=len(nums)
#         nums.sort()

#         arr=[]

#         def dfs(start):
#             if len(arr)==3:
#                 if sum(arr)==0:
#                     answer.add(tuple(arr))
#                     return 
#                 return 
#             for i in range(start,k):
#                 arr.append(nums[i])
#                 dfs(i+1)
#                 arr.pop()
#         dfs(0)
#         return list(answer)

        