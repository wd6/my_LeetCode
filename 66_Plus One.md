## 题目:  66. Plus One

**描述**:  给一个只包含个位数的 list, 给 list 末尾加一, 如果是等于10 则需要将该位置变为0,并给前一个加一

### Method 1

- **思路**: 将 list 转换成字符串, 在转换成 int 型,然后加1, 再转换会数字 list

  

- **代码**:

  ```python
  class Solution:
      def plusOne(self, digits):
          num = int(''.join(map(str,digits)))+1
          return [int(i) for i in str(num)]
  ```

  

### Method 2

- **思路**: 从最后一个位置向前判断, 如果该位置小于9, 那该位置直接加1 并返回; 否则将该位置变为0, 然后检查下一个位置. 直到检查完. 最终返回<code>[1]+[0]*len(digits)</code>

- **代码**:

  ```python 
  class Solution:
      def plusOne(self, digits):
          for i in range(1, len(digits)+1):
              if digits[-i] < 9:
                  digits[-i] += 1
                  return digits
              digits[-i] = 0
          return [1] + [0]*len(digits)
  ```

  

