"""
Question:
	Plus One
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
"""


class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""

		for i in range(1, len(digits) + 1):
			if digits[-i] == 9:
				digits[-i] = 0
			else:
				digits[-i] += 1
				is_carry = False
				break
		else:
			digits.insert(0, 1)

		return digits


if __name__ == "__main__":
	s = Solution()

	nums = [1, 2, 3]
	print("Input: %s" % nums)
	output = s.plusOne(nums)
	print("Output: %s" % output)

	nums = [4, 9, 5]
	print("Input: %s" % nums)
	output = s.plusOne(nums)
	print("Output: %s" % output)

	nums = [0]
	print("Input: %s" % nums)
	output = s.plusOne(nums)
	print("Output: %s" % output)

	nums = [9, 9, 9]
	print("Input: %s" % nums)
	output = s.plusOne(nums)
	print("Output: %s" % output)
