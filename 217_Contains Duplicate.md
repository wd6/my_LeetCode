## 题目:   217. Contains Duplicate

**描述**:  给一个数组，检查该数组是否包含重复的元素

### Method 1

- **思路**: 暴力检查。将每一个元素不断加入新建的字典中（字典比 list 快）， 检查新元素是否在 list， 如果在，说明有重复元素，则返回 True， 否则继续检查到最后，返回 False

  

- **代码**:

  ```python
  class Solution:
    def containDuplicate(self, nums:List[int]):
      check = {}
      for i in nums:
        if i in check:
          return True
        check[i] = 0
      return False
  ```

  

### Method 2

- **思路**: 利用Python 的 Sort() 函数，将数组先排序，然后检查相邻元素是否相等

  

- **代码**:

  ```python 
  class Solution:
    def containDuplicate(self, nums):
      if not nums: return False
      nums.sort()
      for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
          return True
     	return False
  ```


###  

### Method 3

- **思路**： 最好的方法是利用 Python 的 set 函数， 如果 set 的长度和原 list 长度相同，那说明没有重复元素，否则有重复元素。**注意**：在涉及重复元素的问题上都应该想到 set 的作用
- 代码：

```python
class Solution:
  def containDuplicate(self, nums):
    if not nums: return False
    return len(set(nums)) != len(nums)
```



