class WCDirReader:

	def __init__(self, path):
		import os

		# check path is valid
		if (not os.path.exists(path)):
			raise NotADirectoryError()

		self.path = path
		self.wordcount_dict = {}
		self.temp_zips = []

	def get_wordcount_dict(self):
		return self.wordcount_dict

	def open_zips(self):
		# Going thru the path, will unzip zip files and register them
		pass

	def close_zips(self):
		# Going thru the path, will delete the directories and un-register them
		pass

	def count_words(self):
		import os

		# set the output and call the helper
		output = ""
		wordcount_dict = {}

		for root, dirs, files in os.walk(self.path, topdown=True):
			for name in files:

				full_name = os.path.join(root, name)

				# throw error for non-text files
				if (full_name[-4:] is not ".txt"):
					raise FileNotFoundError("filetype not supported by WCDirReader")
				wordcount_dict[name] = self.file_counter(full_name)

		self.wordcount_dict = wordcount_dict

	def file_counter(file):
		# Given a file, returns how many words

		file = open(file, "r", encoding="utf-8-sig")

		return 28

	def quick_hist(self):
		# Histogram of word counts
		# throws some error if there is no data
		pass

	def to_sql(self, connection):
		# writes wordcount_dict to sql with connection info
		pass



	
