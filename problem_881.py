#881. Boats to Save People
#link: https://leetcode.com/problems/boats-to-save-people/
#the idea is if the lightest and haviest go together on the Boat
#we will have the mminum number of people on boat

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people = sorted(people, reverse=True) 
        count = 0
        i = 0
        j = len(people)-1
        while i <= j:
            while(people[j]+people[i]<=limit):
                    j-=1
                   
            count+=1
            i+=1
        return count

   
                
        