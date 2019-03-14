## 题目:  121. Best Time to Buy and Sell Stock

**描述**:  

### Method 1

- **思路**: 取当前最小的价格， 然后不断更新，记录最大利润。

  

- **代码**:

  ```python
  calss Solution:
      def maxProfit(self, prices):
          minP, maxP = float('inf'), 0  # float('inf) 表示无穷大  
          							  # -float('inf') 表示负无穷
  		profit = price - minP
          maxP = max(maxP, profit)
      return maxP
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

