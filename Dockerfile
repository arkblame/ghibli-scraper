FROM python:3.8-alpine

EXPOSE 8000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN sed -i "s/flask.ext.cache/flask_cache/" /usr/local/lib/python3.8/site-packages/flask_cache/jinja2ext.py

COPY . /app

CMD [ "python" , "/app/main.py" ]
