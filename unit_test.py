import os
from file_operation import FileOperation
class FilleTests(object):
    def __init__(self):
        pass
    
    def testCreateDir():
        FileOperation.createDir('testCreateDir')
        if os.path.exists('testCreateDir'):
            print("createDir test pass ")
            return True
        else:
            print("createDir test false ")
            return False
        
    def testCreateFile():
        FileOperation.createFiles(4,"test")
        if os.path.exists('0.txt') and os.path.exists('1.txt') and os.path.exists('2.txt') and os.path.exists('3.txt'):
            file0 = open("0.txt",'r')
            file1 = open("1.txt",'r')
            file2 = open("2.txt",'r')
            file3 = open("3.txt",'r')
            
            if file0.read() == "test\ntest\ntest\ntest\n" \
            and file1.read() == "test\ntest\ntest\ntest\n" \
            and file2.read() == "test\ntest\ntest\ntest\n" \
            and file3.read() == "test\ntest\ntest\ntest\n":
                print("createfiles test pass ")
                return True
            else:
                print("createfiles test false ")
                return False
        else:
            print("createfiles test false ")
            return False
        
    def testDeleteFile():
        for i in range(4):
            if os.path.exists(str(i)+".txt"):
               FileOperation.deleteFile(str(i)+".txt")
            else:
                print("delete file test false ")
                return False
        print("delete file test pass ")
        return True
    
    def testInterface():
        cheсklist=[False, False, False,False]
        cheсklist[0] = FileOperation.interface('1','2',"testCreateDirInterface")
        cheсklist[1] = FileOperation.interface('2','3',"test Create text in files")
        cheсklist[2] = FileOperation.interface('3','3',"testCreateDirInterface")
        cheсklist[3] = FileOperation.interface('4','3',"test Create text in files")
        if cheсklist == [True,True,True,True]:
            print("interface test pass ")
            return True
        else:
            print("interface test false ")
            return False
        
             
        
FilleTests.testCreateDir()
FilleTests.testCreateFile()
FilleTests.testDeleteFile()
FilleTests.testInterface()


    
