"""
Question:
	Maximum Subarray
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
"""


class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		max_sum = None
		tmp_sum = 0
		for num in nums:
			tmp_sum += num
			print(num, tmp_sum)
			if max_sum is None or tmp_sum > max_sum:
				max_sum = tmp_sum
			if tmp_sum < 0:
				tmp_sum = 0

		return max_sum


if __name__ == "__main__":
	s = Solution()

	input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print("Input: %s" % input)
	output = s.maxSubArray(input)
	print("Output: %s" % output)

