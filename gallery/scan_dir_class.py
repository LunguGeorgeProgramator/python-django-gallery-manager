# -*- coding: utf-8 -*-
import os
import urllib.parse

class ScanDir:

    PATH = "c:/Users/George/venv/myProjects/gallery-pic"

    def scanDirFunc(self):
        files = os.listdir(self.PATH)
        return files

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
                'files_in_dir': ScanDir.replaceString(file+'/'+files_in_dir)
            })
        return files_content
    
    @staticmethod
    def replaceString(str_var):
        # # str_var = str_var.replace('%','%25')
        # # str_var = str_var.replace('#','%23')
        # str_var_n = str_var.decode('utf8')
        # str_var = str_var_n.encode('cp1250')
        # str_var = urllib.parse.quote(str_var)
        return urllib.parse.quote_plus(str_var)


