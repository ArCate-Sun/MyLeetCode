"""
Question:
	Fizz Buzz
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
"""


class Solution:
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		result = [str(i) for i in range(1, n + 1)]
		for i in range(2, n, 3):
			result[i] = "Fizz"
		for i in range(4, n, 5):
			result[i] = "Buzz"
		for i in range(14, n, 15):
			result[i] = "FizzBuzz"
		return result


if __name__ == "__main__":
	s = Solution()

	input = 15
	print("INPUT: %s" % input)
	output = s.fizzBuzz(input)
	print("OUTPUT: %s" % output)
