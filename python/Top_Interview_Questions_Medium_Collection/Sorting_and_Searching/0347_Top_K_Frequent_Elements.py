"""
Question:
	Top K Frequent Elements
See:
	https://leetcode.com/problems/top-k-frequent-elements/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		counter = collections.Counter(nums)
		return heapq.nlargest(k, counter.keys(), key=counter.get)


if __name__ == "__main__":

	inputs = [
		[[1, 1, 1, 2, 2, 3], 2],
		[[1], 1],
		[[-1, -1], 1]
	]
	targets = [
		[1, 2],
		[1],
		[-1]
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.topKFrequent(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
