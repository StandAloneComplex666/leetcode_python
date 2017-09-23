#49ms / 66.98%
class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		ones,twos=0,0
		for ele in A:
			ones = ones^ele & ~twos
			twos = twos^ele & ~ones
		return ones
