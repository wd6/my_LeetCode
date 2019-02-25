## 题目:  860. Lemonade Change

**描述**:  顾客每次付钱5,10,20元, 柠檬摊主是否可以按照给定的顺序找零钱

### Method 1

- **思路**: if 语句不断判断当下的情况

  

- **代码**:

  ```python
  class Solution:
      def lemonadeChange(self, bills: List[int]) -> bool:
          
          count = {5:0,10:0}
          for b in bills:
              if b == 5:
                  count[5] += 1
              elif b == 10 and count[5] >0:
                  count[5]-=1
                  count[10]+=1           
              elif b==20 and count[10]>0 and count[5]>0:
                  count[10]-=1
                  count[5] -= 1
              elif b==20 and count[5]>=3:
                  count[5]-=3
              else:
                  return False
          return True
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

