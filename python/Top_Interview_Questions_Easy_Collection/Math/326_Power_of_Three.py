"""
Question:
	Power of Three
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
"""


class Solution:
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""

		return n > 0 and 1162261467 % n == 0

	def isPowerOfThree2(self, n):
		"""
		:type n: int
		:rtype: bool
		"""

		if not n:
			return False
		while n % 3 == 0:
			n //= 3
		return n == 1

	def isPowerOfThree3(self, n):
		"""
		:type n: int
		:rtype: bool
		"""

		i = 1
		while i <= n:
			if i == n:
				return True
			i *= 3
		return False


if __name__ == "__main__":
	demos = [27, 0, 9, 45]
	s = Solution()

	for demo in demos:
		input = demo
		print("INPUT: %s" % input)
		output = s.isPowerOfThree2(input)
		print("OUTPUT: %s" % output)

