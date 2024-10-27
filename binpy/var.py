

def return_var(var_, t=False):
    from .__var import var
    var1 = var().all_var.get(var_)
    del var
    print(var1)
    if t:
        return type(var1)
    return var1

def create_var(var_, change: list):
    if not len(change) > 1:
        change = ' '.join(change)
    from .__var import var
    var().all_var[var_] = change
    del var

def __init__(root, argv):
    if len(argv) > 2:
        if argv[2] == '=':
            create_var(argv[1], argv[3:])
            return 0
        elif argv[2] == '-t':
            print(argv[1])
            r = return_var(argv[1], t=True)
            return r
        else:
            return 1

    elif len(argv) > 1:
        var = return_var(argv[1])
        return var

