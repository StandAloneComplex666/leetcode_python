class Solution:
    def helper(self, n, path, res):
        d1 = { '0', '1', '8' }
            
        d2 = {
            '1': '1',
            '8': '8',
            '0': '0',
            '6': '9',
            '9': '6'
        }

        if n == 0:
            res.append(path)
            return
        elif n == 1:
            mid = len(path) // 2
            for num in d1:
                res.append(path[:mid] + num + path[mid:])
            return
        
        for key, val in d2.items():
            if (n == 2 or n == 3) and key == '0':
                continue
            self.helper(n - 2, key + path + val, res)
        
        return
        
    def findStrobogrammatic(self, n):
        res = []
        self.helper(n, "", res)
        
        return res