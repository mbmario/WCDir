import unittest
from WCDirReader import *

class WCDirTest(unittest.TestCase):

	def test_bad_path(self):

		path = "/xxx/"
		with self.assertRaises(NotADirectoryError):
			reader = WCDirReader(path)

	def test_good_path(self):
		import pdb
		pdb.set_trace()

		path = "./test_dirs/testdir_empty/"
		reader = WCDirReader(path)
		reader.read_files()
		wordcount_dict_result = reader.get_wordcount_dict()

		wordcount_dict_desired = {
			"aaa.txt":0, "bbb.txt":0, "cccc.txt":0, "ddddd.txt":0, "z_grandchild":0
		}
		self.assertDictEqual(wordcount_dict_result, wordcount_dict_desired)

	def test_count_words(self):
		import os

		file1_wc_desired = 28
		file1 = "aaa.txt"
		path = "./test_dirs/testdir_empty/"

		reader = WCDirReader(path)
		file1_wc_actual = reader.count_words(file1)

		self.assertEqual(file1_wc_desired, file1_wc_actual)




if __name__ == '__main__' :
	unittest.main()




