FROM bobbystearman/hedera-py-java

### 1. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKERIZE_VERSION v0.6.1

### 2. Setup GDAL
RUN apt-get update &&\
    apt-get -y install gettext ;\
    apt-get -y  install httpie; \
    apt-get install -y binutils libproj-dev gdal-bin python3-gdal


### 3. Add dockerize to allow waiting for the DB to load.
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

### 4. Create working directory
RUN mkdir /code
COPY . /code/
WORKDIR /code

### 4. Install packages
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r /code/requirements/dev.txt ;

### 5. Expose port
EXPOSE 8000