#!/usr/bin/env bash

docker build . -t ghibli-scraper && docker run -d -p 8000:8000 ghibli-scraper
