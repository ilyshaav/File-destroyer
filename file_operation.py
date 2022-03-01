import os
class FileOperation:
    def __init__(self):
        pass
    
    def createDir(nameOfDir):
        os.mkdir(nameOfDir)

    def createFiles(countFiles,text):
        for i in range(int(countFiles)):
            file = open(str(i)+".txt", "w+")
            file.close()
        
