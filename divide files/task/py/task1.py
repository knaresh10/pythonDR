import os
import shutil
for file in os.listdir():
    di = file.split('.')[-1]
    if not os.path.isdir(di):
        os.mkdir(di)
    shutil.move(os.getcwd()+"\\"+file, di)
