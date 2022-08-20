import os
import shutil

from_dir='C:/Users/ga969/Downloads/C102_assets-main/C102_assets-main'
to_dir='D:/WhiteHat.Jr/Class 102/Images'

list_of_files=os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    print(name)
    print(extension)
    
    if extension=='':
        continue
    
    if extension in ['.gif','.png','.jpg','.jpeg','jfif']:
        path1=from_dir + '/' + filename
        path2=to_dir + '/' + 'image_files'
        path3=to_dir + '/' + 'image_files' + '/' + filename
        
        #print(path1)
        #print(path3)
        
        if os.path.exists(path2):
            print('moving' + filename + '....')
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print('moving' + filename + '....')
            shutil.move(path1,path3)
            