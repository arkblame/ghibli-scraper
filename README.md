# Ghibli scraper
## Short description
This web app is gathering data from Ghibli studio and present all
movies produced by this studio with corresponding cast.

## Description
This application used API to get data from Ghibli studio.
API documentation is provided here: https://ghibliapi.herokuapp.com/

Site is using browser caching to decrease number of API calls.

Solution implemented here is not perfect, but because of time limit
I choose to use the easiest solution. In less time restrained project
with large number of different users I would use server site caching.
Then every request from different user would use cached value on the server.

I choose docker because there is a small issue in Flask-Cache library. 
It uses old flask extension notification, where to import jinja following line
was used `flask.ext.cache` instead of `flask_cache`. Because of that I'm using
*sed* in `Dockerfile` to change this line.

## How to run
### docker
You would need to install *Docker*

After that run `start-docker.sh` to start server. It will be available at: 
http://localhost:8000/movies
