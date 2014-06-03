
import sys
import error
import time
def highlight_search(word,data):
    '''
        hightlight_search(word,data) -> str
        Prints the word to be found in color
    '''
    
    for d in data:
        if d.find(word) == -1:
            print "Word not found!\n"
        else:
            index = d.index(word)
            if index in [0,1,2]:
                print >> sys.stderr, word[index],
                time.sleep(1)
                print d[index+1:]
                continue
            else:
                print "Invalid"
            
