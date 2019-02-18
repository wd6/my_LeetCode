## 题目: 13_ Roman to Integer

*tips*

### Method 1

- **思路**: 关键点就是如果一个罗马字符比其前一个字符的值大, 那么其就应该减去前面的值,我们只需要用一个 if 条件判断就好. 时间复杂度 $O(n)$

  

- **代码**

  ```python
  class Solution:
      def romanToInt(self, s):
          roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
          pre = 0
          num = 0
          for i in s:
              current = roman[i]
              num += current
              if current > pre:
                  num -= 2*pre
              pre = current
          return num
  ```




### Method 2: 暂时只想到一种方法

- **思路**:

  

- **代码**

  ```python 
  
          
  ```

  

