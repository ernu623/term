def __init__(*argv):
	"""
		is make directory 
		mkdir [dir]
	"""
	import os
	try:
		os.mkdir(argv[1][1])
	except IndexError:
		print('no file')
	except OSError:
		print('directory exists')
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		del os
		return 0
