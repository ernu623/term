
def main(argv):
    try:
        with open(argv[1][1], 'r') as file:
            print('this file already exists')
    except IndexError:
        print('touch [file]')
    except FileNotFoundError:
        with open(argv[1][1], 'w'):
            pass
    except PermissionError:
        print('permission denied')
    except:
        return 1
    finally:
        return 0


def __init__(*argv):
    '''
        this crate file
        touch [file]
    '''
    return main(argv)

