from django.shortcuts import render
from gallery.loadFiles import LoadFiles 
from gallery.pagination import Pagination
from django.http import HttpResponse
from shutil import rmtree
import random, ast, os, sys, stat, json

def index(request, last_item = None):
    s = LoadFiles()
    r = Pagination(last_item)
    files = s.scanDirFunc()[r.prev:int(r.last_page)]
    return render(request, 'index.html', { 
        'complete_list': s.getFirstFile(files),
        'next': r.next,
        'prev': r.prev
    })

def view(request, folder_name, last_item = None):
    s = LoadFiles()
    r = Pagination(last_item)
    return render(request, 'view.html', {
        'files_json': json.dumps(s.getPhotosFiles(folder_name)[r.prev:r.last_page]),
        # 'files': json.dumps(s.getPhotosFiles(folder_name)[r.prev:r.lastPage]),
        'folder_name': folder_name,
        'next': r.next,
        'prev': r.prev
    })

def search(request, search = None):
    s = LoadFiles()
    files = s.scanDirFunc()
    search_get = request.GET['search']
    if search_get:
        search = search_get
    if not search_get and not search: # check if empty string
        files = []
    return render(request, 'index.html', { 
        'complete_list': s.getFirstFile(files, True, search),
        'next': None,
        'prev': None
    })

def renameDir(request):
    requestPost = request.body.decode('utf-8')
    requestPost = ast.literal_eval(requestPost) if requestPost and type(requestPost) == str else requestPost
    if ("oldDirName" in requestPost and "newDirName" in requestPost):
        oldPath = LoadFiles.PATH + '/'+ requestPost["oldDirName"]
        newPath = LoadFiles.PATH + '/'+ requestPost["newDirName"]
        if (requestPost["oldDirName"] and requestPost["newDirName"]):
            os.rename(oldPath, newPath) 
    return HttpResponse("Done", content_type='text/plain')

def removeDir(request):
    requestPost = request.body.decode('utf-8')
    requestPost = ast.literal_eval(requestPost) if requestPost and type(requestPost) == str else requestPost
    if ("oldDirName" in requestPost):
        path = LoadFiles.PATH + '/'+ requestPost["oldDirName"]
        if(os.chmod(path, stat.S_IXGRP)):
            os.chmod(path, stat.S_IWOTH)
        rmtree(path)
    return HttpResponse("Done", content_type='text/plain') 