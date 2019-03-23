## 题目:  169_Majority Element

**描述**：给一个数组长度为 n，其中有一个元素有超过n/2 个，找出这个元素

### Method 1

- **思路**: 利用 collections 的 Counter

  

- **代码**

  ```python
  class Solution:
      def majorityElement(self, nums):
          import collections
          dic = collections.Counter(nums)
          dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
          return dic[0][0]
  ```

  

### Method 2

- **思路**: 超简单啊。 因为有一个元素多于 n/2 个， 那对数组排序后，最中间的元素一定是该元素

  

- **代码**

  ```python 
  class Solution:
      def majorityElement(self, nums):
          nums.sort()
          return nums[len(nums)//2]
  ```

  











