class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.uni_nums = set()
        self.dup_nums = set()
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.uni_nums:
            self.uni_nums.add(number)
        else:
            if number not in self.dup_nums:
                self.dup_nums.add(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for number in self.dup_nums:
            if number * 2 == value:
                return True
        for number in self.uni_nums:
            if value - number in self.uni_nums and number != value - number:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)