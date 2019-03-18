## 题目:  219. Contains Duplicate 2

**描述**: 给一个数组和一个 k 值， 检查数组是否有两个相同元素且其之间距离不大于 k

### Method 1

- **思路**: 利用 enumerate 函数， 以数值为键，以索引为字典 value，不断加入到字典中，判断是否已经在字典里，如果在，判断其距离，若小于等于 k 即可返回。否则就继续将该数值加入字典中 (在重复但是大于的情况下，字典值会更新)

  

- **代码**:

  ```python
  class Solution:
    def containsNearbyDuplicate(self, nums):
      if len(set(nums)) == len(nums):
        return False
      dic = {}
      for i, j in enumerate(nums):
        if j in dic and i-dic[j] <= k:
          return true
        dic[j] = i
      return False
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

