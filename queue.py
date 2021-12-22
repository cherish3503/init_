class Queue:
    def __init__(self):
        self.data = list()
        
    def enqueue(self, i):
        self.data.append(i)
        
    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            tmp = self.data[0]
            del self.data[0]
            return tmp
            
    def size(self):
        return len(self.data)
        
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def front(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[0]
    
    def back(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[len(self.data)-1]
    
