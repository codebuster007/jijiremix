#!/bin/bash
source ./jijiremix/setup/envvars.sh

python manage.py makemigrations &
python manage.py migrate &
python manage.py runserver &  