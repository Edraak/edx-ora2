#!/usr/bin/env bash

set -e

cd `dirname $BASH_SOURCE` && cd ..

echo '---------------'

# npm install

# make javascript

# Configure Django settings
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-"settings.dev"}

# Create the database
#echo "Updating the database..."
#python manage.py migrate

echo "Starting server..."
python manage.py runserver_plus "${@:1}"
