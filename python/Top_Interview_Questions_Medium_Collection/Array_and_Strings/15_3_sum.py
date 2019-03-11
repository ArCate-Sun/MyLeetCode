"""
Question:
	3 Sum
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
"""


class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		if not nums:
			return []

		result = []

		# statistics appearance counts of the numbers in nums
		count_dict = {}
		for n in nums:
			count_dict[n] = count_dict.get(n, 0) + 1

		# if 0 appears more than 2 times in nums
		if count_dict.get(0, 0) > 2:
			result.append([0, 0, 0])

		negatives = [n for n in count_dict.keys() if n < 0]
		positives = [n for n in count_dict.keys() if n > 0]

		for n in negatives:
			for p in positives:
				need = - (n + p)
				if need == n and count_dict[n] > 1:
					result.append([n, n, p])
				elif need == p and count_dict[p] > 1:
					result.append([n, p, p])
				elif n < need < p and need in count_dict:
					result.append([n, need, p])
		return result

	def threeSum_2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		result = []
		nums.sort()
		for i in range(len(nums) - 2):

			if i > 0 and nums[i] == nums[i - 1]:
				continue

			if nums[i] > 0:
				break

			left, right = i + 1, len(nums) - 1
			while right > left:
				s = nums[i] + nums[left] + nums[right]
				if s < 0:
					left += 1
				elif s > 0:
					right -= 1
				else:
					result.append([nums[i], nums[left], nums[right]])
					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
						right -= 1
					left += 1
					right -= 1
		return result


if __name__ == "__main__":

	demos = [
		[-1, 0, 1, 2, -1, -4],
		[0, 0, 0],
		[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
	]
	results = [
		[
			[-1, -1, 2],
			[-1, 0, 1]
		],
		[
			[0, 0, 0]
		],
		[[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.threeSum(*demo)
		else:
			output = s.threeSum(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()

