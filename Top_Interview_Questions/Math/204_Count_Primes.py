"""
Question:
	Count Primes
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
"""


class Solution:

	def is_prime(self, n):
		"""
		判断是否为质数
		:type n: int
		:rtype: bool
		"""
		if n <= 1:
			return False
		for i in range(2, int(n ** 0.5) + 1):
			if n // i * i == n:
				return False
		return True

	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		count = 0
		for i in range(n):
			if self.is_prime(i):
				count += 1
		return count

if __name__ == "__main__":
	s = Solution()

	input = 10
	print("INPUT: %s" % input)
	output = s.countPrimes(input)
	print("OUTPUT: %s" % output)
