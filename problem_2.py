#disclaimer this is not the smartest way to solve it
#problem 2. Add Two Numbers
#link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum =0
        i = 0
        while l1 and l2:
            sum += (l1.val* (10 **(i))) + (l2.val* (10 **(i)))
            # print(l1.val* (10 **(i)), l2.val* (10 **(i)))
            l1 = l1.next
            l2 = l2.next
            i+=1
        # print(sum)
        if(l1 and not l2):
            while l1:
                 sum += l1.val* (10 **(i)) 
                 print(sum,l1.val* (10 **(i)) )
                 l1 = l1.next
                 i+=1
        if(l2 and not l1):
            while l2:
                 sum += l2.val* (10 **(i)) 
                 l2 = l2.next
                 i+=1
        # print(sum)
        sum = str(sum)[::-1]
        # print(sum)
        head =None
        for i in range(0,len(sum)):
            newNode = ListNode(sum[i] , None)
            if(head):
              current = head
              while(current.next):
                current = current.next
              current.next = newNode
            else:
              head = newNode
        return(head)
        
            
            
            
        