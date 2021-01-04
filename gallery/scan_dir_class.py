import os

class ScanDir:

    PATH = "c:/Users/George/venv/myProjects/gallery-pic"

    def scanDirFunc(self):
        files = os.listdir(self.PATH)
        return files[:20]

    def getFirstFile(self, files, first_file = True):
        files_content = []
        for file in files:
            if(os.path.isdir(self.PATH + '/' + file) == False):
                continue
            files_in_dir = os.listdir(self.PATH + '/' + file)
            if(first_file == True):
                files_in_dir = files_in_dir[0]
            files_content.append({
                'dir': file,
                'files_in_dir': file+'/'+files_in_dir
            })
        return files_content
            


