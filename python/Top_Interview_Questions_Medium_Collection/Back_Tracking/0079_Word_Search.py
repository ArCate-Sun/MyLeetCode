"""
Question:
	Word Search
See:
	https://leetcode.com/problems/word-search/
"""
import collections
from typing import List
from common.verification import Verification


class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:

		def _exist(r, c, words):

			if not words:
				return True
			if not 0 <= r < row or not 0 <= c < col:
				return False
			if board[r][c] != words[0]:
				return False
			if (r, c) in queue:
				return False

			queue.append((r, c))
			words = words[1:]
			result = _exist(r - 1, c, words) \
					 or _exist(r, c + 1, words) \
					 or _exist(r + 1, c, words) \
					 or _exist(r, c - 1, words)
			queue.pop()
			return result

		if not board or not board[0]:
			return False

		b_count = collections.Counter([x for row in board for x in row])
		w_count = collections.Counter([x for x in word])
		for k, v in w_count.items():
			if b_count[k] < v:
				return False

		row = len(board)
		col = len(board[0])
		queue = []
		for r in range(row):
			for c in range(col):
				if board[r][c] == word[0] and _exist(r, c, word):
					return True
		return False


if __name__ == "__main__":

	board = [
		['A', 'B', 'C', 'E'],
		['S', 'F', 'C', 'S'],
		['A', 'D', 'E', 'E']
	]
	inputs = [
		["ABCCED"],
		["SEE"],
		["ABCB"]
	]
	targets = [
		True,
		True,
		False
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.exist(board, *i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
