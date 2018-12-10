"""
Question:
	House Robber
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
"""


class Solution:
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		a, b = 0, 0
		for num in nums:
			a, b = b, max(a + num, b)
		return b


if __name__ == "__main__":
	s = Solution()

	input = [1, 2, 3, 1]
	print("Input: %s" % input)
	output = s.rob(input)
	print("Output: %s" % output)

	input = [2, 7, 9, 3, 1]
	print("Input: %s" % input)
	output = s.rob(input)
	print("Output: %s" % output)

	input = [1, 1, 1, 2]
	print("Input: %s" % input)
	output = s.rob(input)
	print("Output: %s" % output)
