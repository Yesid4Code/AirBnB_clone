#!/usr/bin/python3
""" HBnB Console """
import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "Review": Review, "City": City, "Place": Place, "State": State}


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

    def default(self, args):
        """
        Separete the line command to find instrucciontions.
            Expect: <class name>.all().
        """
        command = args.split(".")
        if len(command) == 2:
            if command[1] == "count()":
                self.do_count(command[0])
            elif command[1] == "all()":
                self.do_all(command[0])
            elif command[1][0:4] == "show":
                # self.do_show(command[0] + " " + command[1][5:])
                idd = re.split(r'show\("|"\)', command[1])
                self.do_show(command[0] + " " + idd[1])
            elif command[1][:7] == "destroy":
                idd = re.split(r'destroy\("|"\)', command[1])
                self.do_destroy(command[0] + " " + idd[1])
            elif command[1][:6] == "update":
                lis = re.split(r'update\("|"|, "|\)', command[1])
                print(list_u)
                print("Yo: " + list_u[5])
                self.do_update(command[0] +
                               " " + lis[1] + " " + lis[3] + " " + lis[5])

    def do_create(self, args):
        """ Create new instance of the class """
        if len(args) == 0:
            print("** class name missing **")
        elif not (args in classes):
            print("** class doesn't exist **")
        else:
            new = classes[args]()
            new.save()
            print(new.id)

    def do_count(self, args):
        """ Count the number of instances of a class. """
        command = args.split(" ")
        objects = storage.all()
        count = 0

        if not (args in classes) and len(args) > 0:
            print("** class doesn't exist **")
        elif len(args) == 0:
            for k in objects.keys():
                count += 1
            print(count)
        else:
            for k in objects:
                key = k.split(".")
                if key[0] == command[0]:
                    count += 1
            print(count)

    def do_show(self, args):
        """ Show string representation """
        command = args.split(" ")
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not command[0] in classes:
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
        elif not command[0] in classes:
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
        command = args.split(" ")
        objects = storage.all()
        allist = []
        if not (args in classes) and len(args) > 0:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for value in objects.values():
                allist.append(str(value))
            print(allist)
        else:
            for k, value in objects.items():
                key = k.split(".")
                if key[0] == command[0]:
                    allist.append(str(value))
            print(allist)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
            by adding or updating attribute """
        command = args.split(" ")
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not command[0] in classes:
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
