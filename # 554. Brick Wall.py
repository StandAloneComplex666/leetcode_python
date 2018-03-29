# a very naive way which will cause memory limit error
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counts = [0 for i in range(len(wall))]
        indexs = [0 for i in range(len(wall))]
        min_bricks = 10001
        width = sum(wall[0])
        print(width)
        for i in range(width):
            temp = 0
            for j in range(len(wall)):
                if counts[j] == wall[j][indexs[j]]:
                    indexs[j] += 1
                    counts[j] = 0
                else:
                    temp += 1
                    counts[j] += 1
            min_bricks = min(temp, min_bricks)
        return min_bricks
# beat 100% 一雪前耻！
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        space_dict = {}
        for row in wall:
            len_row = 0
            for brick in row[:-1]:
                len_row += brick
                if len_row not in space_dict:
                    space_dict[len_row] = 1
                else:
                    space_dict[len_row] += 1
        # if space_dict:
        #     return len(wall) - max(space_dict.values())
        # else:
        #     return len(wall)
        return len(wall) if (len(space_dict) == 0) else (len(wall) - max(space_dict.values()))