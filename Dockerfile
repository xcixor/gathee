# Base Image
FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888
ENV DATABASE_NAME="dcelpj42i0pafq"
ENV DATABASE_USER="puvkblmaltrngy"
ENV DATABASE_PASSWORD="6c050278a137e937a7ecc45c7ce88c24cbfe516bd01b8437890e0769f9c26563"
ENV POSTGRES_IP="127.0.0.1"
ENV TWILIO_ACCOUNT_SID=AC0d68879d3fea1077ca56886824416583
ENV TWILIO_AUTH_TOKEN=cec0e6c3559978227e4c2f3cd63a20db
ENV SECRET_KEY='f3n*ds2#3y#jk3w%*=0hc1^gtl@@*s*r(g+thfu%pjuaz43vum'
ENV DJANGO_SETTINGS_MODULE=core.settings.development
ENV EMAIL_HOST='smtp.sendgrid.net'
ENV EMAIL_HOST_USER='gathee'
ENV EMAIL_HOST_PASSWORD='gathee2019'

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888
CMD gunicorn cfehome.wsgi:application --bind 0.0.0.0:$PORT