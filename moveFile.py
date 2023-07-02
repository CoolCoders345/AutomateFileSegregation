import os
import shutil

from_dir="C:/Users/kovai/Downloads"
to_dir="C:/Users/kovai/OneDrive/Desktop/code/Python/Project102.py"

isExist=os.path.exists(from_dir)
list_of_files = os.listdir(from_dir)
print(list_of_files)
print(isExist)

for fileName in list_of_files:
    name, extension=os.path.splitext(fileName)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".gif",".png","jpg",".jpeg",".jfif"]:
        path1=from_dir+"/"+fileName
        path2=to_dir+'/'+ "Image_files"
        path3=path2+"/"+fileName
        if os.path.exists(path2):
            shutil.copy(path1,path3)
        else: 
            os.makedirs(path2)
            shutil.copy(path1,path3)
    if extension in [".pdf", ".txt", ".docx"]:
        path1=from_dir+"/"+fileName
        path2=to_dir+'/'+ "Doc_files"
        path3=path2+"/"+fileName
        if os.path.exists(path2):
            shutil.copy(path1,path3)
        else: 
            os.makedirs(path2)
            shutil.copy(path1,path3)