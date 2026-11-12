class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        store=set()
        output=[]
        frequent={}
        for elem in nums:
            if elem not in store:
                store.add(elem)
                frequent[elem]=nums.count(elem)
        result = dict(sorted(frequent.items(), key=lambda x: x[1], reverse=True))

        for key in result:
            output.append(key)
            if len(output)==k:
                break
        return output