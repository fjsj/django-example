#!/bin/sh

env_python=env/bin/python
env_pip=env/bin/pip
requirements=requirements/staging.txt
cd_manage_dir='cd django-example'

sudo fuser -k 8080/tcp
$env_pip install -r $requirements
$cd_manage_dir
../$env_python manage.py syncdb --noinput --settings=core.settings.staging
../$env_python manage.py migrate --settings=core.settings.staging
../$env_python manage.py collectstatic --noinput --settings=core.settings.staging
../$env_python manage.py runserver 8080 --settings=core.settings.staging
