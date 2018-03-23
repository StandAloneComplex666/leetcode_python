# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         heights.append(0)
#         stack = [-1]
#         largest = 0
#         for i in range(len(heights)):
#             while heights[i] < heights[stack[-1]]:
#                 current_height = heights[stack.pop()]
#                 width = i - stack[-1] - 1
#                 area = width * current_height
#                 largest = max(area, largest)
#             stack.append(i)
#         heights.pop()
#         return largest

# import sys
# while 1:
#     st1 = raw_input()
#     st2 = raw_input()
#     count = 0
#     for j in len(st2):
#         temp_str = st2[j:j+len(st1)]
#         for i in len(st1):
#             if st1[i] != temp_str[i]:
#                 count += 1
#     sys.stdout.write('%d' %(count))


# import sys
# while 1:
#     res = 0
#     num = map(lambda x: int(x), raw_input().split(' '))
#     for i in range(1,10):
#         if i not in num:
#             res = i
#     if res != 0:
#         sys.stdout.write('%d' %(res))
#     if res = 0 and 0 not in num:
#         res = 10
#         sys.stdout.write('%d' %(res))
#     num_zero = []
#     num_nonzero = []
#     for i in range(len(num)):
#         if num[i] == 0:
#             num_zero.append.(0)
#         else:
#             num_nonzero.append(num[i])
#     num_nonzero = sorted(num_nonzero, reverse = True)
#     for i in range(num):
#         if i = 0:
#             res += 1
#         if i != 0 and num_zero:
#             res = res*10
#         if i != 0 and not num_zero and num_nonzero:
#             res = res*10 + num_nonzero[-1]
#             num_nonzero.pop()
#     sys.stdout.write('%d' %(res))





for i in range(9,0,-1):
    print(i)


