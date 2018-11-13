#!/usr/local/bin/python3

from WCDirReader import WCDirReader
import sys

if (len(sys.argv) == 1):
    path = "./test_dirs/testdir_all"
else:
    path = sys.argv[1]

reader = WCDirReader(path)
reader.open_zips()
reader.count_words()
reader.close_zips()
reader.quick_hist()