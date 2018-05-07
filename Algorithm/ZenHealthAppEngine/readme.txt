## Introduction

This is a simple sample that shows how to:

- Create a Google App Engine service on Google Cloud Platform that loads a pickled scikit-learn model from Google Cloud Storage, and use it to serve prediction requests through Google Cloud Endpoints.  See the accompanying [blog post](https://cloud.google.com/community/tutorials/appengine-serve-machine-learning-model).

The benefits of this configuration include:

1. App Engine's autoscaling and load balancing.
1. Cloud Endpoints' monitoring and access control.


## Requirements

- Install [Python](https://www.python.org/).  The version (2.7 or 3) used for local developement of the model should match the version used in the service, which is specified in the file `app.yaml`.

- Install [Google Cloud Platform SDK](https://cloud.google.com/sdk/).  The SDK includes the commandline tools `gcloud` for deploying the service and [`gsutil`](https://cloud.google.com/storage/docs/gsutil) for managing files on Cloud Storage.

- Create a Google Cloud Platform project which as the following products enabled:

    - [Google App Engine](https://cloud.google.com/appengine/)

    - [Google Cloud Storage](https://cloud.google.com/storage/)

    - [Google Cloud Endpoints](https://cloud.google.com/endpoints/)

## steps:

- gcloud endpoints services deploy modelserve.yaml : to deploy gcloud endpoints

- to get config ids from endpoints:
    gcloud endpoints configs list --service="modelserve-dot-zenloop-202821.appspot.com"
    => CONFIG_ID     SERVICE_NAME
    2018-05-04r0  modelserve-dot-zenloop-202821.appspot.com

- bucket_anme should be all small
    gsutil mb gs://BUCKET_NAME
    gsutil cp lr.pkl gs://BUCKET_NAME


##Clean services

- gcloud app services delete modelserve

- gcloud endpoints services delete modelserve-dot-zenloop-202821.appspot.com

tfidf , countvectorization


