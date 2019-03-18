## 题目:  242. Valid Anagram

**描述**：给两个字符串， 判断第二个字符串是不是第一个的另一个顺序

### Method 1

- **思路**: count()

  

- **代码**

  ```python
  class Solution:
      def isAnagram(self, s, t):
          if len(s) != len(t):
              return False
          k = set(s) # 保证后续循环没有重复
          for i in k:
              if s.count(i) != t.count(i):
                  return False
          return True
  ```

  

### Method 2

- **思路**: 排序后直接比较， 利用 sorted(); 还有一种利用 collections 里面的 Counter()

  

- **代码**

  ```python 
  class Solution:
      def isAnagram(self, s, t):
          return sorted(s) == sorted(t)
  
  '''
  import collections
  return collections.Counter(s) == collections.Counter(t)
  '''
  ```

  
