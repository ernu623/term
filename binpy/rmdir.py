

def __init__(*argv):
	'''
		is remove directory
		rm [dir]
	'''
	import os
	try:
		os.rmdir(argv[1][1])
	except FileNotFoundError:
		print('no file')
	except IndexError:
		print('no file')
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		del os
		return 0
