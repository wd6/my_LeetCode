## 题目:  268. Missing Number

*描述*: 给一个数组, 从0到 n, 其中有一个 missing 的数,找出它

总体:  这个题目和 找出 singleNumber 的题目是一个类型,可以用同样的方法来解决

### Method 1

- **思路**: 暴力匹配. 相当于新建了一个 list,然后逐一检查其元素是否在原来的 nums 中

- **代码**:

  ```python
  class Solution:
      def missingNumber(self, num):
          for num in range(len(nums)+1):
              if num not in nums:
                  return nums
  ```


### Method 2

- **思路**: 数学类的方法(高斯)

  

- **代码**:

  ```python 
  class Solution:
      def missingNumber(self, nums):
          expect = (len(n)+1) * len(n) // 2
          real = sum(nums)
          return expect - real
  ```

  

### Method 3

- **思路**: 异或的运算方法

  

- **代码**:

  ```python 
  class Solution:
      def missingNumber(self, nums)
      	nums = nums + list(range(len(nums)+1))
          a = 0
          for num in nums:
              a ^= num
          return a
  ```

### Method 2

- **思路**: 最优方法

  

- **代码**:

  ```python 
  class Solution:
      def missingNumber(self, nums):
  		return sum(range(len(nums)+1))-sum(nums)
  ```

