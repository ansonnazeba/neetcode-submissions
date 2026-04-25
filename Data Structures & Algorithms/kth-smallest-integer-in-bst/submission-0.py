# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h1 = []

        h1 = self.buildingList(root, h1)
        return h1[k - 1]

    def buildingList(self, root: Optional[TreeNode], listIn:[]) -> []:
        if not root:
            return listIn
        
        self.buildingList(root.left, listIn)
        listIn.append(root.val)
        self.buildingList(root.right, listIn)

        return listIn

        