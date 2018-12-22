"""
Question:
	Number of 1 Bits
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
"""


class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		return bin(n).count("1")

	def hammingWeight2(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		count = 0
		while n:
			count += n % 2
			n //= 2
		return count


if __name__ == "__main__":
	demos = [11, 128, 4294967293]
	results = [3, 1, 31]
	s = Solution()

	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.hammingWeight(*demo)
		else:
			output = s.hammingWeight(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
