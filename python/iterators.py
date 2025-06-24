class Counter:
    def __init__(self,max_value):
        self.max = max_value
        self.counter = 0

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.max:
            self.counter+=1
            return self.counter
        else:
            raise StopIteration
        


s = Counter(5)

for x in s:
    print(x)