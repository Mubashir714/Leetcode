class FreqStack:

    def __init__(self):
        self.element=defaultdict(int)
        self.freq=defaultdict(list)   
        self.max_feq=0

    def push(self, val: int) -> None:
        self.element[val]+=1
        count=self.element[val]
        self.freq[count].append(val)
        self.max_feq=max(count,self.max_feq)


    def pop(self) -> int:
        
        value=self.freq[self.max_feq].pop()
        self.element[value]=self.max_feq-1
        if not self.freq[self.max_feq]:
            self.max_feq-=1
        return value



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()