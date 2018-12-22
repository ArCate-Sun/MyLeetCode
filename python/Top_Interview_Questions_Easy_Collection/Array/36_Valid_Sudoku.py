"""
Question:
	Valid Sudoku
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
"""


class Solution:
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""

		blocks = [set() for _ in range(9)]
		rows = [set() for _ in range(9)]
		cols = [set() for _ in range(9)]

		for i in range(9):
			for j in range(9):
				if board[i][j] == ".":
					continue
				# 判断块
				if board[i][j] in blocks[i // 3 * 3 + j // 3]:
					return False
				else:
					blocks[i // 3 * 3 + j // 3].add(board[i][j])
				# 判断行
				if board[i][j] in rows[i]:
					return False
				else:
					rows[i].add(board[i][j])
				# 判断列
				if board[i][j] in cols[j]:
					return False
				else:
					cols[j].add(board[i][j])
		return True


if __name__ == "__main__":
	s = Solution()

	input = [
		["5", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	]
	print("Input: %s" % input)
	output = s.isValidSudoku(input)
	print("Output: %s" % output)

	input = [
		["8", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	]
	print("Input: %s" % input)
	output = s.isValidSudoku(input)
	print("Output: %s" % output)
