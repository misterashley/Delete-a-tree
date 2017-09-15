import os, shutil

targetdir="/Users/mrashley/Documents/temp/nina images/contents"

for subfol in os.listdir(targetdir):
    subfol = targetdir+"/"+subfol
    files = []
    for x in "1":
        try:
            shutil.rmtree(subfol+"/thumbnail")
        except (FileNotFoundError):
            print("Thumbnail Folder not found in "+subfol)
    for (dirpath,dirnames,filenames) in os.walk(subfol):
        files.extend(filenames)
        break
    
    for file in files:
        try:
            shutil.move(subfol+"/"+file,targetdir)
        except:
            print("Something failed with "+file)
    try:
        #print ("trying to remove "+subfol)
        os.rmdir(subfol)
    except (FileNotFoundError, NotADirectoryError, OSError):
        print("Could not remove folder "+subfol)
