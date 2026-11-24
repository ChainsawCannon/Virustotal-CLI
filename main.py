import sys
import help
from fileread import *
from about import *
from urlread import * 
# API Key obtaining from file, (BRING YOUR OWN KEY)
#main function just calls for other virustotal functions which will be programmed into other modules


#arguments after main.py enabled
if __name__ == '__main__':
    args = sys.argv[1:]
    
    #arguments exist
    if args:
        func = args[0]
        #help argument provided!
        if func == "-help":
            help.help()
        
        #feeds file argument to fileread
        if func == "-hp":
            filepath = args[1]
            fhash(filepath)
        if func == "-fs":
            filepath = args[1]
            filescan(filepath)
        if func == "-hs":
            sample = args[1]
            hashscan(sample)
        if func == "-url":
            url = args[1]
            urlscan(url)

        if func == "-about":
            about()
    #if no argument is provided that is in the list, print a command mentioning help
    else:
        print("No argument provided or is invalid, use -help for help")