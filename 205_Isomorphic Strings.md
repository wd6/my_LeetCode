## 题目:  205. Isomorphic Strings

**描述**：检查两个字符串是否结构相同

### Method 1

- **思路**: 用字典来把所有字母的索引存起来，然后排序，如果排序后的索引列表相等，返回 True

  

- **代码**

  ```python
  class Solution:
      def isIsomorphic(self, s, t):
          ss = {}
          tt = {}
          for i, val in enumerate(s):
              ss[val] = ss.get(val, [])+[i]
          for i, val in enumerate(t):
              tt[val] = tt.get(val, [])+[i]
          return sorted(ss.values()) == sorted(tt.values())
      
  ```

  

### Method 2

- **思路**: 利用 set, 如果两个结构相同，那他们 zip 以后的 set 的长度和两者分别的长度也相同

- **代码**

  ```python 
  class Solution:
      def findDisappearedNumber(self, s, t):
          return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
  ```

  











