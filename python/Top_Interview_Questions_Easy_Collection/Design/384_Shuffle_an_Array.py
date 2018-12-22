"""
Question:
	Shuffle an Array
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
"""
import random


class Solution:
	_nums = None

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self._nums = nums

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self._nums

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""

		return sorted(self._nums, key=lambda x: random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == "__main__":
	nums = [1, 2, 3]
	obj = Solution(nums)
	param_1 = obj.reset()
	param_2 = obj.shuffle()
