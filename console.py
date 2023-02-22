#!/usr/bin/python3
""" Documentation for the console py """

import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command processor HBNB."""
    # 
    prompt = '(hbnb) '
    use_rawinput = True
    
    #
    CLASSLIST = ["BaseModel", "User"]
    
    # Methode Obligatoire
    def cmdloop(self, intro=None):
        """_summary_

        Args:
            intro (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return cmd.Cmd.cmdloop(self, intro)
    
    # def preloop(self):
    # def postloop(self):
        
    def emptyline(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return 0 #cmd.Cmd.emptyline(self)
    
    # Methode Commande
    def do_EOF(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True
    
    def do_quit(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True
    
    # Create Methode
    def do_create(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if line and line in self.CLASSLIST:
            cls = eval(line) #getattr(sys.modules[__name__], line)
            base = cls()
            storage.new(base)
            print(base.id)
        elif line is None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def complete_create(self, text, line, begidx, endidx):
        """_summary_

        Args:
            text (_type_): _description_
            line (_type_): _description_
            begidx (_type_): _description_
            endidx (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not text:
            completions = self.CLASSLIST[:]
        else:
            completions = [ f
                            for f in self.CLASSLIST
                            if f.startswith(text)
                            ]
        return completions
    # Show Methode
    def do_show(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        args = self.parseline(line)
        #print(f"{args[0]}, {args[1]}")
        if args[0] and args[0] in self.CLASSLIST:
            if args[1]:
                item = storage.all().get("{}.{}".format(args[0], args[1]), False)
                if (item):
                    print(str(item))
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")
        

    def complete_show(self, text, line, begidx, endidx):
        """_summary_

        Args:
            text (_type_): _description_
            line (_type_): _description_
            begidx (_type_): _description_
            endidx (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not text:
            completions = self.CLASSLIST[:]
        else:
            completions = [ f
                            for f in self.CLASSLIST
                            if f.startswith(text)
                            ]
        return completions
    
    def do_all(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if line and line in self.CLASSLIST:
            for k, item in storage.all().items():
                if item.get("__class__", None) == line:
                    print(item)
        elif line:
            print("** class doesn't exist **")
        else:
            print(storage.all())
    
    def do_destroy(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        args = self.parseline(line)
        if args[0] and args[0] in self.CLASSLIST:
            if args[1]:
                items = storage.all()
                item = items.get("{}.{}".format(args[0], args[1]), False)
                if (item):
                    del items["{}.{}".format(args[0], args[1])];
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

if __name__ == '__main__':
    HBNBCommand(stdin=input).cmdloop()
