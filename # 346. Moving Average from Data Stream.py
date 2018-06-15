class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.total = 0
        self.num = 0
        self.queue = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += val
        if len(self.queue) == self.size:
            self.total-= self.queue.pop(0)
        else: self.num += 1
        self.queue.append(val)
        return self.total/float(self.num)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)