#622. Design Circular Queue
#link https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    queue = []
    front = 0
    rear = 0
    lenk = 0
    count = 0
    def __init__(self, k: int):
        self.queue = ['False' for i in range(k)]
        self.lenk = k
    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        else:
            self.queue[self.rear] = value
            if(self.rear<self.lenk-1):
                self.rear+=1
            else:
                self.rear=0
            self.count+=1
            return True
                
            
        

    def deQueue(self) -> bool:
       
        if(self.isEmpty()):
            return False
        else:
            self.queue[self.front] = 'False'
            if(self.front<self.lenk -1):
                self.front+=1
            else:
                self.front = 0
            self.count-=1
            return True
            
        

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.rear-1]
        

    def isEmpty(self) -> bool:
        return self.count==0
            
    def isFull(self) -> bool:
        return self.count==self.lenk
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()