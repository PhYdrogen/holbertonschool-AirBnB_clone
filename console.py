#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command processor HBNB."""
    # 
    prompt = '(hbnb) '
    
    #
    CLASSLIST = ["BaseModel", "User"]
    
    # Methode Obligatoire
    def cmdloop(self, intro=None):
        print ('cmdloop(%s)' % intro)
        return cmd.Cmd.cmdloop(self, intro)
    
    # def preloop(self):
    # def postloop(self):
        
    def emptyline(self):
        print ('emptyline()')
        return cmd.Cmd.emptyline(self)
    
    # Methode Commande
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True
    
    # Create Methode
    def do_create(self, line):
        if line and line in self.CLASSLIST:
            cls = eval(line) #getattr(sys.modules[__name__], line)
            base = cls()
        elif line is None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def complete_create(self, text, line, begidx, endidx):
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
        args = self.parseline(line)
        print(f"{args[0]}, {args[1]}")
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
        if not text:
            completions = self.CLASSLIST[:]
        else:
            completions = [ f
                            for f in self.CLASSLIST
                            if f.startswith(text)
                            ]
        return completions
    
    def do_all(self, line):
        if line and line in self.CLASSLIST:
            for k, item in storage.all().items():
                if item.get("__class__", None) == line:
                    print(item)
        elif line:
            print("** class doesn't exist **")
        else:
            print(storage.all())
    
    def do_destroy(self, line):
        return True

    def do_update(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()