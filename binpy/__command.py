import os
import importlib


def if_user(tmp, root):
    """
        Executes user-level command based on input.

        Parameters:
            - tmp (list): List of command and arguments split from user input.
    """

    if tmp:
        try:
            # Attempt to import and initialize module based on user command
            mod = importlib.import_module(f'binpy.{tmp[0].lower()}', package='__init__')
            result = mod.__init__(root, tmp)
            del mod # Initialize module with user-level privilege (2)
        except ModuleNotFoundError:
            print(f'no \'{tmp[0]}\' command')
        except Exception as e:
            print(f'this command \'{tmp[0]}\' is not fixed\nError:\n{e}')		



class input_all:
    """
        Class to handle input commands and execute corresponding actions.
    """

    def __init__(self, command, root):
        """
            Initializes InputAll instance with a command.

            Parameters:
                - command (str): Input command string.
        """
        self.command = command
        self.tmp = self.command.split()
        self.root = root

    def command_user(self):
        """
            Executes root-level command based on the stored command string.
        """
    
        if_user(self.tmp, self.root)
