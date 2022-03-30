#287. Find the Duplicate Number
#link https://leetcode.com/problems/find-the-duplicate-number/

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counting = Counter(nums)
        return(counting.most_common(1)[0][0])
        