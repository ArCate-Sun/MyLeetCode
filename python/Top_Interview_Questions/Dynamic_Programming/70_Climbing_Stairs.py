"""
Question:
	Climbing Stairs
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
"""


class Solution:
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		a, b = 0, 1
		for _ in range(n):
			a, b = b, a + b
		return b

	def calculate_c(self, m, n):
		"""
		C(m, n)
		:param m: base
		:param n: num
		:return:
		"""

		if n > m // 2:
			n = m - n

		if n == 0:
			return 1

		a = m
		b = n
		for i in range(1, n):
			a *= m - i
			b *= n - i

		return int(a / b)

	def climbStairs2(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		result = 1
		for i in range(1, n // 2 + 1):
			result += self.calculate_c(n - i, i)
		return result


if __name__ == "__main__":
	s = Solution()

	input = 2
	print("Input: %s" % input)
	output = s.climbStairs(input)
	print("Output: %s" % output)

	input = 3
	print("Input: %s" % input)
	output = s.climbStairs(input)
	print("Output: %s" % output)

