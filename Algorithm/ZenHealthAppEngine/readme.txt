## Introduction

This is a simple sample that shows how to:

- Create a Google App Engine service on Google Cloud Platform that loads a pickled scikit-learn model from Google Cloud Storage,
and use it to serve ML requests through Google Cloud Endpoints.


The benefits of this configuration include:

1. App Engine's autoscaling and load balancing.
1. Cloud Endpoints' monitoring and access control.


## Requirements

- Install [Python](https://www.python.org/).  The version (2.7 or 3) used for local developement of the model should match
    the version used in the service, which is specified in the file `app.yaml`.

- Install [Google Cloud Platform SDK](https://cloud.google.com/sdk/).  The SDK includes the commandline tools `gcloud` for
    deploying the service and [`gsutil`](https://cloud.google.com/storage/docs/gsutil) for managing files on Cloud Storage.

- Create a Google Cloud Platform project which as the following products enabled:

    - [Google App Engine](https://cloud.google.com/appengine/)

    - [Google Cloud Storage](https://cloud.google.com/storage/)

    - [Google Cloud Endpoints](https://cloud.google.com/endpoints/)

## steps:

Set up a Cloud Platform project, install required software, and create an App Engine app. See Before you begin.
Download the sample code. See Getting the sample code.
Configure the openapi-appengine.yaml file, which is used to configure Endpoints. See Configuring Endpoints.
Deploy the Endpoints configuration to create a Cloud Endpoints service. See Deploying the Endpoints configuration.
Create a backend to serve the API and deploy the API. See Deploying the API backend.
Send a request to the API. See Sending a request to the API.
Track API activity. See Tracking API activity.
Avoid incurring charges to your Google Cloud Platform account. See Clean up.

#---------------------------------------------------------------------------------------------------------------------------
## Cloud SDK

- open gcloud SDK
- gcloud auth login
-  gcloud config set project PROJECT_ID
#---------------------------------------------------------------------------------------------------------------------------
##endpoints
- gcloud endpoints services deploy zenloopserve.yaml : to deploy gcloud endpoints

- to get config ids from endpoints:
    gcloud endpoints configs list --service="zenloopserve-dot-zenloop-202821.appspot.com"
    => CONFIG_ID     SERVICE_NAME
    2018-05-04r0 *.appspot.com




##Clean services

- gcloud app services delete zenloopserve

- gcloud endpoints services delete zenloopserve-dot-zenloop-202821.appspot.com

tfidf , countvectorization


#---------------------------------------------------------------------------------------------------------------------------
##cloud storage

- bucket_anme should be all small
    gsutil mb gs://BUCKET_NAME
    gsutil cp lr.pkl gs://BUCKET_NAME

#---------------------------------------------------------------------------------------------------------------------------
## App engine deployement

- gcloud app deploy

-  gcloud app browse

-gcloud app browse -s serve

#---------------------------------------------------------------------------------------------------------------------------
## run locally cloud SQL on gclous sdk

- download cloud proxy (Right-click https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe and select "Save link as..." to
    download the proxy, renaming it to cloud_sql_proxy.exe.)

- /cloud_sql_proxy -instances=<INSTANCE_CONNECTION_NAME>=tcp:3306

 - ./cloud_sql_proxy -instances=<INSTANCE_CONNECTION_NAME>=tcp:3306 \
                  -credential_file=<PATH_TO_KEY_FILE> &
#---------------------------------------------------------------------------------------------------------------------------
## clooud SQL configuraiton

- app.yaml file
    env_variables:
        # Replace user, password, database, and instance connection name with the values obtained
        # when configuring your Cloud SQL instance.
        SQLALCHEMY_DATABASE_URI: >-
          mysql+pymysql://USER:PASSWORD@/DATABASE?unix_socket=/cloudsql/INSTANCE_CONNECTION_NAME

      beta_settings:
    cloud_sql_instances: INSTANCE_CONNECTION_NAME

- requirements.txt

    Flask==0.12.2
    Flask-SQLAlchemy==2.3.2
    gunicorn==19.7.1
    PyMySQL==0.8.0

- .py file

    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ['SQLALCHEMY_DATABASE_URI']

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#---------------------------------------------------------------------------------------------------------------------------
## clooud compute engine

- sudo apt-get install python-setuptools

- sudo easy_install flask markdown

- sudo python -m SimpleHTTPServer

- sudo apt-get install supervisor

- sudo service supervisor status

- sudo supervisorctl reread

-sudo supervisorctl update

-sudo supervisorctl restart uni_app








