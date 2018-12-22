"""
Question:
	Hamming Distance
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
"""


class Solution(object):
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		return bin(x ^ y).count("1")


if __name__ == "__main__":
	demos = [(1, 4)]
	results = [2]
	s = Solution()

	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.hammingDistance(*demo)
		else:
			output = s.hammingDistance(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
