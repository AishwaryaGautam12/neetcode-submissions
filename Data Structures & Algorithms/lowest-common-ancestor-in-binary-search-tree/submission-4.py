# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST means root se chote left mai, bade right mai. so we check if p and q are bada or chota. if p and q chota search left warna search right and if p bada q chota (vice versa) then that is the LCA becuase usi node pe split hua hai. Time complexity = O(h-height) becuase we are not checking every node we are checking every level. Space = O(h) because of recursion stack
        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root