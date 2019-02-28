## 题目:  203. Remove Linked List Elements

**描述**:  移除 linked list 里面的 val

### Method 1

- **思路**: 

  

- **代码**:

  ```python
  class Solution:
      def removeElements(self, head):
          if not head:
              return None
          current = head
          while current.next:
              if current.next.val == val:
                  current.next = current.next.next
              else:
                  current = current.next
          return head.next if head.val == val else head
      
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

