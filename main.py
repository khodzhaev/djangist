
import os, sys, random
line = "###########################################################\n"


print("Hello, I am Anata, i can help you create django.")


print("Let's begin, Enter all services.\nexample: pages control api.")
while True:
    APP_SERVICES = input(": ")
    flag = input(line + str(APP_SERVICES.split(" ")) + "\nCorrect? [Y/n]: ")
    if flag == "Y":
        print("STARTING.....")
        APP_SERVICES = APP_SERVICES.split(" ")
        break
    

py  = "venv/bin/python"
pip = "venv/bin/pip"
venv = "venv/bin"
os.system("pip3 install virtualenv")
os.system("virtualenv venv")
os.system(f'{pip} install django')
os.system(f'{pip} install pillow')
os.system(f'{pip} install django_resized')
os.system(f'{pip} install django-cors-headers')
os.system(f'{pip} install psycopg2')
os.system(f'{pip} install psycopg2-binary')
os.system(f'{pip} install django_cleanup')
os.system(f'{pip} install gunicorn')
os.system(f'{pip} install django_dramatiq')
os.system(f'{pip} install pika')
os.system(f"{venv}/django-admin startproject core .")
os.mkdir('templates')
for i in APP_SERVICES:
    os.system(f'{py} manage.py startapp {i}')
def gen():
    c = ""
    for i in range(0, 60):
        c += random.choice("qwertyuiopasdfghjklzxcvbnm!@#$%^&*()<>")
    return c

with open('core/local_settings.py', 'w', encoding="utf-8") as file:
    file.write("""  
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '""" + gen() + """'


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'niat_db',
#        'USER': 'niat_admin',
#        'PASSWORD': 'ge7csbk3f6sk',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.yandex.com'
#EMAIL_HOST_USER = 'reset@zamin.dev'
#EMAIL_HOST_PASSWORD = 'fzuqanhxawysypgl'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#SERVER_EMAIL = EMAIL_HOST_USER
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER   
    """)

with open('core/settings.py', 'r', encoding="utf-8") as file:
    z = file.readlines()


z.insert(46, "\t'corsheaders.middleware.CorsMiddleware',\n")
z.pop(57)
z.insert(57, "\t\t'DIRS': [BASE_DIR / 'templates'],\n")



z.pop(106)
z.insert(106, "LANGUAGE_CODE = 'ru'\n")
z.pop(108)
z.insert(108, "TIME_ZONE = 'Asia/Tashkent'\n")

z.pop(120)
z.insert(120, """

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'core/static'
]
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True

#DRAMATIQ_BROKER = {
#    "BROKER": "dramatiq.brokers.rabbitmq.RabbitmqBroker",
#    "OPTIONS": {
#        "url": "amqp://localhost:5672",
#    },
#    "MIDDLEWARE": [
#        "dramatiq.middleware.Prometheus",
#        "dramatiq.middleware.AgeLimit",
#        "dramatiq.middleware.TimeLimit",
#        "dramatiq.middleware.Callbacks",
#        "dramatiq.middleware.Retries",
#        "django_dramatiq.middleware.DbConnectionsMiddleware",
#        "django_dramatiq.middleware.AdminMiddleware",
#    ]
#}

#DRAMATIQ_TASKS_DATABASE = "default"

""")



for i in range(30):
    z.pop(0)


for i in range(6):
    z.pop(46)

z.insert(0, "try:\n\tfrom .local_settings import *\nexcept ImportError:\n\tpass\n")
z.insert(10, "\t'corsheaders',\n")
z.insert(10, "\t'django_dramatiq',\n")
z.insert(10, "\t'django_cleanup',\n")


for i in APP_SERVICES:
    z.insert(13, f"\t'{i}',\n")


with open('core/settings.py', 'w', encoding="utf-8") as file:
    file.write("".join(z))

os.mkdir('core/static')

os.system(f'{py} manage.py makemigrations')
os.system(f'{py} manage.py migrate')



with open('core/urls.py', 'w', encoding="utf-8") as file:
    file.write("""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('_admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
""")

with open('core/urls.py', 'r', encoding="utf-8") as file:
    z = file.readlines()

for i in APP_SERVICES:
    z.insert(7, f"\tpath('{i}/', include('{i}.urls')),\n")

with open('core/urls.py', 'w', encoding="utf-8") as file:
    file.write("".join(z))

for i in APP_SERVICES:
    with open(f'{i}/urls.py', 'w', encoding="utf-8") as file:
        file.write("""
from django.urls import path
from . import views
urlpatterns = [
    
]    
""")
    os.mkdir(f"templates/{i}")


with open('.gitignore', 'w', encoding="utf-8") as file:
    file.write("""
    
# Django #
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media
local_settings.py
# Backup files #
*.bak

# If you are using PyCharm #
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/dictionaries
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.xml
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/gradle.xml
.idea/**/libraries
*.iws /out/

# Python #
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text #
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code #
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
    
""")