from .__passwd import*

def re():
    login()

def login():
    """
    """
    
    try:
        user = str(input('login: '))

        passwd = str(input('password: '))
    except KeyboardInterrupt:
        print('\n')
       
    t = passwd_login()
    t.load_passwd()
    u = t.user_passwd.get(user)

    if u == passwd:
        return t.user_root[user]
    return -1


if __name__ == '__main__':
    print(login())

