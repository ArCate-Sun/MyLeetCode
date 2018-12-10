import os

ads = ["logo.png", "www.situku.com", "更多福利必读"]


def clear_ads(dir_path):
	for f1 in os.listdir(dir_path):
		if f1.startswith("."):
			continue
		if os.path.isfile(os.path.join(dir_path, f1)):
			for ad in ads:
				if ad in f1:
					os.remove(os.path.join(dir_path, f1))
		if os.path.isdir(os.path.join(dir_path, f1)):
			clear_ads(os.path.join(dir_path, f1))
			print("[D] %s" % os.path.join(dir_path, f1))


if __name__ == "__main__":
	base_path = "/Users/acat/Desktop/tmp/蛋黄姬/"
	clear_ads(base_path)


# if __name__ == "__main__":
# 	base_path = "/Users/acat/Desktop/tmp/镜颜欢/"
# 	for fname in os.listdir(base_path):
#
# 		f1 = fname[4:]
# 		print(os.path.join(base_path, f1))
# 		if " [" in f1:
# 			f1 = f1[:f1.find(" [")]
# 			print(os.path.join(base_path, f1))
# 		if " (" in f1:
# 			f1 = f1[:f1.find(" (")]
# 			print(os.path.join(base_path, f1))
# 		print()
#
# 		#
# 		os.rename(os.path.join(base_path, fname), os.path.join(base_path, f1))