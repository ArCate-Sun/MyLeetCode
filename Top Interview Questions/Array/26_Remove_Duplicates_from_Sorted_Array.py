"""
Question:
	Remove Duplicates from Sorted Array
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = 0

		len_nums = len(nums)
		if len_nums > 0:

			prev_v = nums[0]
			length = 1

			for i in range(1, len_nums):
				if nums[i] != prev_v:
					prev_v = nums[length] = nums[i]
					length += 1
			del nums[length:len_nums]

		return length


if __name__ == "__main__":
	s = Solution()

	nums = [1, 1, 2]
	print("Input: %s" % nums)
	length = s.removeDuplicates(nums)
	print("Output: %s, %s" % (nums, length))

	nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	print("Input: %s" % nums)
	length = s.removeDuplicates(nums)
	print("Output: %s, %s" % (nums, length))
