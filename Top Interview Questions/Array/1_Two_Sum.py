"""
Question:
	Two Sum
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
"""


class Solution:
	def find_from_sorted_nums(self, nums, n, start=None, stop=None):
		"""
		从有序数列中寻找指定值, 返回其下标
		:param nums:
		:return:
		"""

		start = 0 if start is None else start
		stop = len(nums) - 1 if stop is None else stop

		while start <= stop:
			i = (start + stop) // 2
			if nums[i] < n:
				start = i + 1
			elif nums[i] > n:
				stop = i - 1
			else:
				return i

		return None

	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		sorted_nums = list(nums)
		sorted_nums.sort()
		for i in range(len(nums)):
			j = self.find_from_sorted_nums(sorted_nums, target - sorted_nums[i], i + 1)
			if j is not None:
				m = nums.index(sorted_nums[i])
				if sorted_nums[i] == sorted_nums[j]:
					n = nums.index(sorted_nums[j], m + 1)
				else:
					n = nums.index(sorted_nums[j])
				return [m, n]


if __name__ == "__main__":
	s = Solution()

	nums = [2, 7, 11, 15]
	target = 9
	print("Input: nums = %s, target = %s" % (nums, target))
	output = s.twoSum(nums, target)
	print("Output: %s" % output)
