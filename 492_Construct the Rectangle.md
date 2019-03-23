## 题目:  492. Construct the Rectangle

**描述**：给一个数字，返回其最接近的两个因数，且第一个大于等于第二个

### Method 1

- **思路**: 取该数字的平方根，然后检查平方根是否为其中一个，若是则返回，否则不断 -1 更新， 直到找到这两个数

  

- **代码**

  ```python
  class Solution:
      def constructRectangle(self, area):
          mid = int(pow(area, 0.5))
          while mid > 0:
              if area % mid == 0:
                  return [area // mid, mid]
             	mid -= 1
  ```

  

### Method 2

- **思路**: 把所有满足条件的值加入到 list 中，然后返回

  

- **代码**

  ```python 
  class Solution:
      def constructRectangle(self, area):
          for i in range(int(pow(area, 0.5)), 0, -1 ):
              if area % i == 0:
                  return [area//i, i]
      
  ```

  











