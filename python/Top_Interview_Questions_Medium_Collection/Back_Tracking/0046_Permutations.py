"""
Question:
	Permutations
See:
	https://leetcode.com/problems/permutations/
"""
from typing import Set, List
from common.verification import Verification


class Solution:
	permutations = {}

	def permute(self, nums: List[int]) -> List[List[int]]:

		if not nums:
			return []

		if len(nums) == 1:
			return [[nums[0]]]

		nums = tuple(sorted(nums))
		if nums in Solution.permutations:
			return Solution.permutations[nums]

		permutations = []
		for n in nums:
			tmp_nums = list(nums)
			tmp_nums.remove(n)
			suffix_permutations = self.permute(tmp_nums)
			for p in suffix_permutations:
				permutations.append([n] + p)
		Solution.permutations[nums] = permutations

		return Solution.permutations[nums]


if __name__ == "__main__":

	inputs = [
		[[1, 2, 3]]
	]
	targets = [
		[
			[1, 2, 3],
			[1, 3, 2],
			[2, 1, 3],
			[2, 3, 1],
			[3, 1, 2],
			[3, 2, 1]
		]
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.permute(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
