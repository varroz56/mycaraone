# mycaraone {#title}

An easy to use and responsive app to rent motorhomes.

## Where Can I see it?
The source code can be found [here](https://github.com/varroz56/mycaraone) on Github. 
The Deployed verion is on the [MyCaraOne](http://mycaraone.herokuapp.com) site.


## UX {#UX}

The aim of this project to offer more convenient ways to rent motorhomes. Both the user and motorhome data generalized and stored in a single database. 

 The initial documentation have been uploaded to the [docs folder](docs). Wireframes can be found in the [wireframes folder](docs/wireframes).

### User Stories

The planned User Stories can be found in the docs [here](./docs/UserStories/UserStories.xlsx)
This section shows the ways how users can use the site and what options present for them in order to accomplish their goals.
The most important part is that the authentication and payment system separate them to 3 parts and these are the following access levels:
- Visitor A landiing on the page, can see the motorhomes listings, the detailed page and the home page where can contact the Team by submitting the contact form.
- - The contact form can be found on the landing page. It is located at the bottom of the page. The home page can be accessed from any other pages by clicking on the Home or Logo buttons on the top left corner.
- - The Motorhomes page can be access in two ways, one link from the home page body link and the other link can be accessed from any page as it is located on the navbar right side
- - The motorhome detailed page can be accessed by clicking on the selected Motorhome in the motorhome listing. The Listing cards change their size on hover to show that there is an available action for this.

- - Available pages are the sign in and register pages these are located both on the home page and on the navbar
- - When a visitor is trying to access a restricted page this will redirect them to the login page.

- Registered B can do everything what visitors plus:
- - On the profile page can add quick contact details and a profile picture
- - and also can create, read, update and delete a billing address
- - - The Billing address enchanced using Google Maps API and also autocomplete form for their convenience
- - Can Book motorhomes and can see their booked motorhomes with some information about their bookings
- - can access the logout option
  
- Registered C who also completed the checkout process can access the checkout success page where can see the summary about their booking

- The links are hidden from the users whos access level is lower then the reuired except the book this motorhome button what redirects to the login page.

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
14.  - [x] Deployment to Heroku
15.  - [x] Final testing
16.  - [x] fixing issues
17.  - [] Project submission 

## Technologies used
- [Python](https://python.org)
- [Django](https://www.djangoproject.com/) a python based framework
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/) for user authentication
- [Bootstrap](https://getbootstrap.com/) for styling
- [Font Awsome](https://fontawesome.com/) for extra styling(icons)
- [Google Places API](https://cloud.google.com/maps-platform/) for the billing address form (it is in the version control, however it is restricted to the MyCaraOne site and also to thsis API)
- [Stripe](https://stripe.com) for online card payments
- [Javascript](https://www.w3schools.com/js/js_intro.asp) for manipulating the elements on the page and handling async requests
- [HTML](https://www.w3schools.com/html/) the markup language for the site
- [CSS](https://www.w3schools.com/Css/) for styling the the HTML elements
- [Googole fonts](https://fonts.google.com/) where the 'Yusei Magic' font hosted
- [PIP](https://pypi.org/project/pip/) for python package management
- other packages are listed in the [requirements.txt](./requirements.txt) file.
- [PostgreSQL](https://www.postgresql.org/) as the deployed database
- [AWS S3](https://aws.amazon.com/s3/) for storing static and media files
- [Heroku](https://heroku.com) to host the site and also the DB

- [VSCode](https://code.visualstudio.com/) as code editor
- [GIMP](https://www.gimp.org/) for editing images
- [OnlineFavicon](http://onlinefavicon.com/) to created the favicon
- [Github](https://github.com) for hosting the source code and its previous versions
- [Git](https://git-scm.com/) for version controll

- [MS Office](https://office.com) for text/and other document editing


## Not implemented but planned features

- Multilingual UI
- More information about the bookings, to separate paid and confirmed bookings
- To be able to manage bookings after created through the app
- To be able to communicate to other users(blog style) to share pictures and experience

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

- when deployed to Heroku, started testing the deployed project.


## Local set up

Steps:
- Clone/Download the repo or open it [Gitpod](https://gitpod.io) from the repo [page](https://github.com/varroz56/mycaraone)
- To clone/download this can use the repo page or the Gihub CLI or the git command prompt.


- Once opened locally, it is advised to cerate a virtual environment usin the "python3 -m venv venv" command. With this the installed packeges are containerized and will not affect other projects.
- Activate the virtual env with teh "source venv/bin/activate" select the correct python interpreter and then if PIP is not installed, nned to install it form [here](https://pypi.org/project/pip/).
- The reuirements.txt and the manage.py are located in the same folder. Navigate into this folder and the use "python3 -m pip install -r requirements.txt" to download and install the required packages.
- Once installed every package need to check the [settings.py](./project_mycaraone/settings.py) and where an env var has been used need to provide one.
- Once all set
- use "export DEVELOPMENT=True" commanmd to set the services to local(also by not setting the USE_AWS anv var to True) and then "python manage.py runserver"

Every technology used are referenced in the Technologies Used section.

## Testing
The project was tested since the start of the project, however automated testing only applied at the end. A separate document was created to describe the test methods and results [here](./docs/testsdoc/MyCaraOneTests.docx).
Also ran through [CSS vaildator](http://jigsaw.w3.org/) and fixed the issues(some issues are related to the BS5 ne classes)
And checked it with [HTML validator](https://validator.w3.org/) and fixed the issues

## Credits
Default user profile pictures downloaded from [Flaticon](https://www.flaticon.com/free-icons/profile)
The motorhomes images and some (not 100% accurate) information was donwloaded from: [Elnagh](https://www.elnagh.com/00-en/Pagina/Index/413), [Poessl](https://www.poessl-mobile.de/en/models), [Roadcar](https://www.poessl-mobile.de/en/models) and [Mobilvetta](https://www.mobilvetta.it/00-en/) sites.
The Webhooks part is from the course content from [CodeInstitute](https://codeinstitute.net)
The Stripe js part following the course content but it is customized to the project needs.
The course content cleared and helped a lot when started to do things in the wrong order

