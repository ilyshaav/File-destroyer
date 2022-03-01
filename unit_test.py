import os
from file_operation import FileOperation
class FilleTests(object):
    def __init__(self):
        pass
    
    def testCreateFile():
        FileOperation.createDir('testCreateDir')
        if os.path.exists('testCreateDir'):
            print("createDir test pass ")
            return True
        else:
            print("createDir test false ")
            return False

FilleTests.testCreateFile()
    
