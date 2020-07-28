FROM python:3.8-alpine

EXPOSE 8000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python" , "/app/main.py" ]
