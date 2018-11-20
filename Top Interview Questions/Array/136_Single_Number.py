"""
Question:
	Single Number
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
"""


class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		nums.sort()
		for i in range(1, len(nums), 2):
			if nums[i - 1] != nums[i]:
				return nums[i - 1]
		else:
			return nums[-1]


if __name__ == "__main__":
	s = Solution()

	nums = [2, 2, 1]
	print("Input: %s" % nums)
	single_number = s.singleNumber(nums)
	print("Output: %s" % single_number)

	nums = [4, 1, 2, 1, 2]
	print("Input: %s" % nums)
	single_number = s.singleNumber(nums)
	print("Output: %s" % single_number)
