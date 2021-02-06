# mycaraone {#title}

An easy to use and responsive app to rent motorhomes.



## UX {#UX}

The aim of this project to offer more convenient ways to rent motorhomes. Both the user and motorhome data generalized and stored in a single database. 

 The initial documentation have been uploaded to the [docs folder](docs). Wireframes can be found in the [wireframes folder](docs/wireframes).

### User cases

 User A 

## Project milestones

1. - [x] Project planning
2. - [x] Initial docs
3. - [x] Wireframes
4. - [x] Project setup
5. - [x] Allauth integration
6. - [x] email service integration
7. - [x] User profile app and user page setup
8. - [x] CRUD on user secondary information
9. - [x] Home app with contact form
10. - [x] Motorhomes app and listings
11. - [x] Booking app and Rent/Booking page
12. - [x] Checkout app and payment page
13. - [x] My Bookings app and bookings page
14.  - [] Deployment to Heroku
15.  - [] Final testing
16.  - [] fixing issues
17.  - [] Project submission 

## Technologies used
- [Python](https://python.org)
- [Django](https://www.djangoproject.com/) a python based framework
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/) for user authentication
- [Bootstrap](https://getbootstrap.com/) for styling
- [Font Awsome](https://fontawesome.com/) for extra styling(icons)

## User Stories
This section shows the ways how users can use the site and what options present for them in order to accomplish their goals.
The User Stories section have been uploaded to the [UserStories folder](docs/UserStories).

## Deployment
Created app on [Heroku](https://heroku.com):
- After registration, from the dashboard New option created new app called mycaraone.
- set the region to europe
- installed [dj-database-url](https://pypi.org/project/dj-database-url/) to easily connect to the remote DB.
- installed [psycopg2](https://pypi.org/project/psycopg2-binary/) as will use postgres DB
- created requirements.txt file with python3 -m pip freeze >> requirements.txt command to translate the required packages to heroku
- from Heroku Resources created a free Heroku-Postgres instance
- set up database connection using the URI provided by Heroku
- ran migrations as this needs to be set up on the new remote DB
- with python manage.py showmigrations verified migrations
- with the loaddata command added the modelinstances
- installed [gunicorn](https://pypi.org/project/gunicorn/) as the webserver
- created Procfile to translate the app to Heroku
- in Heroku settings added the env vars
- installed the Heroku CLI (usinng pip)
- uesd [heroku config:set DISABLE_COLLECTSTATIC=1](https://devcenter.heroku.com/articles/django-assets)
- added allowed hosts in settings
- [set up git remote](https://devcenter.heroku.com/articles/git) from the heroku CLI
- deployed to Heroku
- [set automatic deployment](https://devcenter.heroku.com/articles/github-integration) when pushed to [Github](https://github.com) from Heroku 

- Set up [amazon aws services](https://console.aws.amazon.com/) to host the project static files
- created publick bucket, set up [hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html) and will use the bucket's endpoint to access the files.
- set [CORS permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/ManageCorsUsing.html)
- set up bucket policy using aws [policy generator](https://awspolicygen.s3.amazonaws.com/policygen.html) and amend to allow all resources from mycaraone
- amend ACL to allow list obj for everyone
- cerated user groups and assigned access policy to it and created user with access keys
- installed [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) an AWS SDK
- installed [djang-storages](https://django-storages.readthedocs.io/en/latest/) to help with the storage backend
- created custom_storages file to configure boto3 and describe the static and media files location
- in settings, set up aws backend and overridden file path for static and media files
- enabled collect statics
- added cache settings
## Credits
Default user profile pictures downloaded from [Flaticon](https://www.flaticon.com/free-icons/profile)