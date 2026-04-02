# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def isSameTree(p, q):
#     if not p and not q:
#         return True
#     if not p or not q:
#         return False
#     if p.val != q.val:
#         return False
#     return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if isSameTree(root,subRoot):
        #     return True
        # if not root:
        #     return False
        # return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        r = self.serialize(root)
        s = self.serialize(subRoot)
        return s in r
    def serialize(self,root):
        if not root:
            return "#"
        return str(root.val) + "|" + self.serialize(root.right) + "|" + self.serialize(root.left)

    