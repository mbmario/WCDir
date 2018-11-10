class WCDirReader:

	def __init__(self, path):
		import os

		# check path is valid
		if (not os.path.exists(path)):
			raise NotADirectoryError()

		self.path = path
		self.wordcount_dict = {}

	def get_wordcount_dict(self):
		return self.wordcount_dict

	def read_files(self):
		import os

		# set the output and call the helper
		output = ""
		wordcount_dict = {}

		for root, dirs, files in os.walk(self.path, topdown=True):
			for name in files:

				print(os.path.join(root, name))
				wordcount_dict[name] = 0

		self.wordcount_dict = wordcount_dict

	def count_words(file):


		file = open(file, "r", encoding="utf-8-sig")

		return 28



	
