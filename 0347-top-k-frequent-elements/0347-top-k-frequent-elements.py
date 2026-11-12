class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        output=[]
        frequent={}
        for elem in nums:
            frequent[elem] = frequent.get(elem, 0) + 1
        result = dict(sorted(frequent.items(), key=lambda x: x[1], reverse=True))
        for key in result:
            output.append(key)
            if len(output)==k:
                break
        return output