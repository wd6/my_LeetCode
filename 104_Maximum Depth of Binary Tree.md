## 题目 104 .Maximum Depth of Binary Tree

*tips*: 二叉树相关

### Method 1: 递归 (Recursion)

- **思路**: 

  

- **代码**

  ```python
  class TreeNode:
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
  class Solution1:
      def maxDepth(self, root: 'TreeNode'):
          if not root:
              return 0
          return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
  ```

  







### Method 2: 迭代 (Iteration)

- **思路**: 用一个临时 list 来捕获每一层的 node, 从而实现树的深度的计算

  

- **代码**

  ```python 
  class TreeNode:
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
  class Solution2:
      def maxDepth(self, root: 'TreeNode'):
          if not root:
              return 0
          else:
              depth = 0
              q = [root]
              while q:
                  temp = []
                  for node in q:
                  	if node.left:
                      	temp.append(node.left)
                  	if node.right:
                      	temp.append(node.right)
                  q = temp
           	return depth
  ```

  

