Technologies:

    Django 3.0.5
    Python 3.7.7
    Bootstrap v4.4.1
    Font Awesome 4.7.0
    Vue v2.6.11
    Vue Modal
    VuePreviewer
    Axios v0.19.2

This application is used for managing image gallery folders and files if is needed, in any place on a server if the permissions are set to read on them.

It is build on Django and some vue elements on the ui side. Set a python environment and clone this project there.

To set the path of the gallery change the code in class "LoadFiles" located in:
  
    https://github.com/LunguGeorgeProgramator/python_gallery_manager/blob/master/gallery/loadFiles.py
    
Code to change is the path, I build this on a windows OS so my this is my pictures path on my computer. Change it to any paht on your machine that has a directories with photos files in them:

    PATH = "./tutorial_photos"
    
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

To run this website on docker just follow the list steps:

1. open terminal and ender project location:

        cd your_path_to_project/python-django-gallery-manager
2. run docker compose file to set python version and django package:

        docker-compose up
        
3. after all is automaticlly downloaded and extrated I think last line shold be:

        python_1  |  Watching for file changes with StatReloader

4. Afetr just access in a browser link:

        http://127.0.0.1:8090/ or http://0.0.0.0:8090/ or http://localhost:8090/ or http://your_docker_domenain_set:8090/


This website can be run on a python envirement "you need to set on on your machine also set dejango to". The setps to run it are:

1. activate python envirement in terminal ("I am using windows"), venv is the name of the folder I set it:

        C:\Users\George> venv\Scripts\activate
  
2. Ender project location:

        (venv) C:\Users\George>cd venv/myProjects/python-django-gallery-manager
        
3. Start python server:
    
        (venv) C:\Users\George\venv\myProjects\python-django-gallery-manager>py manage.py runserver
        
4. Wait for it to finish last line should be:

        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
        
 5. Afetr just access in a browser link:

        http://127.0.0.1:8000/ or http://0.0.0.0:8000/ or http://localhost:8000/ or http://your_enev_domenain_set:8000/
        

