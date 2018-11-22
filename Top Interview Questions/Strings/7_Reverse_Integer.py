"""
Question:
	Reverse Integer
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""


class Solution:
	_MAX_INT = 2 ** 31 - 1
	_MIN_INT = - 2 ** 31

	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		result = 0
		is_negative = x < 0
		x = abs(x)
		while x != 0:
			result = result * 10 + x % 10
			x //= 10

		result *= (-1) ** is_negative

		return result if self._MIN_INT <= result <= self._MAX_INT else 0



if __name__ == "__main__":
	s = Solution()

	input = 123
	print("Input: %s" % input)
	output = s.reverse(input)
	print("Output: %s" % output)

	input = -123
	print("Input: %s" % input)
	output = s.reverse(input)
	print("Output: %s" % output)

	input = 1534236469
	print("Input: %s" % input)
	output = s.reverse(input)
	print("Output: %s" % output)
