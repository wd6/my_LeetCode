## 题目:  929. Unique Email Addresses

**描述**: 检查给定的一组 email 地址有多少是独立的. 本地名有 . 的忽略, 遇到+号的其后面忽略

### Method 1

- **思路**: 将 email split 为两部分, 将 local 里的 . 替换为空, + 号后面省略

  

- **代码**:

  ```python
  class Solution:
      def numUniqueEmails(self, emails):
          ans = 0
          email_set = set()
          for email in emails:
              local, domain = email.split('@')
              local = local.split('+')[0]
              local = local.replace('.', '')
              email_set.add(local+'@'+domail)
         	return len(email_set)
  ```


### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

