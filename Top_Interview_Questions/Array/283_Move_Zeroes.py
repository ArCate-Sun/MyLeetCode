"""
Question:
	Move Zeroes
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
"""


class Solution:
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		length = len(nums)
		i = 0
		while i < length:

			if nums[i] == 0:
				nums.pop(i)
				nums.append(0)
				length -= 1
			else:
				i += 1


if __name__ == "__main__":
	s = Solution()

	nums = [0, 1, 0, 3, 12]
	print("Input: %s" % nums)
	s.moveZeroes(nums)
	print("Output: %s" % nums)



