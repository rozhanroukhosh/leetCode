#2287. Rearrange Characters to Make Target String
#link https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = []
        minC = 9999999
        for i in set(target):
            c = s.count(i)//target.count(i)
            if(minC>c):
                minC=c
        return minC
        
                