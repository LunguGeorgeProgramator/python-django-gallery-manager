from django.shortcuts import render
from gallery.scan_dir_class import ScanDir
import random


def index(request):
    files = ScanDir().scanDirFunc()
    return render(request, 'index.html', {
        'var_test': 's', 
        'files': files, 
        'complete_list': ScanDir().getFirstFile(files)
    })

def view(request):
    return render(request, 'view.html', {'var_test': 's2'})