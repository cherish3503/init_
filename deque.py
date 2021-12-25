class Deque:
    def __init__(self):
        self.data = list()
        
    def push_front(self, i):
        self.data.insert(0,i)
        
    def push_back(self, i):
        self.data.append(i)
        
    def pop_front(self):
        if self.isEmpty():
            return -1
        else:
            tmp = self.data[0]
            del self.data[0]
            return tmp
        
    def pop_back(self):
        if self.isEmpty():
            return -1
        else:
            tmp = self.data[self.size()-1]
            del self.data[self.size()-1]
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
