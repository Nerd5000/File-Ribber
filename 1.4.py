import os,shutil
filePath=input("enter path to rib : ")
fileFormate=input("enter files formate : ")
fileSavePath=input("enter save path : ")

filesDict={}
counter=1
if os.path.exists(filePath):
    if "." in fileFormate:
        fileFormate=fileFormate.replace('.','')
    
    for Root,Folders,Files in os.walk(filePath):
        for file in Files:
            if file.lower().split(".")[-1]==fileFormate:
                shutil.copy(os.path.join(Root,file),fileSavePath)
        
            
else:
    print("path don't exsist")
