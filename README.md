# django_barebones
Django Barebone Project

# With docker
## Starting the App
- Run `docker compose up -d`
- Navigate to `http://localhost:8000/`

## Listing the app
`docker ps`

## Stopping the App
`docker compose down`

# How to install and  run without docker
- `pip install -r requirements.txt`
- `cd django_barebones`
- `python manage.py migrate`
- `python manage.py runserver` 

