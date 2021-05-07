# Create a base image for our api with python
FROM python:3

# Authors
MAINTAINER Mateo Garcia Conzales <mgarcia@cifpfbmoll.eu>
MAINTAINER Pau Llinas Amat <pllinas@cifpfbmoll.eu>

# Select the work dir and make a copy of it
WORKDIR /app

COPY . /app

# Install requirements
RUN pip3 --no-cache-dir install -r requirements.txt

# Set environment
ENV FLASK_APP=app.py

ENV FLASK_ENV=development

ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py
CMD ["flask", "run"]