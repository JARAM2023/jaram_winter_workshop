FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apt-get -y update
RUN apt-get -y install vim

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 50003
ENTRYPOINT gunicorn --bind=0.0.0.0:50003 jaram_winter_workshop.wsgi:application