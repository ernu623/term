

def __init__(*argv):
	"""
		if one is a normal person, and if 0,
		then a root person
	"""
	print('root' if argv[0] == 2 else 'user')
	return 0
