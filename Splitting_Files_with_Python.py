import os, shutil
dictexten={
    'audio':('.mp3','wav'),
    'video':('.m4a','MKV',".mpeg"),
    'doc':('.doc','.docx','.pdf'),
    'picture':('.jpg','.png')
         }

loactionPath=input("Enter your path: ")

def findfile(filepath,extensions):
    files=[]
    for file in os.listdir(filepath):
        for extension in extensions:
            if file.endswith(extension):
                files.append(file)
    return files

for ex_type, dotextn in dictexten.items():
    folderName=ex_type+'_files'
    folderPath=os.path.join(loactionPath,folderName)
    os.mkdir(folderPath)

    for i in findfile(loactionPath,dictexten):
        ipath=os.path.join(loactionPath,i)
        ipathnew=os.path.join(folderPath,i)
        shutil.move(ipath,ipathnew)

