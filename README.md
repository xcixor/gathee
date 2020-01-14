# [Gathee](http://production.nyotamusicacademy.com/)

[![](https://img.shields.io/badge/Protected_by-Hound-a873d1.svg)](https://houndci.com) [![Maintainability](https://api.codeclimate.com/v1/badges/988f7f01d9bb391751b1/maintainability)](https://codeclimate.com/github/xcixor/gathee/maintainability) [![Coverage Status](https://coveralls.io/repos/github/xcixor/gathee/badge.svg)](https://coveralls.io/github/xcixor/gathee)


## About Environment Variables
Environment variables are use key, value objects that hold certain data needed by applications such as database passwords and directory paths.
In the development of this app, environment variables have been used to make the work of the developer more dynamic, by enabling him to not only hide sensitive information from the public, but also run the application in different configurations.
The following is a list of the required environment variables that the developer/user/you needs to explicitly set to run the app.

### Local environment variables
This are variables that the app cannot run without and need to be set on the local machine where the app is being hosted. Conventionally, each variable can be export manually using the ```export``` command but its much faster and flexible to place all the variables in a **.env** file and the batch exporting them as explained in the steps below:
- Create called *.env* and place it in the root of your working folder
- Add the following environment variables, replacing the descriptions with the actual variables
    - export POSTGRES_IP="The IP address of where your database is being hosted eg 127.0.0.1 for local hosting"
    - export DATABASE_NAME="Name of app's database"
    - export DATABASE_USER="The authorised user of the db"
    - export PORT=5432
    - export HOST="Same as Postgres Ip"
    - export DATABASE_PASSWORD=""
    - export SECRET_KEY='Secret Key for securing data in the app'
    - export DJANGO_SETTINGS_MODULE="The environment being used for running the app e.g core.settings.development"
    - export GS_BUCKET_NAME="Name of gcp bucket hosting images for the app, only necessary in staging and production environments"
    - export GS_BUCKET_URL="Url of the bucket, get this from the gcp account where the bucket was created"
    - export SERVICE_ACCOUNT='Credentials for gcp, only required in production and staging environments'
    - export GOOGLE_APPLICATION_CREDENTIALS="The file path location for the service account"
    - export EMAIL_HOST='Email provider'
    - export EMAIL_HOST_USER='Email host account'
    - export EMAIL_HOST_PASSWORD='gEmail host account password'
    - export TWILIO_ACCOUNT_SID="Twilio account SID get from twilio account"
    - export TWILIO_AUTH_TOKEN="Twilio auth token"


### Circle CI
As in the local machine you will need to add the above environment variables for circle ci tests to pass. In addition, further variables will be required to host the app on gcp. They include the following:

- COVERALLS_REPO_TOKEN
- INTEGRATION_ENVIRONMENTAL_VARIABLES
- PRODUCTION_ENVIRONMENTAL_VARIABLES
- STAGING_ENVIRONMENTAL_VARIABLES

#### N:B integration, production and staging environment variables
The variables, **INTEGRATION_ENVIRONMENTAL_VARIABLES**, **PRODUCTION_ENVIRONMENTAL_VARIABLES**, and **STAGING_ENVIRONMENTAL_VARIABLES** are required in hosting the app in gcp under different environments. These are almost similar to the variables required for hosting the app with a few difference. They include the following.

- region="us-central1"
- zone="us-central1-b"
- project="Project Id consult gcp account"
- ip_address="Reserved Ip address in gcp account"
- database_name=""
- database_user="
- database_password=""
- postgres_ip=""
- application_host="the hosting address eg integration.nyotamusicacademy.com"
- gs_bucket="gs bucket name"
- gs_bucket_url="bucket url"
- network="default"
- compute_instance_name="name of the instace to create, should be unique eg integration for integration environment"
- image_name="Consult gcp account"
- twilio_account_sid=""
- twilio_auth_token=""
- email_host=""
- email_host_user=""
- email_host_password=""

Copy these variables as they are, including the quotes and without changing the case but removing the bullets into a txt file such as **integration_vars.txt**.

So that the variables can be properly parsed when creating the gcp infrastructure, you need to encode the variables and copy the encoded string to circleci in the following steps.

- **Encode the variables with the following comand.**

    ```base64 integration_vars.txt > integration_encoded_vars.txt ```

- **Copy the generated string in *integration_encoded_vars.txt* to circle ci as the value for *replace with appropriate environment*_ENVIRONMENTAL_VARIABLES .**

It is also important to note that the develop branch is associated with staging while the master branch is associated with production ennvironment, other branches are considered for integration purposes. While you will not be required to explicitly set the branch, naming conventions should be observed eg, the *application_host* when deploying master should be production.nyotamusicacademy.com
