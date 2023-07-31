import os
import shutil
Download_Folder=input('Enter folder Name :')
os.chdir(Download_Folder)
for filename in os.listdir('.'):
    if filename.endswith((".jpeg",".jpg",".png")):
        os.makedirs('Images',exist_ok=True)
        shutil.move(filename,'Images')
    elif filename.endswith((".pdf",".docx",".doc",".xlsx")):
        os.makedirs('Docs',exist_ok=True)
        shutil.move(filename,'Docs')
    elif filename.endswith((".html",".css",".js")):
        os.makedirs('Code',exist_ok=True)
        shutil.move(filename,'Code')
    elif filename.endswith((".exe",".zip")):
        os.makedirs('Folder',exist_ok=True)
        shutil.move(filename,'Folder')

print('Done.....')