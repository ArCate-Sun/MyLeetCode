"""
Question:
	Missing Number
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
"""


class Solution:
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		return (len(nums) * (len(nums) + 1)) / 2 - sum(nums)


if __name__ == "__main__":

	demos = [[3, 0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]]
	results = [2, 8]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.missingNumber(*demo)
		else:
			output = s.missingNumber(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
