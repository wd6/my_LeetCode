## 题目:  1005. Maximize Sum Of Array After K Negations

**描述**：给一个数组和一个整数， 对数组执行 K 次正负变换，返回最大的和

### Method 1

- **思路**: 首先对数组进行排序，然后进行符号操作，if 原数字小于0， 直接改变其符号，一旦原数字开始等于或大于零，则直接选择数组中当前最小的数并重复对其进行变换（确定其符号）

  

- **代码**

  ```python
  class Solution:
      def largestSumAfterKNegations(self, A, k):
          A.sort()
          for i in range(K):
  			if A[i] < 0:
                  A[i] = -A[i]
              else:
                  A_min = min(A)
                  A[A.index(A_min)] = A_min * pow(-1, K-i)
                 	break
         	return sum(A)
  ```

  

### Method 2

- **思路**: 利用 Python 的堆 heapq

  

- **代码**

  ```python 
  class Solution:
      def 
  ```

  
