import unittest
from WCDir import *

class WCDir_test(unittest.TestCase):

	def test_bad_path(self):

		path = "/xxx/"
		with self.assertRaises(NotADirectoryError):
			WCDir.WCDir_main(WCDir, path)

if __name__ == '__main__' :
	unittest.main()




