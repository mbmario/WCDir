import unittest
from WCDirReader import *

class WCDirTest(unittest.TestCase):

	def test_init(self):
		# tests incorrect init, with bad path

		path = "/xxx/"
		with self.assertRaises(NotADirectoryError):
			reader = WCDirReader(path)


	def test_open_zips(self):
		# Copies a multi level directory with zips.
		# Walks the new directory, asserting for several zip files that their old zip is there,
		# 	the new zips are there with nonempty files, and it is registered.
		# Deletes copied dir

		import os
		import shutil

		# copy dir to prevent corruption
		source = "./test_dirs/testdir_zips"
		path = "./test_dirs/testdir_zips_copied"
		shutil.copytree(source, path)


		reader = WCDirReader(path)

		reader.open_zips()

		# check the files
		files_desired = [
			path + "/child_temp/cccc.txt",
			path + "/child_temp/grandchild/ddddd.txt"
		]

		for file in files_desired:
			self.assertTrue(os.path.isfile(file), "Extracted file not found")

		# check the registry
		temp_zips_actual = reader.temp_zips
		temp_zips_desired = [path + "/child_temp"]
		self.assertListEqual(temp_zips_actual, temp_zips_desired)

		shutil.rmtree(path) # TODO: execute in all cases


	def test_close_zips(self):
		# Given a directory with identical opened and zipped files, and a  registry. Assert it deletes the open ones and leaves a shorter registry

		import shutil
		import os

		# copy dir to prevent corruption
		source = "./test_dirs/testdir_zips_opened"
		path = "./test_dirs/testdir_zips_opened_copied"
		shutil.copytree(source, path)

		reader = WCDirReader(path)
		reader.temp_zips = [path + "/child_temp"]
		reader.close_zips()

		# check the file
		deleted_dir = path + "/child_temp"
		self.assertFalse(os.path.isdir(deleted_dir), "_temp was not deleted")

		# check the registry
		temp_zips_actual = reader.temp_zips
		temp_zips_desired = [path + "/child_temp"]
		self.assertListEqual(temp_zips_actual, temp_zips_desired)

		shutil.rmtree(path) # TODO: execute in all cases


	def test_count_words(self):
		# counts words in

		path = "./test_dirs/testdir_nozips/"
		reader = WCDirReader(path)
		reader.count_words()
		wordcount_dict_actual = reader.get_wordcount_dict()

		wordcount_dict_desired = {
			"one": 4, "two":4, "three":3, "four":2, "five":2,
			"six": 2, "seven": 1, "eiiiiiiiiiiight": 1
		}
		self.assertDictEqual(wordcount_dict_actual, wordcount_dict_desired)

if __name__ == '__main__' :
	import os
	os.chdir("/Users/Sargon/Marios_code/WCDir") # CHANGE HERE, TODO: env var or trick
	unittest.main()




