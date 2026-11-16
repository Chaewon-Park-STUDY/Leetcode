
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s=[0]*26
        count_t=[0]*26
        for elem in s:
            count_s[ord(elem)-97]+=1
        for elem in t:
            count_t[ord(elem)-97]+=1
        return count_s==count_t


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 정렬을 해서 anagram이면 정렬된 리스트의 원소가 동일
#         # 시간 복잡도: O(n log n) - 정렬, 공간 복잡도: O(n) - sorted로 list 생성
#         # 정렬 말고 다른 효율적 풀이가 있을까요?? 코멘트 많이 부탁드립니다~!!
#         return sorted(s) == sorted(t)


        