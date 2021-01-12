This application is used for managing image gallery folders and files if is needed, in any place on a server if the permissions are set to read on them.

It is build on Django and some vue elements on the ui side. Set a python environment and clone this project there.

To set the path of the gallery change the code in class "LoadFiles" located in:
  
    https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/gallery/loadFiles.py
    
Code to change is the path, I build this on a windows OS so my this is my pictures path on my computer. Change it to any paht on your machine that has a directories with photos files in them:

    PATH = "c:/Users/George/Pictures"
    
The number of folder per page is set no by default to 100, it can be change to any number in class "Pagination" located in:

    https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/gallery/pagination.py
    
Change code form 100 to any number nedded:
    
    MAX_ON_PAGE = 100

Tutorial index page:

![name-of-you-image](https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/tutorial_photos/index.jpg?raw=true)

Option of this page are:
  1. search in the top form add text and click the blue button.
  2. navigate pagiation.
  3. edit each folder name or remove it for ever for your store.
  4. click one of the photos representing one folder and see the photos content ('loads the view page').

![name-of-you-image](https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/tutorial_photos/edit_page.jpg?raw=true)

View photos per folder page, here if there are more than the max items pe page ('see variable MAX_ON_PAGE default value 100') the pagination can be used to see them all. 
Also there is a view photo vue library added to examin in more detail "vue-viewer" just click on photo:

![name-of-you-image](https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/tutorial_photos/view.jpg?raw=true)
