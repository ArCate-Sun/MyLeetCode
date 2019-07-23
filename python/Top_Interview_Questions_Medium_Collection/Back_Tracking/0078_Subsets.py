"""
Question:
	Subsets
See:
	https://leetcode.com/problems/subsets/
"""
from typing import Set, List
from common.verification import Verification


class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		res = [[]]
		for n in nums:
			for i in range(len(res)):
				res.append(res[i] + [n])
		return res


if __name__ == "__main__":

	inputs = [
		[[1, 2, 3]]
	]
	targets = [
		[
			[3],
			[1],
			[2],
			[1, 2, 3],
			[1, 3],
			[2, 3],
			[1, 2],
			[]
		]
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.subsets(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
