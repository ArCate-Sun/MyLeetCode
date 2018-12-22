"""
Question:
	Merge Sorted Array
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
"""


class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""

		end = m + n - 1
		m -= 1
		n -= 1
		while m >= 0 and n >= 0:
			if nums1[m] >= nums2[n]:
				nums1[end] = nums1[m]
				m -= 1
			else:
				nums1[end] = nums2[n]
				n -= 1
			end -= 1

		if n >= 0:
			nums1[:n + 1] = nums2[:n + 1]


if __name__ == "__main__":
	s = Solution()

	nums1 = [1, 2, 3, 0, 0, 0]
	m = 3
	nums2 = [2, 5, 6]
	n = 3
	print("Input: nums1 = %s, m = %s, nums2 = %s, n = %s" % (nums1, m, nums2, n))
	output = s.merge(nums1, m, nums2, n)
	print("Output: %s" % output)
