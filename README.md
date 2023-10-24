# django_barebones
Django Barebone Project

# With docker

# Build the images
`docker-compose build`

## Starting the App
- Run `docker compose up -d`
- Navigate to `http://localhost:8000/`

# Docker images
`docker images`

## Stopping the App
`docker compose down`

## AWS references
`https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html`

# How to install and  run without docker
- `pip install -r requirements.txt`
- `cd django_barebones`
- `python manage.py migrate`
- `python manage.py runserver` 

