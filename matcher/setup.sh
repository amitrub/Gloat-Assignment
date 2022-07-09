#!/bin/bash

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/job_matcher.json --app job_matcher
python manage.py runserver