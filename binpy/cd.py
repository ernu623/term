

def __init__(*argv):
	"""
		move directory
		cd [dir]
	"""

	import os

	try:
		os.chdir(argv[1][1])
	except IndexError:
		print(os.getcwd())
	except FileNotFoundError:
		print(f'no dir \'{argv[1][1]}\'')
	except PermissionError:
		print(f'permisson denied')
	except:
		return 1
	finally:
		del os
		return 0
