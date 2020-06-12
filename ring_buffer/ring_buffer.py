class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.current] = item
            self.current+= 1
            if(self.current > 4):
                self.current = 0
        

    def get(self):
        return self.data
