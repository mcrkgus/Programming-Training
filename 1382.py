# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def search(node):
	if node:
		search(node.left)
		my_node.append(node.val)
		search(node.right)

def sortedArrayToBST(arr): 
    if not arr: 
        return None
    mid = (len(arr)) // 2
    root = TreeNode(arr[mid]) 
    root.left = sortedArrayToBST(arr[:mid]) 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        global my_node
        my_node = []
        search(root)
        return sortedArrayToBST(my_node)