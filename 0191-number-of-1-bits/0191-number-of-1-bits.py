class Solution:
    def hammingWeight(self, n: int) -> int:
        num=0

        def bin(n):
            nonlocal num
            if n==0:
                return
            num+=n%2 
            n//=2
            
            bin(n)
            return num
        bin(n)
        return num

        