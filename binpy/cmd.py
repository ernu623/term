
def __init__(*argv):
	import os
	if os.system('cmd' if os.name == 'nt' else 'termial') == 0:
		del os
		return 0
	return 1
