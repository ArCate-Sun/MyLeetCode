"""
Question:
	Reverse Bits
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
"""


class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		b = bin(n)[:1:-1]
		if len(b) < 32:
			b += "0" * (32 - len(b))
		return int(b, 2)



if __name__ == "__main__":

	demos = [43261596, 4294967293]
	results = [964176192, 3221225471]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.reverseBits(*demo)
		else:
			output = s.reverseBits(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
