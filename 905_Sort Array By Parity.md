## 题目:  905. Sort Array By Parity

**描述**: 将数组重新排列为先偶数再奇数

### Method 1

- **思路**: 将奇数挑选出来, 将偶数挑选出来, 然后合并

  

- **代码**:

  ```python
  class Solution:
      def sortArrayByParity(self, A):
          even = []
          odd = []
          for a in A:
              if a%2 == 0:
                  even.append(a)
              else:
                  odd.append(a)
         	return even+odd
  ```

  

### Method 2

- **思路**: 从首位开始进行判断,不断交换, 将所有偶数换到前面

  

- **代码**:

  ```python 
  class Solution:
      def sortArrayByParity(self, A):
          i, j = 0, len(A)-1
          while i<j:
              if A[i]%2 ==1 and A[j]%2 == 0:
                  A[i], A[j] = A[j], A[i]
              if A[i]%2 == 0:
                  i += 1
              if A[j]%2 == 1:
                  j -= 1
          return A
  ```

  

