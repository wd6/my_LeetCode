## 题目: 136. Single Number

*描述*: 给定一个非空的整数数组, 除了其中一个元素以外,其他元素都出现两次,找出这个只出现一次的元素

### Method 1

- **思路**: 新建一个 list, 循环每一个元素,检查其是否在 list 中, 如果在就,remove 它, 如果不在,就 append 它, 最后返回 list 中的元素. $O(n^2)$

  

- **代码**:

  ```python
  class Solution:
      def singleNumber(self, nums):
          alist = []
          for n in nums:
              if n in alist:
                  alist.remove(n)
              else:
                  alist.append(n)
          return alist[0]
  ```


### Method 2

- **思路**: 数学方法, 因为只有一个数字是单独的,其他都是两个,所以取 set, 那么 2倍的 set 减去原来的就是要找的数字. $ O(n) $

  

- **代码**:

  ```python 
  class Solution:
      def singleNumber(self, nums):
          return 2*sum(set(nums))-sum(nums)
  ```

  

### Method 3

-  **思路**: 用 Python 字典,也就是 hash table. 和方法一很相似,但是更快

  

- **代码**:

  ```python
  class Solution:
      def singleNumber(self, nums):
          dic = {}
          for n in nums:
              try:
                  dic.pop(n)
              except:
                  dic[n] = 1
         	return dic.popitem()[0]
  ```



### Method 4

- **思路**: XOR (异或), Python 中用符号 ^ 表示. 非零的数和0 异或为 非零的数; 两个非零的数异或为0; 



- **代码**

```python
class Solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a = a^i
        return a
```

