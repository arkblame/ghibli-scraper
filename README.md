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

## How to run
### docker
You would need to install *Docker*

After that run `start-docker.sh` to start server. It will be available at: 
http://localhost:8000/movies

### tests
1. Install python 3.7 or higher
2. Install requirements by running `pip install -r requirements.txt`
3. Run script `run_tests.sh`
