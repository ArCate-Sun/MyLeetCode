"""
Question:
	Rotate Image
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
"""
import math


class Solution:
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		for y in range(math.ceil(len(matrix) / 2)):
			for x in range(y, len(matrix) - y - 1):
				matrix[y][x], matrix[x][-y - 1], matrix[-y - 1][-x - 1], matrix[-x - 1][y] = matrix[-x - 1][y], matrix[y][x], matrix[x][-y - 1], matrix[-y - 1][-x - 1]


if __name__ == "__main__":
	s = Solution()

	matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	print("Input: %s" % matrix)
	s.rotate(matrix)
	print("Output: %s" % matrix)

	matrix = [
		[5, 1, 9, 11],
		[2, 4, 8, 10],
		[13, 3, 6, 7],
		[15, 14, 12, 16]
	]
	print("Input: %s" % matrix)
	s.rotate(matrix)
	print("Output: %s" % matrix)
