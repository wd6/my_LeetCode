## 题目:  38_Count and Say

**描述**: 下一个数字代表的 sequence 是上一个的读法. 例如 21, 读作1211

### Method 1

- **思路**: 设置一个参数, 检查上一个里面的每一个数字,如果相同,则计数加一, 如果不同,则更新参数数字, 并将原来已经计算完成的第一个数字 append 

  

- **代码**:

  ```python
  class Solution:
      def countAndSay(self, n):
          s = '1'
          for i in range(n-1):
              temp = ''
              letter = s[0]
              count = 0
              for num in s
              	if s[i] == letter:
                  	count+=1
              	else:
                      temp += str(count)+letter
                      count = 1
             	temp += str(count)+letter
              s = temp
        	return s
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

