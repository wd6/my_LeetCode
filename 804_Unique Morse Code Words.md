## 题目:  804. Unique Morse Code Words

***描述***: 将给定的一组词转化为 Morse 密码, 检查不重复的密码有多少个

### Method 1

- **思路**: 简单题目

  

- **代码**:

  ```python
  class Solution:
      def(self, words):
          Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
          res = set()
          for word in words:
              morse = "".join([Morse[ord(letter)-ord('a')] for letter in word]) 
              res.add(morse)
          return len(res)
      
  # list expression
  """
  morse = {"".join(Morse[ord(letter)-ord('a')] for letter in word) for word in words}
  return len(morse)
  """
  ```

  







### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

