#!/usr/bin/python3
"""
This class contains the entry point of the command interpreter
"""

import cmd
from importlib import import_module
from ast import literal_eval
import shlex
import models


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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        validated = self.validate_arg(arg, True)
        if validated:
            args = arg.split()
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                module_path = self.get_module_path(args[0])
                module = import_module(module_path)
                value = models.storage.all()[key]
                instance = getattr(module, args[0])(**value)
                print(instance)
            else:
                print("** no instance found **")
        return False

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        validated = self.validate_arg(arg, True)
        if validated:
            args = arg.split()
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
        return False

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        args = arg.split()
        instances = []
        if len(args) == 0:
            instance_dict = models.storage.all().copy()
            for key, value in instance_dict.items():
                classname = key.split(".")[0]
                module_path = self.get_module_path(classname)
                module = import_module(module_path)
                instance = getattr(module, classname)(**value)
                instances.append(str(instance))
        else:
            validated = self.validate_arg(arg, False)
            if validated:
                instance_dict = models.storage.all().copy()
                for key, value in instance_dict.items():
                    classname = key.split(".")[0]
                    if classname == args[0]:
                        module_path = self.get_module_path(classname)
                        module = import_module(module_path)
                        instance = getattr(module, classname)(**value)
                        instances.append(str(instance))
            else:
                return False
        print(instances)
        return False

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        validated = self.validate_arg(arg, True)
        if validated:
            args = shlex.split(arg)
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    module_path = self.get_module_path(args[0])
                    module = import_module(module_path)
                    # models.storage.all()[key][args[2]] = args[3].strip('\"')
                    # models.storage.save()
                    # self.do_show("{} {}".format(args[0], args[1]))
                    value = models.storage.all()[key]
                    instance = getattr(module, args[0])(**value)
                    try:
                        setattr(instance, args[2],
                                literal_eval(args[3]))
                    except ValueError, SyntaxError:
                        setattr(instance, args[2],
                                args[3])
                    instance.save()
                    print(instance)
                else:
                    print("** no instance found **")
        return False

    def get_module_path(self, classname):
        classpaths = {"BaseModel": "base_model", "User": "user"}
        return "models.{}".format(classpaths[classname])

    def validate_arg(self, arg, check_for_id):
        """
        validate argument string
        Args:
            arg (string): argument string
            check_for_id (bool): check if id is present in arg
        """
        classnames = ["BaseModel", "User"]
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
            # check if instance exists for id
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
