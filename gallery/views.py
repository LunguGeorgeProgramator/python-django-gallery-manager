from django.shortcuts import render
from gallery.scan_dir_class import ScanDir
from gallery.pagination import Pagination
import random


def index(request, last_item = None):
    r = Pagination(last_item)
    s = ScanDir()
    files = s.scanDirFunc()
    files = s.scanDirFunc()[r.prev:r.next]
    return render(request, 'index.html', {
        'var_test': 's', 
        'files': files, 
        'complete_list': s.getFirstFile(files),
        'next': r.next,
        'prev': r.prev,
    })

def view(request):
    return render(request, 'view.html', {'var_test': 's2'})

