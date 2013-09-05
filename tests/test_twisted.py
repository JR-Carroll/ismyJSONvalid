import unittest
from ismyJSONvalid import *
from twisted.web.static import File

class TestmyFile(unittest.TestCase):
    """Tests that the MyFile class in ismyJSONvalid.py."""
    def testIsLeafTrue(self):
        """Test if File obj is a leaf"""
        self.fileObj = MyFile("dummy")
        self.assertFalse(self.fileObj.isLeaf)
    
    def testInstanceofFile(self):
        """
        Test if MyFile() is an instance of File()
        Test fails if True
        """
        self.fileObj = MyFile("dummy")        
        self.failIfEqual(MyFile, File)

    def testrender_Post(self):
        """
        Test to make sure that when no value is available, the default
        value is set to '{}'
        """
        pass


class TestConsoleOutput(unittest.TestCase):
    def testStartServer(self):
        pass


class TestFileCreation(unittest.TestCase):
    def testWriteTestFile(self):
        pass
    def testFileCreationErrorCatching(self):
        pass
    
    
class TestLogging(unittest.TestCase):
    def testLocation(self):
        pass
    def testLogWarning(self):
        pass
    def testLogError(self):
        pass
    def testLogInfo(self):
        pass


class TestTwisted(unittest.TestCase):
    def testEntryPage(self):
        pass
    def testFactory(self):
        pass

class TestStaticData(unittest.TestCase):
    def testPort(self):
        pass
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
    
        