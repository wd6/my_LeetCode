## 题目: 104_Maximum Depth of Binary Tree

*描述*: 给一个 Binary Tree, 返回其深度(层数)

### Method 1

- **思路**: 递归(每次返回所有 Node 的左右里面最大的,+1)

  

- **代码**:

  ```python
  class Solution:
      def maxDepth(root:"TreeNode"):
          if not root:
              return 0
          return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
  ```

  

### Method 2

- **思路**: 迭代, 每次将一层加入到一个列表中,一直到列表为空,说明已经加完

  

- **代码**:

  ```python 
  class Solution:
      def maxDepth(root):
          if not root:
              return 0
          queue = [root]
          depth = 0
          while queue:
              depth += 1
              temp = []
              for node in queue:
                  if node.left: temp.append(node.left)
                  if node.right: temp.append(node.right)
              queue = temp
          return depth
                  
              
  ```

  

