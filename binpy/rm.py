

def __init__(*argv):
	"""
		is remove file
		rm [file]
	"""
	import os
	try:
		os.remove(argv[1][1])
	except FileNotFoundError:
		print('this no file')
	except IndexError:
		print('no file')
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		del os
		return 0

