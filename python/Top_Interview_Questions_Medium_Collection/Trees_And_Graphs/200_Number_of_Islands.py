"""
Question:
	Number of Islands

See:
	https://leetcode.com/problems/number-of-islands/
"""

from typing import List


class Solution:

	def removeIsland(self, grid, r, c):
		if r > 0 and grid[r - 1][c] == "1":
			grid[r - 1][c] = "0"
			self.removeIsland(grid, r - 1, c)
		if r + 1 < len(grid) and grid[r + 1][c] == "1":
			grid[r + 1][c] = "0"
			self.removeIsland(grid, r + 1, c)
		if c > 0 and grid[r][c - 1] == "1":
			grid[r][c - 1] = "0"
			self.removeIsland(grid, r, c - 1)
		if c + 1 < len(grid[r]) and grid[r][c + 1] == "1":
			grid[r][c + 1] = "0"
			self.removeIsland(grid, r, c + 1)

	def numIslands(self, grid: List[List[str]]) -> int:

		if not grid:
			return 0

		row = len(grid)
		col = len(grid[0])

		count = 0
		for r in range(row):
			for c in range(col):
				if grid[r][c] == "1":
					grid[r][c] = "0"
					count += 1
					self.removeIsland(grid, r, c)

		return count


if __name__ == "__main__":
	demos = [
		[
			["1", "1", "1", "1", "0"],
			["1", "1", "0", "1", "0"],
			["1", "1", "0", "0", "0"],
			["0", "0", "0", "0", "0"],
		],
		[
			["1", "1", "0", "0", "0"],
			["1", "1", "0", "0", "0"],
			["0", "0", "1", "0", "0"],
			["0", "0", "0", "1", "1"],
		]
	]
	results = [
		1,
		3
	]

	s = Solution()
	for demo, result in zip(demos, results):

		output = s.numIslands(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()

