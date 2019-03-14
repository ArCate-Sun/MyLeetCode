"""
Question:
	Increasing Triplet Subsequence
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
"""

from typing import List
import sys


class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		"""
		思路:
			遍历数组 nums,
			由 min 记录当前遇到的最小值,
			由 mid 记录当前遇到的次小值,
			min 和 mid 组成一个两元素的递增序列.
			若当前遍历的值大于 mid,
			则 min, mid 和当前值可组成一个三元素的递增序列.
		:param nums:
		:return:
		"""
		min = mid = sys.maxsize
		for n in nums:
			if min >= n:
				min = n
			elif mid >= n:
				mid = n
			else:
				return True
		return False


if __name__ == "__main__":

	demos = [
		[1, 2, 3, 4, 5],
		[5, 4, 3, 2, 1]
	]
	results = [
		True,
		False
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.increasingTriplet(*demo)
		else:
			output = s.increasingTriplet(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
