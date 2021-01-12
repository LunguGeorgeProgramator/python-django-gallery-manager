This application is used for managing image gallery folders and files if is needed in anyplace on a server if the permissions are set to read on them.

It is build on Django and some vue elements on the ui side. Set a python environment and clone this project there.

To set the path of the gallery change the code in class "LoadFiles" located in:
  
    https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/gallery/loadFiles.py
    
Code to change is the path, I build this on a windows OS so my this is my pictures path on my computer. Change it to any paht on your machine that has a directories with photos files in them:

    PATH = "c:/Users/George/Pictures"
    
The number of folder per page is set no by default to 100, it can be change to any number in class "Pagination" located in:

    https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/gallery/pagination.py
    
Change code form 100 to any number nedded:
    
    MAX_ON_PAGE = 100
