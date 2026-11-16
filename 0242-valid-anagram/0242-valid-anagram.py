class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #정렬을 해서 anagram이면 정렬된 리스트의 원소가 동일
        #시간 복잡도: O(n log n)  공간 복잡도: O(n)
        #시간 복잡도: 정렬, 공간 복잡도: sorted로 list 생성

        #정렬 말고 다른 효율적 풀이가 있을까요??
        # 코멘트 많이 부탁드립니다~!!
        