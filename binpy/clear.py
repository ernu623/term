
def __init__(*argv):
	"""
		Clear screen on console
	"""
	import os
	if os.system('cls' if os.name == 'nt' else 'clear') == 0:
		del os
		return 0
	return 1
	
