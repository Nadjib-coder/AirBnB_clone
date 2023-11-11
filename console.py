#!/usr/bin/python3
"""
This modual contains the HBNBCommand class that represants the HBNB console
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    This class for the hbnb console
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
        This method used to creat an instance from BaseModel class
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                name = f'{args[0]}.{args[1]}'
                a = 0
                for k in models.storage.all().keys():
                    if k == name:
                        print(models.storage.all()[k])
                        a = 1
                if a == 0:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        This method to Deletes an instance based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                name = f'{args[0]}.{args[1]}'
                a = 0
                for k in models.storage.all().keys():
                    if k == name:
                        a = 1
                        del models.storage.all()[k]
                        models.storage.save()
                        break
                if a == 0:
                    print("** no instance found **")

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()