#!/usr/bin/python3
"""
This class contains the entry point of the command interpreter
"""

import cmd
from importlib import import_module


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
        validated = self.validate_arg(arg, False)
        if validated:
            args = arg.split()
            module_path = self.get_module_path(args[0])
            module = import_module(module_path)
            instance = getattr(module, args[0])()
            instance.save()
            print(instance.id)
            return False
    
    def get_module_path(self, classname):
        classpaths = {"BaseModel": "base_model"}
        return "models.{}".format(classpaths[classname])
    
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
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
