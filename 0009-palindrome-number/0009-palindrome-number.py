class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        new=[]
        for elem in x:
            new.append(elem)
        if int(x)>=0:
            if new[::]== new[::-1]:
                return True
            else:
                return False
        else:
            return False

        