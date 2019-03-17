## 题目:  2. Add two numbers

**描述**:  You are given two non-empty linked lists representing two non-negative integers. The digits are sorted in reverse order and each of node contains a single digit. Add th two numbers and return it as a linked list

### Method 1

- **思路**:  对于 linked list, 需要一个元素一个元素进行操作。不断去除两个 list 中的元素相加，除以10的余数作为新 list 的 node， 而其整数部分则顺加到下一位

  

- **代码**:

  ```python
  class Solution:
      def addTwoNumber(self, l1, l2):
      		dummy = cur = ListNode(0)
      		carry = 0
      		while l1 or l2 or carry:
        			if l1:
         					carry += l1.val
          				l1 = l1.next
        			if l2:
          				carry += l2.val
          				l2 = l2.next
        					cur.next = ListNode(carry%10)
        			cur = cur.next
        			carry //= 10
      		return dummy.next
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

