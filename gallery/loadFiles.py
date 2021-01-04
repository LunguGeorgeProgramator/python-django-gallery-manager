# -*- coding: utf-8 -*-
import os, re
import urllib.parse

class LoadFiles:

    PATH = "c:/Users/George/venv/myProjects/gallery-pic"

    def __init__(self, path_to_scan = None):
        self.path_to_scan = path_to_scan if path_to_scan else self.PATH

    def scanDirFunc(self):
        return os.listdir(self.path_to_scan)

    def getFirstFile(self, files, first_file = True, search = None):
        files_content = []
        for file in files:
            if(os.path.isdir(self.path_to_scan + '/' + file) == False):
                continue
            if search and not re.search(re.escape(search), file, flags=re.I):
                continue
            files_in_dir = os.listdir(self.path_to_scan + '/' + file)
            if(first_file == True):
                files_in_dir = files_in_dir[0]
            files_content.append({
                'dir_name': file,
                'dir_name_encoded': file,
                'files_in_dir': LoadFiles.encodeUrl(file+'/'+files_in_dir)
            })
        return files_content
    
    def getPhotosFiles(self, dir_name):
        files_content = []
        dir_name = LoadFiles.decodeUrl(dir_name)
        self.path_to_scan = self.path_to_scan + '/' + dir_name
        for file in self.scanDirFunc():
            file_path = self.path_to_scan + '/' + file
            if(os.path.isdir(file_path) == True):
                continue
            files_content.append(file_path)
        return files_content
    
    @staticmethod
    def encodeUrl(str_var):
        return urllib.parse.quote(str_var)
    
    @staticmethod
    def decodeUrl(str_var):
        return urllib.parse.unquote(str_var)


