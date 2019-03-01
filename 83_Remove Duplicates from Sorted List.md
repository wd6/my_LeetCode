## 题目:  83. Remove Duplicates from Sorted List

**描述**: 从链表中移除重复的值

## Python 的变量都只是指针

### Method 1

- **思路**: Remove duplicates from sorted linked list

  

- **代码**:

  ```python
  class Solution:
      def deleteDuplicates(self, head: ListNode):
          current = head
          while current:
              while current.next and current.next.val == current.val:
                  current.next == current.next.next
             	current = current.next
        	return head
  ```

  

### Method 2

- **思路**: 递归

  

- **代码**:

  ```python 
  
  ```

  

