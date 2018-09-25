# start with a base image
FROM django:2.1.1-python3
MAINTAINER vagrant <Alex Miller, alex.miller@devinit.org>

RUN mkdir /src
ADD ./ /src

WORKDIR /src
# install dependencies
RUN apt-get update
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD gunicorn -w 2 -b 0.0.0.0:80 ghts.wsgi
