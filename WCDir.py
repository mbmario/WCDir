class WCDir:


	def WCDir_main (self, path):
		import os

		# check path is valid
		if (not os.path.exists(path)):
			raise NotADirectoryError()

		# set the output and call the helper
		output = ""
	
		self.WCDir_helper(path)


	def WCDir_helper(path):
		return True




		



	
