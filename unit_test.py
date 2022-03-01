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
        FileOperation.createFiles(4,"test test test")
        if os.path.exists('0.txt') and os.path.exists('1.txt') and os.path.exists('2.txt') and os.path.exists('3.txt'):
            print("createfiles test pass ")
            return True
        else:
            print("createfiles test false ")
            return False
        
FilleTests.testCreateDir()
FilleTests.testCreateFile()

    
