
def main(argv):
	"""
		Opens a file in python format and completes
		open [python file]
	"""

	try:
		imp = __import__(f'{argv[1][1]}', fromlist={'__init__'})
		imp.__init__()
	except IndexError:
		print('is no file')
	except ModuleNotFoundError:
		print('this no file')
	except NameError:
		print('is no file')
	except TypeError:
		print('is no init')
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		return 0

def __init__(*argv):
	return main(argv)
