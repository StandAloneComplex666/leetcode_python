# class Solution:
#     def isAdditiveNumber(self, num):
        
        
#         def recurse(end, level, prev, prev2):
#             if level > 2 and end == len(num):
#                 return True
#             for index in range(end+1, len(num)+1):
#                 if num[end:index][0] == '0' and len(num[end:index]) > 1: continue
#                 curr = int(num[end:index])
#                 if level <= 1 or (level > 1 and prev+prev2 == curr):
#                     if recurse(index, level+1, curr, prev): return True
#             return False
#         return recurse(0, 0, 0, 0)   
print('hello')