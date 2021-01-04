from django.shortcuts import render
from gallery.scan_dir_class import ScanDir
import random


def index(request):
    files_content = []
    files = ScanDir().scan_dir()
    for file in files:
        first_file = ScanDir().getFirstFile(file)
        if (first_file):
            files_content.append({
                'dir': file,
                'first_file': first_file
            })
    return render(request, 'index.html', {'var_test': 's', 'files': ScanDir().scan_dir(), 'complete_list': files_content})

def view(request):
    return render(request, 'view.html', {'var_test': 's2'})