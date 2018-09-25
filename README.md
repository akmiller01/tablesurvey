# To build (with new Postgres Docker):
```bash
docker volume create --name=surveydata
docker-compose up --build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py collectstatic --noinput
```


# To run:
```bash
docker-compose up
```

# TODO
0. Add which campaign to surveyresponse model, so it can be queried.
1. Capture POSTed form data gracefully.
2. Return POSTed form data gracefully.
