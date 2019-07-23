"""
Question:
	Merge Intervals
See:
	https://leetcode.com/problems/merge-intervals/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:

		if not intervals:
			return []

		intervals = sorted(intervals, key=lambda x: x[0])
		l, r = intervals[0]
		result = []
		for interval in intervals[1:]:
			if r < interval[0]:
				result.append([l, r])
				l, r = interval
			else:
				r = max(r, interval[1])
		result.append([l, r])
		return result


if __name__ == "__main__":

	inputs = [
		[[[1, 3], [2, 6], [8, 10], [15, 18]]],
		[[[1, 4], [4, 5]]],
	]
	targets = [
		[[1, 6], [8, 10], [15, 18]],
		[[1, 5]]
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.merge(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
