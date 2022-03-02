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
        countFiles=count
        if int(commаnd) == 1:
            FileOperation.createDir(text)
            return True
        elif int(commаnd) == 2:
            FileOperation.createFiles(int(count),text)
            return True
        elif int(commаnd) == 3:
            os.rmdir(text)
            return True
        elif int(commаnd) == 4:
            for i in range(int(countFiles)):
                FileOperation.deleteFile(str(i)+".txt")
            return True
        else:
            return False
run = 1
print("команды: ")
print("1 - создать папку")
print("2 - создать файлы")
print("3 - удалить папку")
print("4 - удалить файлы")

while (run):
    FileOperation.interface(input("Введите команду: "),input("Введите кол-во: "), input("Введите текст: "))
            
