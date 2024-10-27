
def __init__(*argv):
	"""
		this is help
		help [command]
	"""
	import importlib
	
	try:
		mod = importlib.import_module(argv[1][1], package='__init__')
		print(help(str(argv[1][1])))
		del mod
	except IndexError:
		print('help (command)')
	except PermissionError:
		print('permission denied')
	except FileNotFoundError:
		print('no command')
	except UnboundLocalError:
		print('no command')
	except:
		return 1
	finally:
		del importlib
		return 0

