#copyfile() : copies contents of a file
#copy(): copyfile()+ permission mode+destination can be directory
#copy2(): copy()+copies metadata(file's creation and modification times)

import shutil

#This will create similar file with different name
#You can choose your destination to be a new file
#or the path of choice.
shutil.copy('File detection.txt','copy.txt')

#if you need to use the other commands, the arguments are the same.

