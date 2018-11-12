import unittest
from WCDirReader import *

class WCDirTest(unittest.TestCase):

	def test_init(self):
		# tests incorrect init

		path = "/xxx/"
		with self.assertRaises(NotADirectoryError):
			reader = WCDirReader(path)


	def test_open_zips(self):
		# Copies a multi level directory with zips.
		# Walks the new directory, asserting for several zip files that their old zip is there,
		# 	the new zips are there with nonempt files, and it is registered.
		# Deletes copied dir
		pass


	def test_close_zips(self):
		# Given a directory with identical opened and zipped files, and a  registry. Assert it deletes the open ones and leaves a shorter registry
		pass

	def test_count_words(self):
		# counts words in

		path = "./test_dirs/testdir_nozips/"
		reader = WCDirReader(path)
		reader.read_files()
		wordcount_dict_result = reader.get_wordcount_dict()

		wordcount_dict_desired = {
			"aaa.txt": 10, "bbb.txt":0, "cccc.txt":2, "ddddd.txt":0, "z_grandchild.txt":0
		}
		self.assertDictEqual(wordcount_dict_result, wordcount_dict_desired)



	def test_quick_hist(self):
		pass

if __name__ == '__main__' :
	unittest.main()




