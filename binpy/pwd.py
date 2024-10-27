def __init__(*argv):
	"""
		displays the current working directory
	"""
	import os
	print(os.getcwd())
	del os
	return 0
