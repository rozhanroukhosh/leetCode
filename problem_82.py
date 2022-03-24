#problem 82. Remove Duplicates from Sorted List II
#link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = head
        newone = None
        while data:
              holder = data.val
              if data.next and holder == data.next.val:
                    data = data.next.next
                    while data and holder == data.val:
                            data = data.next
              else:
               
                if(not newone):
                    newone = copy.copy(data)
                    newone.next = None
                   
                else:
                    temp = newone
                    while temp.next:
                          temp = temp.next
                    temp.next = copy.copy(data)
                    temp.next.next = None
                data = data.next
        return newone
        