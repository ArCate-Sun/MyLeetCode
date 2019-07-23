"""
Question:
	Unique Paths
See:
	https://leetcode.com/problems/unique-paths/
"""
from typing import List
from common.verification import Verification


class Solution:
	def uniquePaths(self, m: int, n: int) -> int:

		if m <= 1 or n <= 1:
			return 1

		m = m - 1
		table = [[1] * n for i in range(m)]
		for r in range(1, m):
			for c in range(1, n):
				table[r][c] = table[r - 1][c] + table[r][c - 1]
		return sum(table[-1])


if __name__ == "__main__":

	inputs = [
		[3, 2],
		[7, 3]
	]
	targets = [
		3,
		28
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.uniquePaths(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
