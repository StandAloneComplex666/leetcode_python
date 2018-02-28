import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

    def matrixReshape(self, nums, r, c):
	    flat = sum(nums, [])
	    if len(flat) != r * c:
	        return nums
	    tuples = zip(*([iter(flat)] * c))
	    return map(list, tuples)

	def matrixReshape(self, nums, r, c):
	    if r * c != len(nums) * len(nums[0]):
	        return nums
	    it = itertools.chain(*nums)
	    return [list(itertools.islice(it, c)) for _ in xrange(r)]