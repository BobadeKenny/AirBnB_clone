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

    def do_create(self, arg):
        "Creates a new instance of class"
        args = self.validate_arg(arg, False)
    
    def validate_arg(self, arg, check_for_id):
        """
        validate argument string
        Args:
            arg (string): argument string
            check_for_id (bool): check if id is present in arg
        """
        classnames = ["BaseModel"]
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in classnames:
            print("** class doesn't exist **")
            return False
        if check_for_id:
            if len(args) < 2:
                print("** instance id missing **")
                return False
            #check if instance


if __name__ == '__main__':
    HBNBCommand().cmdloop()
