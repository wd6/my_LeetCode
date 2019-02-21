## 题目:  561.  Array Partition 1

***描述***: 给一个 2n 长度的数组, 将其分为两两一组, 返回使得每一组的最小值的和最大的最大值

### Method 1

- **思路**: 对数组进行排序, 然后按照顺序两两即为一对, 间隔取出并求和

  

- **代码**:

  ```python
  class Solution:
      def arrayPairSum(self, nums):
          nums.sort()
          res = 0
          n = 0
          while n<len(nums):
              res += nums[n]
              n += 2
         	return res
  ```


### Method 2

- **思路**: 用 list 的 slice

  

- **代码**:

  ```python 
  class Solution:
      def arrayPairSum(self, nums):
          nums.sort()
          return sum(nums[::2])
  ```

  

