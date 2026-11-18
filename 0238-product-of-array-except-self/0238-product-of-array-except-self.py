class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        k = len(nums)
        # 아무것도 곱하지 않은 상태를 1에서 시작,
        # 첫번째 풀이와 달리 자기자신을 곱하지 않음
        # left[i]: i 왼쪽 원소들의 곱 / right[i]: i 오른쪽 원소들의 곱
        left = [1] * k
        right = [1] * k
        for i in range(1, k):
            left[i] = left[i - 1] * nums[i - 1]
            right[k - i - 1] = right[k - i] * nums[k - i]

        answer = []
        for i in range(k):
            answer.append(left[i] * right[i])
        return answer












# naive한 첫번째 풀이 

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         # 시간 복잡도 O(n) 이내에, 나눗셈 쓰지 말 것
#         # 누적 곱셈
#         # ex)1 [1,2,6,24] [24, 12   2*4, 6]
#         # [24,24,12,4]
#         # [-1,-1,0,0,0]
#         # [0,0,0,-9,3]
#         k=len(nums)
#         answer=[]
#         #양 끝 원소들과 아닌 원소들 처리 다르게 하기
#         left=[nums[0]]*k
#         right=[nums[-1]]*k
#         for i in range(1,k):
#             left[i]=left[i-1]*nums[i]
#             right[k-i-1]=right[k-i]*nums[k-i-1]

#         for i in range(k):
#             if i==0:
#                 answer.append(right[1])
#             elif i==k-1:
#                 answer.append(left[i-1])
#             else:
#                 answer.append(left[i-1]*right[i+1])
#         return answer
