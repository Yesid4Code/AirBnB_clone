#!/usr/bin/python3
""" HBnB Console """
import cmd
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
