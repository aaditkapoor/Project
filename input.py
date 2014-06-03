import sys

def checker(arg):
    '''
         checker(str) -> bool
         Checks whether the given arg is a command or not
    '''
    
    if arg == 'exit':   
        print >> sys.stderr, "*** EXITING ***"
        sys.exit(0)


