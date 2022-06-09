#752. Open the Lock
#link https://leetcode.com/problems/open-the-lock/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
                    
        q = deque()
        visit = set(deadends)
        q.append(["0000", 0])
        while q:
            lock_pos, turns = q.popleft()
            if lock_pos == target:
                return turns
            for i in range(4):
                digit = str((int(lock_pos[i]) + 1) % 10)
                child1 = lock_pos[:i] + digit + lock_pos[i+1:]
                digit = str((int(lock_pos[i]) + 10 - 1) % 10)
                child2 = lock_pos[:i] + digit + lock_pos[i+1:]
                if child1 not in visit:
                    visit.add(child1)
                    q.append([child1, turns + 1])
                if child2 not in visit:
                    visit.add(child2)
                    q.append([child2, turns + 1])
        return -1    
