
def __init__(*argv):
    '''
    '''
    import importlib

    try:
        mod = importlib.__import__(f'binpy.{argv[1][1]}', fromlist=['__init__'])
        print(mod.__init__(str(argv[0]), argv[1][1:]))
        del mod
    except FileNotFoundError:
        print('no file')
    except Exception as e:
        print(f'post [command], Error:\n{e}')
        return 1
    return 0

    
