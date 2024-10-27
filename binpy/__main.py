from .__login_main import* # Importing the login function from the __login_main module 
from .__command import* # Importing the command_user and command_root functions from the __command module 


class login_all:
    def __init__(self):
        self.root = login()
        if self.root == -1:
            exit()
       
    def input_user(self):
        # Infinite loop for user command input
        while True:
            try:
                self.command = str(input('# ')) # Input command and strip extra spaces
                if not self.command.strip(): 
                    continue
            
                input_all(self.command, self.root).command_user()
            except KeyboardInterrupt:
                print('\n')
                exit()


def main():
    login_all().input_user()

