"""
Question:
	Count and Say
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
"""


class Solution:
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""

		string = "1"
		for _ in range(n - 1):
			string = string\
				.replace("111", "ca")\
				.replace("222", "cb")\
				.replace("333", "cc")\
				.replace("11", "ba")\
				.replace("22", "bb")\
				.replace("33", "bc")\
				.replace("1", "11")\
				.replace("2", "12")\
				.replace("3", "13")\
				.replace("a", "1")\
				.replace("b", "2")\
				.replace("c", "3")
		return string

	def countAndSay2(self, n):
		"""
		:type n: int
		:rtype: str
		"""

		nums = [1]
		for _ in range(n - 1):
			i = 0
			while i < len(nums):
				count = 0
				for j in range(i, len(nums)):
					if nums[i] == nums[j]:
						count += 1
					else:
						break
				else:
					j += 1
				nums[i:j] = [count, nums[i]]
				i += 2
		return "".join([str(i) for i in nums])

	def countAndSay3(self, n):
		"""
		:type n: int
		:rtype: str
		"""

		string = "1"
		for _ in range(n - 1):
			tmp = ""
			i = 0
			for j in range(len(string)):
				if string[i] != string[j]:
					tmp = tmp + str(j - i) + string[i]
					i = j
			string = tmp + str(len(string) - i) + string[i]
		return string

if __name__ == "__main__":
	s = Solution()

	input = 1
	print("Input: %s" % input)
	output = s.countAndSay(input)
	print("Output: %s" % output)
