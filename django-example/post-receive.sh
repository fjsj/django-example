#!/bin/sh

env_python=../env/bin/python
env_pip=../env/bin/pip

@sudo fuser -k 8080/tcp
$(env_python) manage.py syncdb --noinput --settings=core.settings.production
$(env_python) manage.py migrate --settings=core.settings.production
$(env_python) manage.py collectstatic --noinput --settings=core.settings.production
$(env_python) manage.py runserver 8080
