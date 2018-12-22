"""
Question:
	Intersection of Two Arrays II
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
"""


class Solution:
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""

		# 对 nums1, nums2 排序
		nums1.sort()
		nums2.sort()


		result = []
		i = j = 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] == nums2[j]:
				# 如果 nums[i] == nums2[j],
				# 则 nums[i] 为两数组中共有的元素,
				# 要将 nums[i] 添加进交集集合中
				result.append(nums1[i])
				i += 1
				j += 1
			elif nums1[i] > nums2[j]:
				# 如果 nums[i] > nums2[j],
				# 则下次应用 nums[i] 与 nums2[j + 1] 比较
				j += 1
			else:
				# 如果 nums[i] < nums2[j],
				# 则下次应用 nums[i + 1] 与 nums2[j] 比较
				i += 1

		return result


if __name__ == "__main__":
	s = Solution()

	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2]
	print("Input: nums1 = %s, nums2 = %s" % (nums1, nums2))
	output = s.intersect(nums1, nums2)
	print("Output: %s" % output)

	nums1 = [4, 9, 5]
	nums2 = [9, 4, 9, 8, 4]
	print("Input: nums1 = %s, nums2 = %s" % (nums1, nums2))
	output = s.intersect(nums1, nums2)
	print("Output: %s" % output)
