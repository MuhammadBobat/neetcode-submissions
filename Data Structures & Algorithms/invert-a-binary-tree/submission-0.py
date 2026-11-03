# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         # Base case: return None - leaf node does not swap with anything
         if root is None:
            return None

         # Step case: call function on left and right child, swap
         left = self.invertTree(root.left)
         right = self.invertTree(root.right)

         root.left, root.right = right, left

         return root