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

		single_number = 0
		for num in nums:
			single_number ^= num
		return single_number


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
