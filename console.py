#!/usr/bin/python3
"""
This class contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    entry point of the command interpreter:
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        "EOF to exit the program"
        return True

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
