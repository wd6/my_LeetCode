## 题目:  Best time to buy and sell stock 2

**描述**:  

### Method 1

- **思路**: 

  

- **代码**:

  ```python
  class Solution:
      def maxProfit(self, prices):
          if len(prices) < 2:
              return 0
          pre = prices[0]
          ans = 0
          for price in prices[1:]:
              if price>pre:
                  ans += price-pre
              pre = price
          return ans
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  class Solution:
      def maxProfit(self, prices):
          return sum(y-x for x,y in zip(prices[:-1], prices[1:]) if y>x)
  ```

  

