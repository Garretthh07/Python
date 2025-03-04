#!/usr/bin/python
# Filename: using_file.py

poem = '''\
        Programming is fun
        When the work is done
        if you wanna make your work also fun:
            use Python!
'''

f = file('poem.vim', 'w')  # open for 'w'riting, if this file is not exist, will create it!
f.write(poem) # write text to file
f.close() # close the file

f = file('poem.vim') # if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: #Zero length indicates EOF
        break
    print line, #Notice comma to avoid automatic newline added by Python

f.close() # close the file
