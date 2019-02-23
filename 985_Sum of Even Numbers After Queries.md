## 题目:  985. Sum of Even Numbers After Queries

**描述**:  对一个数组经过 Queries 变化后求相应的和

### Method 1

- **思路**:  先求出总的 Even 的和, 然后将对接下来要处理的元素进行处理, 入股它被加过,那就先把它还原,然后再处理

  

- **代码**:

  ```python
  class Solution:
      def sumEvenAfterQueries:
          ans = []
          s = sum(x for x in A if x%2==0)
          for val, i in queries:
              if A[i]%2 == 0:
                  s -= A[i]
             	A[i] += val
              if A[i]%2 == 0:
                  s += A[i]
              ans.append(s)
          return ans
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

