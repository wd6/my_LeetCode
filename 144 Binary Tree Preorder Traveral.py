# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    '''
        def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        preorder = list()
        def rec(node):
        if node:
        preorder.append(node.val)
        rec(node.left)
        rec(node.right)
        return preorder
        rec(root)
        return preorder
        '''
    '''
        def preorderTraversal(self, root: 'TreeNode'):
        stack, preorder = [root], []
        while stack:
        node = stack.pop()
        if node:
        preorder.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
        return preorder
        '''
    def preorderTraversal(self, root: 'TreeNode'):
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


