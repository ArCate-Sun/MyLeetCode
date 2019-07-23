"""
Question:
	Search in Rotated Sorted Array
See:
	https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def search(self, nums: List[int], target: int) -> int:

		def binary_search(nums, target, start, stop):
			l, r = start, stop
			mid = -1
			while l <= r:
				mid = (l + r) // 2
				if nums[mid] < target:
					l = mid + 1
				elif nums[mid] > target:
					r = mid - 1
				else:
					break
			if nums[mid] == target:
				return mid
			else:
				return -1

		if not nums:
			return -1

		# 二分查找最小值
		l, r = 0, len(nums) - 1
		while l < r - 1:
			mid = (l + r) // 2
			if nums[mid] >= nums[l]:
				l = mid
			elif nums[mid] <= nums[r]:
				r = mid
		pivot = r
		largest = l

		if nums[0] <= target <= nums[largest]:
			return binary_search(nums, target, 0, largest)
		elif nums[pivot] <= target <= nums[-1]:
			return binary_search(nums, target, pivot, len(nums) - 1)
		else:
			return -1


if __name__ == "__main__":

	inputs = [
		[[4, 5, 6, 7, 0, 1, 2], 0],
		[[4, 5, 6, 7, 0, 1, 2], 3],
		[[3, 1], 1],
		[[1, 3, 5], 3],
		[[4, 5, 6, 7, 0, 1, 2], 1]
	]
	targets = [
		4,
		-1,
		1,
		1,
		5
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.search(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
