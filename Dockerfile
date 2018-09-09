FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev -y
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests scrapy tinydb munch

COPY . .

CMD [ "python", "./main.py" ]
