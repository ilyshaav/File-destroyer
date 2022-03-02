import os
class FileOperation:
    def __init__(self):
        pass
    
    def createDir(nameOfDir):
        os.mkdir(nameOfDir)

    def createFiles(countFiles,text):
        for i in range(int(countFiles)):
            file = open(str(i)+".txt", "w+")
            for i in range(int(countFiles)):
                file.write(text+"\n")
            file.close()
        
    def deleteFile(nameOfFile):
        if os.path.exists(nameOfFile):
            os.remove(nameOfFile)
            
    def interface(cmd, count, text):
        commаnd=cmd
        if int(commаnd) == 1:
            FileOperation.createDir(text)
            return True
        else:
            return False

            
