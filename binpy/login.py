
def main():
	from .__main import main
	main()
	del main

def __init__(*argv):
	"""
		login from programs
	"""
	main()
	return 0

