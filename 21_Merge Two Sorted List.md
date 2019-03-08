## 题目:  21_Merge Two Sorted Lists

**描述**: 

### Method 1

- **思路**: 

  

- **代码**:

  ```python
  class Solution:
      def mergeTwolists(self, l1, l2):
          dummy = cur = ListNode(0)
          while l1 and l2:
              if l1.val < l2.val:
                  cur.next = l1
                  l1 = l1.next
              else:
                  cur.next = l2
                  l2 = l2.next
             	cur = cur.next
          cur.next = l1 or l2
          return dummy.next
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

