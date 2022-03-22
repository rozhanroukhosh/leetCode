#1663. Smallest String With A Given Numeric Value
#https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        newS = ''
        i=26
        while i>0 and n>0 and k>0:
            #reason for +1 is that I am already looking for this place
            while(int((k+1-n)/i)>0 and n>0 and k>0):
                #while it is possible always choose the highest charcter
                 newS+=chr(i + 96)
                 k-=i
                 n-=1
            i-=1
        return newS[::-1]