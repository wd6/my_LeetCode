## 题目:  506. Relative Ranks

**描述**：给一个数组代表分数， 返回一个数组代表排名

### Method 1

- **思路**: 本题目中，其实就是最大的分数有最小的排名。

  首先是我自己做的最普通的方法，比较繁琐

- **代码**

  ```python
  class Solution:
      def findRelativeRanks(self, nums):
          dic = {}
          for idx,val in enumerate(nums):
              sorted_nums = sorted(dic.items(), key = lambda x : x[0], reverse=True)
              index = list(zip(*sorted_nums))[1]
              for i, j in  enumerate(index):
                  li[i] = str(i+1)
              	if li[j] == '1':
                      li[j] = 'Gold Medal'
                  if li[j] == '2':
                      li[j] = 'Silver Medal'
                  if li[j] == '3':
                      li[j] = 'Bronze Medal'
              return li
                  
  ```

  

### Method 2

- **思路**: 自己做的非常繁琐，再看看优化之后的，使用 map 和 zip.

    第一步构建要返回的排名； 第二部将排名和分数用字典对应，第三部返回对应分数的排名 list

    

- **代码**

  ```python 
  class Solution:
      def findRelativeRanks(self, nums):
          ranks = list(map(str, range(1,len(nums)+1)))
          ranks[:3] = ['Gold Medal', 'Silver medal', 'Bronze Medal']
          rating = dict(zip(sorted(nums, reverse=True), ranks))
          return [rating[n] for n in nums]
          
  ```

  
