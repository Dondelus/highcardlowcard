# The base image for the project, let's keep it as small as possible for something so simple.
FROM python:3.7.1-slim

# Let's create a label for future image referencing
LABEL maintainer="Cameron"

# Make sure that we have all of our final copied into the container... (duh)
COPY . /highlow

# The starting point for our application
WORKDIR /highlow

# We might update a path variable here based on any executables we made need here, I'll leave it commented out
# ENV PATH $PATH:/usr/lib/local/bin:/usr/local/lib/python3.7/site-packages

# Update packages.  It's probably not necessary here since we have no real dependencies, but in case we needed to
# use some sort of apt-get package, this might be useful here.
# We're also installing any requirements our application may have with pip
RUN apt-get update -y && \
    pip install -r requirements.txt 

# Here, I would normally expose any ports that might be necessary i.e. 5000 for a flask api

# Let's start up our high-card, low-card application
CMD ["python", "highlow.py"]

