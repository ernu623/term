import os

class passwd_login:
    """
    
    """
    def __init__(self):
        self.file = './binpy/password/password.txt'
        self.user_passwd = {}
        self.user_root = {}

        super().__init__()


    def load_passwd(self):
        if not os.path.isfile(self.file):
            return 
        with open(self.file, 'r', encoding='utf-8') as f:
            for st in f:
                if len(st.split()) == 3:
                    self.user_passwd[st.split()[0]] = str(st.split()[1])
                    self.user_root[st.split()[0]] = str(st.split()[2])
                else:
                    return 

def main():
    print(passwd_login().load_passwd())

if __name__ == '__main__':
    main()

