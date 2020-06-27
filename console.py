#!/usr/bin/python3
""" HBnB Console """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBnB Command interpreter """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """ Quit command to exit program """
        return True

    def do_EOF(self, args):
        """ EOF command to exit progam """
        return True

    def emptyline(self):
        """ Empty Line doesn't do anything """
        pass

    def do_create(self, args):
        """ Create new instance of the class """
        if len(args) == 0:
            print("** class name missing **")
        elif not args == "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        """ Show string representation """
        command = args.split(" ")
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not command[0] == "BaseModel":
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) in objects:
            print(objects["{}.{}".format(command[0], command[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroy Deletes an instance based on the class name """
        command = args.split(" ")
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not command[0] == "BaseModel":
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) in objects:
            del objects["{}.{}".format(command[0], command[1])]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances """
        valshow = storage.all().values()
        allist = []
        if not args == "BaseModel" and len(args) > 1:
                print("** class doesn't exist **")
        else:
            for val in valshow:
                allist.append(str(val))
            print(allist)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
            by adding or updating attribute """
        command = args.split(" ")
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not command[0] == "BaseModel":
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) not in objects:
            print("** no instance found **")
        elif len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        else:
            key = objects["{}.{}".format(command[0], command[1])]
            setattr(key, command[2].replace('"', ''),
                    command[3].replace('"', ''))
            key.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
