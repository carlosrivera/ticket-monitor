FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev -y
RUN pip install requests scrapy tinydb munch flask-cors flask_apscheduler sparkpost

COPY ./app /app
COPY ./data /data
COPY ./frontend/dist /app/static
