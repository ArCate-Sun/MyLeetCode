"""
Question:
	First Bad Version
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		l, r = 0, n

		while l <= r:
			mid = (l + r) // 2

			check_result = isBadVersion(mid), isBadVersion(mid + 1)
			if check_result == (False, True):
				return mid + 1
			elif check_result == (False, False):
				l = mid + 1
			else:
				r = mid - 1


def isBadVersion(version):
	# 从 2356 开始以后的版本是坏的
	return version >= 2356


if __name__ == "__main__":
	s = Solution()

	n = 6523
	print("Input: n = %s" % n)
	output = s.firstBadVersion(n)
	print("Output: %s" % output)
