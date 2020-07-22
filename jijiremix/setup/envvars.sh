#!/bin/bash
# Local development env vars 
export DEBUG='1'
export LOCAL_DEPLOY='1'
export SITE_ID='1'

# export DATABASE_NAME='jijiremix_db'
# export DATABASE_USER='jijiremix_user'
# export DATABASE_PASS='password'

export SECRET_KEY='teaf_w0vke2yz7zvig-h*sl-v^t!gyvawmoeii0or2apclzgbu'


export EMAIL_USE_TLS='1'
export EMAIL_HOST='smtp.example.com' 
export EMAIL_HOST_PASSWORD='my_secret_password'
export EMAIL_HOST_USER='email@example.com'
export DEFAULT_FROM_EMAIL='email@example.com'
export EMAIL_PORT='123'

# Remote deployment extra env vars
# export ALLOWED_HOSTS='example.com'
# export AWS_ACCESS_KEY_ID='amazon_key'
# export AWS_SECRET_ACCESS_KEY='amazon_secret'
# export AWS_STORAGE_BUCKET_NAME='abidria-bucket'
# export DATABASE_URL='postgres://amazonaws.com'