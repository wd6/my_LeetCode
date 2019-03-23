## 题目:  167. Two Sum 2_ Input array is sorted

**描述**：给一个数组和一个 target， 求出数组中两个和等于 target 的值得 index

### Method 1

- **思路**: 

  利用 hashtable, 检查 target 减去当前的值是否在字典中，字典中包含所有当前值之前的值，那么如果在，则返回之前的值得 index， 以及当前的 index

- **代码**

  ```python
  class Solution:
      def twoSum(self, nums, target):
          dic = {}
          for idx, val in enumerate(nums):
              if (target - val) in dic:
                  return [dic[target-val]+1, idx+1]
              else:
                  dic[val] = idx
  ```

  

### Method 2

- **思路**: 

  设置两个 pointer， 分别从前和后面进行判断

- **代码**

  ```python 
  class Solution:
      def sumTwo(self, nums, target):
          pre = 0
          post = len(nums) - 1
          while pre < post:
              if nums[pre] + nums[post] == target:
                  return [pre+1, post+1]
              elif nums[pre] + nums[post] < target:
                  pre += 1
              else:
                  post -= 1        
  ```

  
