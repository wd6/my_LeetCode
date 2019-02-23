## 题目:  922. Sort Array By Parity II

**描述**: 将一个数组重排, 使得其偶数的索引位置出现偶数, 奇数的索引位置为奇数

### Method 1

- **思路**: 设置两个变量循环, 每次加2, 使得变量之前的均为正确的, 而后每次加二进行判断

  

- **代码**:

  ```python
  class Solution:
      def sortArrayByparityII(self, A):
          j = 1
          for i in range(0, len(A), 2)
          if A[i]%2 == 1:
              while A[j]%2 == 1:
                  j += 2
             	A[i], A[j] = A[j], A[i]
         	return A
  ```


### Method 2

- **思路**: 现将数组排序, 然后再将对应的数字放入对应位置

  

- **代码**:

  ```python 
  class Solution:
      def sortArrayByparityII(self, A):
          ans = []
          even = []
          odd = []
          for a in A:
              if a%2 == 0:
                  even.append(a)
             	else:
                  odd.append(a)
        	for i, j in zip(even, odd):
              ans.append(i)
              ans.append(j)
         	return ans
  ```

  

