"""
Question:
	Pascal's Triangle
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
"""


class Solution:
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""

		if numRows == 0:
			result = []
		elif numRows == 1:
			result = [[1]]
		elif numRows == 2:
			result = [[1], [1, 1]]
		else:
			result = [[1], [1, 1]]
			for i in range(2, numRows):
				row = [1] + [result[-1][i] + result[-1][i + 1] for i in range(i - 1)] + [1]
				result.append(row)

		return result

	def generate_2(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""

		result = []
		for i in range(numRows):
			row = []
			for j in range(i + 1):
				if j == 0 or j == i:
					row.append(1)
				else:
					row.append(result[i - 1][j - 1] + result[i - 1][j])
			result.append(row)
		return result


if __name__ == "__main__":

	demos = [5]
	results = [
		[
			[1],
			[1, 1],
			[1, 2, 1],
			[1, 3, 3, 1],
			[1, 4, 6, 4, 1]
		]
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.generate(*demo)
		else:
			output = s.generate(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
