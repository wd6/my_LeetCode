## 28. Implement strStr()

***问题***: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

### Method 1

- **思路**: 比较暴力的解法, 用 if….else 判断, 然后返回相应的值

  

- **代码**

  ```python
  class Solution:
      def strStr(self, haystack:'str', needle:'str'):
          if not needle: return 0
          
          if len(needle) > len(haystack): return -1
          elif len(needle) == len(haystack):
              if needle == haystack: return 0
              else: return -1
          else:
              for i in range(0, len(haystack)-len(needle)+1):
                  if haystack[i:i+len(needle)] == needle:
                      return i
              return -1 
  ```


### Method 2

- **思路**: 用 Python 自带的 index 函数, (index() 可用于 str 和 list)

- **代码**

  ```python 
  class Solution:
      def strStr(self, haystack, needle):
          if needle in haystack:
              return haystack.index(needle)
          else:
              return -1
  ```

  











