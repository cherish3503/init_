class Stack:
    def __init__(self):
        self.top = list()
        
    def push(self, i):
        self.top.append(i)
        
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            tmp = self.top[len(self.top)-1]
            del self.top[len(self.top)-1]
            return tmp
            
    def size(self):
        return len(self.top)
        
    def isEmpty(self):
        if len(self.top) == 0:
            return True
        else:
            return False
        
    def top(self):
        return self.top[len(self.top)-1]
    
