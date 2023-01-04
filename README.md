# djangoproject_windows
Part of Literarywebapp with Deep Learning methods 
Important content: 

1. "texteapp"-directory is a core-app for manager and maitanance, content: 1.1. settings.py; 1.2. urls.py

2. "literary"- directory is a program for textesearch, content: 2.1. "templates"-directory with index.html; 2.2. "fixtures" directory with mypapers.json; 2.3. models.py with database class; 2.4. views.py mixins and generic class based views;

3. "Mytext"- directory is a program for projectmanagement and textesearch (now not completely, but prototype): 3.1."templates"-directory with index.html; 3.2. "fixtures" directory with myproject.json and mytext.json; 3.3. models.py with database class; 2.4. views.py mixins and generic class based views;

4. db.sqlite3 is database

Requierements: 

Python 3.9.12
Django 4.1.1
Pip 22.3.1
Supplementary Library, install with pip: 
django-easticrearch-dsl; NLTK; pandas; spaCy; TextBlob; numpy; docx; bs4; gensim; djangorestframework; django-filter; scikit-learn; unidecode; tweepy; seaborn; sklearn_crfsuite; drf-json-api; djangorestframework-jsonapi; PyPDF2(deprecated at 24.12.2022) replace with pdf; pdfminer.six; matplotlib; HanTa;
Djangoproject_state_of_the_art: TensorFlow; biobert_bern (https://pypi.org/project/biobert-bern/); transformers;python-heatclient; seaborn; matplotlib;mpi;venv¿
User manual (MAC OS):
1. git clone -link 
2. %cd djangoproject
3. %python –m venv venv (=create the venv)
4. % source venv/bin/activate  (=activate the venv)
5. pip install --upgrade pip
6. pip install django
7. Open the texteapp/settings.py; Enter the ALLOWED_HOSTS = ['127.0.0.1','localhost',], save
8. %python manage.py createsuperuser
9. { Enter username (Olgjanius) and password (m57BOG+P)
10. %python manage.py runserver (=start server)
11. Start webbrowser, localhost:8000/admin/
12. Start search for paper under: localhost:8000/search/

User manual (Windows):
1. git clone -link 
2. > cd djangoproject
3. > py --version (=control of python)
4. > py -m venv venv (=create of virtual enviroment)
5. > venv\Scripts\activate.bat (=activate of virtual enviroment)
6. py -m pip install --upgrade pip
7. py -m pip install Django
8. Open the texteapp/settings.py; Enter the ALLOWED_HOSTS = ['127.0.0.1','localhost',], save
9. > python manage.py createsuperuser
10. { Enter username () and password ()
11. > python manage.py runserver (=start server)
12. Start webbrowser, localhost:8000/admin/
13. Start search for paper under: localhost:8000/search/
Schema:

[Djangoproject.pdf](https://github.com/Olgjanius/djangoproject/files/10244543/Djangoproject.pdf)


 

