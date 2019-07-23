"""
Question:
	Search for a Range
See:
	https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:

		if not nums:
			return [-1, -1]

		l = 0
		r = len(nums) - 1
		mid = -1
		while l <= r:
			mid = (l + r) // 2
			if nums[mid] == target:
				break
			elif nums[mid] > target:
				r = mid - 1
			else:
				l = mid + 1

		l, r = -1, -1
		for i in range(mid, -1, -1):
			if nums[i] == target:
				l = i
			else:
				break
		for i in range(mid, len(nums)):
			if nums[i] == target:
				r = i
			else:
				break
		return [l, r]

	def searchRange2(self, nums: List[int], target: int) -> List[int]:
		if target in nums:
			start = nums.index(target)
			end = -1
			for i in range(start, len(nums)):
				if nums[i] == target:
					end = i
			return [start, end]
		else:
			return [-1, -1]


if __name__ == "__main__":

	inputs = [
		[[5, 7, 7, 8, 8, 10], 8],
		[[5, 7, 7, 8, 8, 10], 6],
		[[1, 3], 1]
	]
	targets = [
		[3, 4],
		[-1, -1],
		[0, 0]
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.searchRange(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
