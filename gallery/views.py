from django.shortcuts import render
from gallery.loadFiles import LoadFiles 
from gallery.pagination import Pagination
import random

def index(request, last_item = None):
    r = Pagination(last_item)
    s = LoadFiles()
    files = s.scanDirFunc()[r.prev:r.lastPage]
    return render(request, 'index.html', { 
        'complete_list': s.getFirstFile(files),
        'next': r.next,
        'prev': r.prev
    })

def view(request, folder_name, last_item = None):
    r = Pagination(last_item)
    return render(request, 'view.html', {
        'files': LoadFiles().getPhotosFiles(folder_name)[r.prev:r.lastPage],
        'folder_name': folder_name,
        'next': r.next,
        'prev': r.prev
    })

