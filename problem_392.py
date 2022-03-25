#392. Is Subsequence
#https://leetcode.com/problems/is-subsequence/

import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         reexp =""
#         for i in range(len(s)):
#             reexp+=".*"+s[i]
 
#         isAmatch = re.match(reexp, t)
#         if(isAmatch):
#             return True
#         else:
#             return False
            i = 0
            j=0
            while i<len(s) and j <len(t):
                  if(s[i]==t[j]):
                        i+=1
                  j+=1
            return i==len(s)
            