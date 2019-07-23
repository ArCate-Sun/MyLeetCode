"""
Question:
	Jump Game
See:
	https://leetcode.com/problems/jump-game/
"""
from typing import List
from common.verification import Verification


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		right = 0
		for i, n in enumerate(nums):
			if right < i:
				return False
			right = max(right, i + n)
			if right >= len(nums) - 1:
				return True
		return False


if __name__ == "__main__":

	inputs = [
		[[2, 3, 1, 1, 4]],
		[[3, 2, 1, 0, 4]],
		[[0]],
		[[3, 0, 8, 2, 0, 0, 1]]
	]
	targets = [
		True,
		False,
		True,
		True
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.canJump(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
