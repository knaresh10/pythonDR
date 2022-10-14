import os


os.chdir(r"D:\Drive Ready\python\divide files\task")

slash = '\\'
path = os.getcwd()
print(path)

files = os.listdir()
os.chdir("../")
for file in files:
    s = file.split('.')[-1]
    print(s)
    ext = path  + slash + s
    if not os.path.isdir(ext):
        os.mkdir(ext)
    os.rename(path +slash + file, ext +slash + file)
    
        
    
