import sys
def raise_find_error(word):
     print >> sys.stderr, "*** WORD NOT FOUND ***: %s" % word
    
def file_error():
    print >> sys.stderr, "*** ERROR ***: Error in opening file"
