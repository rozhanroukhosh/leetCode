#347. Top K Frequent Elements
#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        frequent = [counted[0]for counted in a.most_common(k)]
        return frequent