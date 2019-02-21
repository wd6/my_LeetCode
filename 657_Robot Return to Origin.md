## 题目:  657. Robot return to origin

***描述***: 机器人在 "UDLR" 方位指示下行动,最终是否停在原位

### Method 1

- **思路**: 只要U==D和 L==R, 说明可以返回原位,否则不能. 暴力方法,每次移动进行更新坐标,看最终是否在原点

  

- **代码**:

  ```python
  class Solution:
      def judgeCircle(self, moves)
      	x = 0
          y = 0
          for m in moves:
              if m == 'U':
                  y += 1
              elif m == 'D':
                  y -= 1
              elif m == 'R':
                  x += 1
              elif m == 'L':
                  x -= 1
              else:
                  x,y = x,y
          return x == 0 and y == 0
  ```


### Method 2

- **思路**: 用 Python str.count()

  

- **代码**:

  ```python 
  class Solution:
      def judgeCircle(self, moves)
      	U = moves.count('U')
          D = moves.count('D')
          L = moves.count('L')
          R = moves.count('R')
          if U==D and L==R:
              return True
          else:
              return False   
  ```

  

