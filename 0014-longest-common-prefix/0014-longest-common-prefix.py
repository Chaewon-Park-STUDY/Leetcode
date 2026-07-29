class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        store=[]
        for i in range(len(strs[0])):
            if all(elem[:i+1]==strs[0][:i+1] for elem in strs):
                store.append(i)
        if len(store)>0 and len(strs)!=1:
            return f"{strs[0][:max(store)+1]}"
        elif len(strs)==1:
            return strs[0]
        else:
            return ""
        