## 题目:  961. N-Repeated Element in Size 2N

**描述**: 有一个 2N 长度的数组, 其中有 N+1个独特的元素, 其中有一个元素重复 N 次, 找出这个元素并返回

### Method 1

- **思路**: 注意题目中除了一个元素外其余元素都独立,所以一旦发现重复元素,那其必然是重复了 N 次的那个元素, 直接返回即可

  

- **代码**:

  ```python
  class Solution:
      def repeatedNTimes(self, A):
          check = []
          for i in A:
              if i in check:
                  return i
           	check.append(i)
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

