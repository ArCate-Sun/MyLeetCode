"""
Question:
	Search a 2D Matrix II

See:
	https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix or not matrix[0]:
			return False

		row, col = -1, -1
		for r in range(len(matrix)):
			if matrix[r][0] <= target:
				row = r
		for c in range(len(matrix[0])):
			if matrix[0][c] <= target:
				col = c

		print(row, col)

		for r in range(row + 1):
			for c in range(col + 1):
				if matrix[r][c] == target:
					return True
		return False


if __name__ == "__main__":


	inputs = [
		[[
			[1, 4, 7, 11, 15],
			[2, 5, 8, 12, 19],
			[3, 6, 9, 16, 22],
			[10, 13, 14, 17, 24],
			[18, 21, 23, 26, 30]
		], 5],
		[[
			[1, 4, 7, 11, 15],
			[2, 5, 8, 12, 19],
			[3, 6, 9, 16, 22],
			[10, 13, 14, 17, 24],
			[18, 21, 23, 26, 30]
		], 20],
		[[[]], 1]
	]
	targets = [
		True,
		False,
		False
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.searchMatrix(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
