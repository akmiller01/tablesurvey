# start with a base image
FROM python:3
MAINTAINER vagrant <Alex Miller, alex.miller@devinit.org>

RUN mkdir /src
ADD ./ /src

WORKDIR /src
# install dependencies
RUN apt-get update
RUN pip install -r requirements.txt

CMD gunicorn -w 2 -b 0.0.0.0:80 tablesurvey.wsgi
