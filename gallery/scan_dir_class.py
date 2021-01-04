import os

class ScanDir:

    PATH = "c:/Users/George/venv/myProjects/gallery-pic";

    def scan_dir(self):
        files = os.listdir(self.PATH)
    
        # for f in files:
        #     print(f)
        files = files[:20]
        return files;

    def getFirstFile(self, file):
        if(os.path.isdir(self.PATH + '/' + file)):
            return self.PATH + '/' + file + '/' + os.listdir(self.PATH + '/' + file)[0]
        else:
            return None
