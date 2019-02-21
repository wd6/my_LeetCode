## 题目: 500. Keyboard Row

*描述*: 找出 list 里面的单词中的所有字母都在键盘上的一行的单词

### Method 1

- **思路**: 根据单词的第一个字母,检查剩余字母是否和第一个字母在一行,若没有则 flag==0, 如果检查完 flag 仍然等于1, 则将该单词加入待返回的 list

  

- **代码**:

  ```python
  class Solution:
      def findWords(self, words):
          keys = ["qwertyuiop","asdfghjkl", "zxcvbnm" ]
          onerow = []
          for word in words:
              w = word.lower()
              flag = True
              
              if w[0] in keys[0]:
                  for l in w[1:]:
                      if l not in keys[0]:
                          flag = False
                  		break
              if w[0] in keys[1]:
                  for l in w[1:]:
                      if l not in keys[1]:
                          flag = False
              			break
              if w[0] in keys[2]:
                  for l in w[1:]:
                      if l not in keys[2]:
                          flag = False
                          break
              if flag == True:
                  onerow.append(word)
         	return onerow
          
  ```


### Method 2

- **思路**: 构建字典, 键盘上在同一行的字母都赋值同一个数字. 然后利用 Python set 的特性(不能有重复的元素). 最后检查 set 的长度,即可判断该字符串的所有字母是否都在一行

  

- **代码**:

  ```python 
  class Solution:
      def findWords(self, words):
          dic = {}
          res = []
          for a in "qwertyuiop":
              dic[a] = 1
          for b in "asdfghjkl":
              dic[b] = 2
          for c in "zxcvbnm":
              dic[c] = 3
          
          for word in words:
              wordset = set()
              w = word.lower()
              for l in w:
                  wordset.add(l)
              if len(wordset) == 1:
                  res.append(word)
         	return res
  ```

  

