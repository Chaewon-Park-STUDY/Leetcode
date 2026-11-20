# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 중위순회
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        values=[]
        def tree(node):
            if node==None:
                return True
            tree(node.left)
            values.append(node.val)
            tree(node.right)
        tree(root)

        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        return True
        