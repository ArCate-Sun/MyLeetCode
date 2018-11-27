"""
Question:
	Contains Duplicate
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
"""


class Solution:
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""

		return len(nums) != len(set(nums))


if __name__ == "__main__":

	s = Solution()

	nums = [1, 2, 3, 1]
	print("Input: %s" % nums)
	result = s.containsDuplicate(nums)
	print("Output: %s" % result)

	nums = [1, 2, 3, 4]
	print("Input: %s" % nums)
	result = s.containsDuplicate(nums)
	print("Output: %s" % result)

	nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
	print("Input: %s" % nums)
	result = s.containsDuplicate(nums)
	print("Output: %s" % result)
