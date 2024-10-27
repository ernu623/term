
def __init__(*argv):
	"""
		look at the text file
		cat [file]
	"""
	try:
		with open(argv[1][1], 'r') as file:
			print(file.read())
	except IndexError:
		print('no file')
	except FileNotFoundError:
		print('this no file')
	except UnicodeDecodeError:
		print('this is no text file')
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		return 0

