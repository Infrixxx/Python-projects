# Delete file

import os
import shutil

#To delete file we use os.remove('filepath/file name')

#os.remove('Deletethisfile.txt')

#Or you can make it a variable and then delete
path='Deletethisfile.txt'
#os.remove(path)

try:
    os.remove(path)
except FileNotFoundError:
    print(path+ " doesn't exist.")

FOLDER="KK"

#This will say I do not have permission, we create a try except code
#os.remove('KK')

#To delete a folder we use a different code. os.rmdir('KK')
#To delete a file with files we use shutil.rmtree(FOLDER)
try:
    #os.rmdir(FOLDER)
    # Cannot delete folder with the current command, we need to import shutil module
    #we use the shutil command to delete folders with files
    shutil.rmtree(FOLDER)

except PermissionError:
    print(FOLDER+''+ 'Was not found')


except  OSError:
    print('You cannot delete using that function')
else:
    print("Folder was deleted")