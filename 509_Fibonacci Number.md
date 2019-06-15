## 题目: 509_ Fibonacci number

***描述***: 裴波那切数列

### Method 1

- **思路**: Recursion 递归

  

- **代码**:

```python
def fib(N):
    if N == 0: return 0
    if N == 1: return 1
    else: return fib(N-1)+ fib(N-2)
  ```

  

### Method 2

- **思路**: 迭代 iteration

  

- **代码**:

```python 
def fib(N):
    if N == 0: return 0
    if N == 1: return 1
    else: 
        a = 0
        b = 1
        n = 2
        while n <= N:
            a, b = b, a+b
            n += 1
        return b
              
        
              
  ```

  

