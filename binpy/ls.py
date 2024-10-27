def __init__(*argv):
	"""
		View all files directory
	"""
	import os
	
	try:
		for i in os.listdir():
			print(i)
		else:
			del os
	except PermissionError:
		print('permission denied')
	except:
		return 1
	finally:
		return 0
