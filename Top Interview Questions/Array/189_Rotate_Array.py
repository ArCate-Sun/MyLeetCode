"""
Question:
	Rotate Array
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
"""


class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		rotate_arr = nums[-k % len(nums):]
		nums[len(rotate_arr):] = nums[:-len(rotate_arr)]
		nums[:len(rotate_arr)] = rotate_arr


if __name__ == "__main__":

	s = Solution()

	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	print("Input: %s and k = %s" % (nums, k))
	s.rotate(nums, k)
	print("Output: %s" % nums)

	nums = [-1, -100, 3, 99]
	k = 2
	print("Input: %s and k = %s" % (nums, k))
	s.rotate(nums, k)
	print("Output: %s" % nums)

	nums = [1]
	k = 0
	print("Input: %s and k = %s" % (nums, k))
	s.rotate(nums, k)
	print("Output: %s" % nums)

	nums = [1, 2]
	k = 3
	print("Input: %s and k = %s" % (nums, k))
	s.rotate(nums, k)
	print("Output: %s" % nums)
