class WCDirReader:

	def __init__(self, path):
		import os
		from collections import Counter

		# check path is valid
		if (not os.path.exists(path)):
			raise NotADirectoryError()

		self.path = path
		self.wordcount_dict = Counter({})
		self.temp_zips = []

	def get_wordcount_dict(self):
		return self.wordcount_dict

	def open_zips(self):
		import zipfile
		import os

		# Going thru the path, will unzip zip files and register them
		for root, dirs, files in os.walk(self.path, topdown=True):


			for name in files:
				if (name[-4:] == ".zip"):

					# unzip to temp
					full_name = os.path.join(root, name)
					zip_ref = zipfile.ZipFile(full_name)
					zip_ref.extractall(root)

					extr_name = root + "/" + name[:-4]
					temp_name = root + "/" + name[:-4] + "_temp"
					os.rename(extr_name, temp_name)
					zip_ref.close()

					# register temp filenames
					self.temp_zips.append(temp_name)

	def close_zips(self):
		# Going thru the path, will delete the directories and un-register them
		import shutil

		for temp_dir in self.temp_zips:
			shutil.rmtree(temp_dir)



	def count_words(self):
		# going thru the files in the path,

		import os

		output = ""

		for root, dirs, files in os.walk(self.path, topdown=True):

			import pdb

			for name in files:

				full_name = os.path.join(root, name)

				# throw error for non-text files
				if (full_name[-4:] not in (".txt",  ".zip")):
					#raise FileNotFoundError("filetype not supported by WCDirReader")
					print(full_name + ": filetype not supported by WCDirReader")

				elif (full_name[-4:] == ".txt"):

					# merge counters
					file_wordcount_dict = self.file_counter(full_name)
					self.wordcount_dict = self.wordcount_dict + file_wordcount_dict



	def file_counter(self, file):
		# Given a file, returns how many words
		from collections import Counter
		import re

		file = open(file, "r", encoding="utf-8-sig")
		file_wordcount_dict = Counter({})

		# clean line-by-line
		for line in file.readlines():
			line = line.lower()
			line = re.sub(r'\W+', ' ', line)
			line_wordcount_dict = Counter(line.split())

			# small merge
			file_wordcount_dict = file_wordcount_dict + line_wordcount_dict

		return file_wordcount_dict


	def quick_hist(self):
		# Histogram of word counts
		import numpy as np
		import matplotlib.pyplot as plt
		from collections import Counter, OrderedDict

		if not self.wordcount_dict:
			raise ValueError("there are no processed files")

		sorted_wcd = OrderedDict(Counter(self.wordcount_dict).most_common())

		keys = sorted_wcd.keys()
		values = sorted_wcd.values()

		indexes = np.arange(len(keys))
		width = 1

		plt.bar(indexes, values, width)
		plt.title("Word Frequencies")
		plt.xticks(indexes + width * 0.5, keys, ha='right', rotation=45)

		plt.show()


	def to_db(self, connection):
		# writes wordcount_dict to some database with connection info
		# a good potential extension!
		pass
