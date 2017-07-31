#55. Jump Game
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        distance = 0
        can_jump = 0
        for i in A[:-1]:
            can_jump = max(can_jump, distance + i)
            if(can_jump <= distance):
                return False
            distance += 1
        return True