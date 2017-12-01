# ChatbotAPI
Simple project that serves as a demo, to show how to build a very simple Rest API and use it for a chatbot.

First we need to create an environment, then install all our packages (only Django and its Rest Framework). 
When it's done, we can create the Django project and the api app.
```
virtualenv env
source env/bin/activate

pip install django djangorestframework

django-admin.py startproject chatbot_api

cd chatbot_api

python manage.py startapp api
```

When it's done, we need to add Django Rest Framework to the installed apps parameter of our project, in chatbot_api/chatbot_api/settings.py :

```
INSTALLED_APPS = (
    ...
    'rest_framework',
    'api.apps.ApiConfig',
)
```
