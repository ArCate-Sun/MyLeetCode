"""
Question:
	Set Matrix Zeroes
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
"""


class Solution:
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""

		if not matrix:
			return

		row = len(matrix)
		col = len(matrix[0])

		has_zero_in_first_row = 0 in matrix[0]
		has_zero_in_first_col = 0 in [matrix[r][0] for r in range(row)]

		for r in range(1, row, 1):
			for c in range(1, col, 1):
				if not matrix[r][c]:
					matrix[r][0] = 0
					matrix[0][c] = 0

		for r in range(1, row, 1):
			for c in range(1, col, 1):
				if not matrix[r][0] or not matrix[0][c]:
					matrix[r][c] = 0

		if has_zero_in_first_row:
			matrix[0] = [0] * col
		if has_zero_in_first_col:
			for r in range(row):
				matrix[r][0] = 0




if __name__ == "__main__":

	demos = [
		[
			[1, 1, 1],
			[1, 0, 1],
			[1, 1, 1]
		],
		[
			[0, 1, 2, 0],
			[3, 4, 5, 2],
			[1, 3, 1, 5]
		]
	]
	results = [
		[
			[1, 0, 1],
			[0, 0, 0],
			[1, 0, 1]
		],
		[
			[0, 0, 0, 0],
			[0, 4, 5, 0],
			[0, 3, 1, 0]
		]
	]

	s = Solution()
	for demo, result in zip(demos, results):

		print("INPUT: %s" % str(demo))

		if type(demo) == tuple:
			output = s.setZeroes(*demo)
		else:
			output = s.setZeroes(demo)

		if demo == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(demo))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(demo))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()

