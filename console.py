#!/usr/bin/python3
"""
    Console module
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
        Define HBNBCommand class for interactive console
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
            Command to quit from the command interpreter
        """
        return True

    def do_EOF(self, args):
        """
            Command to exit from the command interpreter
        """
        return True

    def help_quit(self):
        """
            Command to show quit documentation
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """
            Command do nothing when emptyline appears
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
