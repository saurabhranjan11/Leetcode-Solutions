# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        q = deque()
        if root:
            q.append(root)
        else:
            return 0
        new = float('-inf')
        depth = 1
        while q:
            total = 0
            for i in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if new < total:
                new = total
                level = depth
            depth += 1
        return level