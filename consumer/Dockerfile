FROM python:3

MAINTAINER Jardel Pereira Zermiani

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD . .

CMD ["python", "app.py"]
