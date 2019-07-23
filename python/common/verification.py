class Verification:
	def __init__(self, inputs: list, answers: list, targets: list):
		self.__inputs = inputs
		self.__answers = answers
		self.__targets = targets

		if len(targets):
			self.__target_type = type(targets[0])
		else:
			self.__target_type = None

	def __verify_item(self, answer, target, unordered: bool = True, judge_func = None) -> bool:

		target_type = self.__target_type

		if type(answer) != target_type:
			return False

		if judge_func:
			return judge_func(answer, target)

		if target_type == set:
			return not answer.symmetric_difference(target)

		elif target_type == list:
			if unordered:
				return sorted(answer) == sorted(target)
			else:
				if len(answer) != len(target):
					return False
				for t in target:
					if t not in answer or answer.count(t) != target.count(t):
						return False

		elif target_type == dict:
			for k in target.keys():
				if answer[k] != target[k]:
					return False

		else:
			return answer == target

	def verify(self, unordered: bool = True, judge_func = None) -> bool:
		inputs = self.__inputs
		answers = self.__answers
		targets = self.__targets

		if len(answers) != len(targets):
			print("\033[0;31mANSWERS: %s\033[0m" % str(answers))
			print("\033[0;36mEXPECTS: %s\033[0m" % str(targets))
			print()
			return

		for input, answer, target in zip(inputs, answers, targets):

			print("INPUT: %s" % str(input))
			if self.__verify_item(answer, target, unordered=unordered, judge_func=judge_func):
				print("\033[0;32mANSWER: %s\033[0m" % str(target))
			else:
				print("\033[0;31mANSWER: %s\033[0m" % str(answer))
				print("\033[0;36mEXPECT: %s\033[0m" % str(target))
			print()