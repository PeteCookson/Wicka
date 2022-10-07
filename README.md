# **WICKA**
## The luxury, locally sourced arrival hamper company

This website is designed and created for the Full Stack Frameworks with Django Milestone Project, for Code Institute's Diploma in Web Application Development.
The objective for this milestone project is to plan, design and develop a project with all the functionalities to work as an fully operational e-commerce website.

WICKA - Is a luxury hamper delivery company that creatively sources locally sourced products, carefully packages them to be delivered to the Airbnb, ready for the guests arrival.

("Responsive Mockup")

**View live version of [website](https:/wicka.herokuapp.com/)**

<br>
<hr>

<a></a>
## Table of Contents 
* [UX](#ux)
    * [Strategy](#strategy)
        * [Site Owner Goals](#site-owner-goals)
        * [External User Goals](#external-user-goals)
        * [Returning User Goals](#returning-user-goals)
    * [Scope](#scope)
    * [Structure](#structure)
        * [Database](#database)
    * [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
    * [Surface](#surface)
        * [Colour Palette](#colour-palette)
        * [Typography](#typography)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
    * [Technologies Used](#technologies-used)
        * [Languages](#languages)
        * [Libraries](#libraries)
        * [Tools](#tools)
        * [Design](#design)
    * [Bugs & Testing](#bugs-and-testing)
    * [Deployment](#deployment)
    * [Credits](#credits)

<br>
<hr>

<a name="ux"></a>
## **UX**
<a></a> 

<a></a>
## **Strategy**
--- 
#### **Site Owner Goals**
The website will target users who are use Airbnb and short break style accommodation who want to enhance their stay with a hamper of locally sourced products delivered prior to their arrival. The primary focus is on providing an easy to navigate and responsive e-commerce website that allows users to easily purchase products.  

#### **User Goals**
- View and be able to easily purchase products easily and securely.
- Process payments to pay for products. 
- Visual order confirmation after checkout to see purchase. 
- Order processed correctly even if the internet drops during transaction.
- Register and confirm email address to receive purchase notification.
- Add and remove items from the basket with update to the total.
- View and search blogs, as well as leave comments.

#### **Admin Goals** - As an administrator, I want to have the same permissions as as registered users, but also want to:
- Have full access the admin dashboard to view all users, products and manage other information of the e-commerce store.
- To be able to post, edit and delete Blogs. 

<a></a>
## **Scope**
---
In order to complete the project in time for the deployment and submission deadline, functions of less importance will not be implemented in the first release of project, below are the main features to be impletmented for the project:

- Landing Page displaying navbar with login, basket and menu items, hero image and footer elements contain contact information and social links
- Products page linkng directly to add to basket button
- Basket page showing products to be purchased, with abilty to remove items.
- Checkout page where the total cost including shipping costs, delivery details, and card payment input using Stripe.
- User profile page where logged in user can view previous order information and update profile details
- Blog page featuring search function, and ability to comment for logged in users.
- Admin priveleges (to manage products and content)
- Brief page on the Wicka story, vision and ethos.

Features for future releases:

-  Affiliate scheme for hosts through a host_user login, offering discounts for their guests, and earning through their purchases.
-  Referral scheme where guests can earn credit on their account for reffering new customers.
- Location based products.
- Working with us, Suppliers, FAQ's, Terms and conditions
- Postcode delivery checker

[Click here](/readme_assets/flow_%20chart.png) to view the Flow Chart

## **Structure**
---
### **Data Structure**
A database structure was designed to be specifically suited for Wicka. It was important to make sure the data structure was logical. Each product is identified by a unque sku

Each order has a unique order number which is generated when the order is processed and orders have the users and product details.

Users have the option to purchase products as guest users or as registered users. Guest users can complete the order process but their details will not be saved, they won’t be able to see a Profile with their details, order history and shipping address etc. A Registered user will not only have access to their Profile but will also have their details pre-populated the next time they shop. 

SQLite, which is Django built-in database is used for development mode and Heroku Postgres is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

### **Database**
A database structure was designed to be specifically suited for Saran Collection. It was important to make sure the data structure was logical. Each product is linked to a category and these are identified by id (pk number). 

Each order has a unique order number which is generated when the order is processed and orders have the users and product details.

Users have the option to purchase products as guest users or as registered users. Guest users can complete the order process but their details will not be saved, they won’t be able to see a Profile with their details, order history and shipping address etc. A Registered user will not only have access to their Profile but will also have their details pre-populated the next time they shop. 

SQLite, which is Django built-in database is used for development mode and Heroku Postgres is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

## **Skeleton**
---
### **Wireframes**
[Adobe XD](https://adobexd.com/) was used to create high-fidelity wireframes., the designs were used to make the coding process easier, havng made all the important desisions about layout, fonts, colours and buttons ets. 
<details><summary>Desktop</summary>

![desktop](/readme_assets/desktop.png)

</details>

<details><summary>Mobile</summary>

![mobile](/readme_assets/mobile.png)

</details>
<br>

## **Surface**
---
### **Colour Palette**

The colors used throughout the webite have been chosen to reflect a clean, natural and fresh feel to tie in with the brands ethos, of delivering locally sourced, ethical hampers.
[Coolors](https://coolors.co) was used to create the colour palette.
<details><summary>Colour Palette</summary>

![Colour Palette](/readme_assets/palette.png)

</details>
<br>

### **Typography**

The website uses the [Google Fonts](https://fonts.google.com/) library to provide the fonts, Raleway is used for the logo, lato and merriweather are used in combination for headings, labels and body copy.

<details>
<summary>Typography</summary>

![Typography](/readme_assets/)

</details>
<br>

## **Existing Features**
---
## **Future Features**
---
## **Technologies Used** 
---
### Languages

The primary languages used throughout the development of this project are:

* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Python3](https://www.python.org/downloads/)
* [JavaScript](https://www.javascript.com/)

### Libraries
- [Bootstrap4](https://getbootstrap.com/) for simplify the structure of the website
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Hover.css](https://cdnjs.com/libraries/hover.css/2.1.0) to apply hover effects to the projects navbar.
- [Django](https://www.djangoproject.com/) (an open-source web framework) as the main framework of Python
- [SQLite](https://www.sqlite.org/index.html) (Django built-in database) as a database in development mode
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) (Heroku built-in) as a database in production mode
- [Stripe](https://stripe.com/en-ie) for credit card payment
- [AWS](https://aws.amazon.com/) (Amazon Web Services) for hosting static files and images for the website
### Tools
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website
- [Responsinator](http://www.responsinator.com/) - to determine if the site was responsive to various devices.
- [Am I Responsive](http://ami.responsivedesign.is/#) to view images of the website on different devices if the site was responsive to various devices.
- Chrome DevTools to help edit pages and diagnose problems quickly.
- [W3C Markup Validator](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [JSHint Validator](https://jshint.com/) for detecting errors and potential problems in your JavaScript code
- [Link Checker](https://validator.w3.org/checklink) for checking all links on the website and see if all links work
- Lighthouse in Google dev tool for testing the performance of the website
- [PEP8 Online](http://pep8online.com/) for checking Python code syntax
- [Grammerly](https://www.grammarly.com/) to check spelling & grammer
- [Notion](https://www.notion.so) for project planning and tracking
- [Datagrip](https://www.jetbrains.com/datagrip/?source=google&medium=cpc&campaign=15034927837&term=datagrip&gclid=Cj0KCQjw6_CYBhDjARIsABnuSzp0LpwQpmCHmvcBxdM9YTyefXuJn_rgE3zlOPdBMWTi9vvJv_mzOHIaAiUeEALw_wcB) to print out the data strucutre 
### Design
- [Adobe XD](https://adobexd.com/) used for wireframe and mockups
- Illustrator
- Photoshop
- Principle

### Other Technologies
- Squoosh

## **Bugs and Testing**
Bugs & Testing information can be found in the seperate [bugs & testing](/TESTING.md) file.

## **Deployment**
This project uses GitHub for version control, GitPod as the cloud-based IDE and Heroku to deploy the site into production. Heroku Postgres is used for the database. [AWS services](https://aws.amazon.com/), which is also a cloud-based platform, is used to store static files and images as Heroku has [no files system to store new files]().

The below steps are specific to Gitpod therefore depending on your IDE, you might need to adjust the below steps. 

### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/Franciskadtt/happybean.git
```

#### To install required software:
While you are still in the terminal, type pip3 install -r requirements.txt, this will install all the required softwares to run the project:
```
pip3 install -r requirements.txt
```

#### Setup an enviroment for variables
You now need to set up the database with environment variables. Create a file titled env.py and make sure it is placed in the of this file structure, on the same level as the app.py file. You can also add these in your workspace variable section. 

Option 1: Env.py file:
```
 os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('DEVELOPMENT', 'True')
 os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your_variable_here>')
 ```
- In ` settings.py`  add:
```
if os.path.exists("env.py"):
    import env
```
-  Add your env.py file to `.gitignore`, before pushing your changes.


<br>Option 2: Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_CH', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_SUB', VALUE = '<your_variable_here>'
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

- In ` settings.py`  add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = 'DEVELOPMENT' in os.environ
```

### **Heroku Deployment**
- Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
- Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
- In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
- Search for your repo (or sign in and connect GitHub account) and select this.
- Then click "Hide Config Vars" in Heroku.
- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the `settings.py file`, you will need to comment out the 'SQLite and Postgres databases' section and uncomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet).
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
- Create a superuser with the following command, and fill in the required information.:
    ```
    python3 manage.py createsuperuser
    ```
- In the `settings.py` file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Install gunicorn and freeze that to the requirements file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
- Create a Procfile and inside, add the following:
    ```
    web: gunicorn happybean.wsgi:application
- In `settings.py`, use an if statement so that when the app runs on Heroku, you will connect to Postgres, and otherwise, it will connect to sqlite3, like so:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
- Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    ```
- Login to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app happybean
    ```
- Add your Heroku app and local host to allowed hosts in `settings.py.`
- Push to Github, and then to Heroku master. 
- In Heroku, go to the 'Deploy' tab. In the section 'Deployment Method' click on 'Github - Connect to Github'. Make sure your Github profile is displayed. Add the repository name and click on 'Search'. After Heroku has found the repository, click on 'Connect'. This will connect your Heroku app to your GitHub repository. Click 'Enable automatic deploys'. Your code will automatically be deployed to Heroku as well. 

### **AWS (Amazon Web Services)**
Create an account with [AWS](www.aws.amazon.com), follow the steps and sign in. 
- Go to the AWS management console and go to the S3 service. There, create a new bucket. Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Go to the buckets properties, and turn on static website hosting. Select 'Use this bucket to host a website', and fill in index.html and error.html, then click 'save'.
- Go to the permissions tab, and go to CORS configuration. Paste in a CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Go to the Bucket policy tab and click 'policy generator', to create a policy. Choose 's3 bucket policy', allow all principals by typing a star. From the action dropdown menu select 'GetObject'. Copy the ARN and paste it into the ARN box. Then click 'add statment' and then click 'generate policy'. Copy the policy into the bucket policy editor. Add a slash star onto the end of the resource key. Click 'save'. 
- Go to access control list tab, under public access, click on 'Everyone', select 'List Objects'. Then click 'save'. 
- Go to IAM (from services menu), click on 'groups' and create a new user group. Give the group a group name (f.e. 'manage-happybean'). Then click 'create group'. 
- Click 'policies' in the dashboard, and then click 'create policy'. Go to the JSON tab. Click 'import managed policy'. Import 'AmazonS3FullAccess'. Get the bucket ARN from the bucket policy page in S3, and paste that in after 'Resource', as a list (first the ARN, then also the ARN with a slash and star). Click 'next tags' and then 'next review'. Give it a name and description. Click 'create policy'. 
- Go to 'groups'. Click the manage-happybean group. Go to 'permissions'. Click 'attach policy'. Select the policy you just created. Click 'add permissions' and then 'Attach policy'.
- Go to 'users'. Click 'add user'. As username write 'happybean-staticfiles-user. Give programmatic access. Click 'next'. Add the user to the group. Click through to the end. Download the .csv file. 

### **Connecting to DJANGO to S3**
- Go back to GitPod. Install boto3 and Django storages, and freeze them to the requirement file with the following commands:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
- Add 'storages' to the installed apps in the settings.py file.
- Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'happybean'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
- On Heroku, add the AWS keys to the Config Variables (they can be found in the csv file you downloaded earlier). Also, add USE_AWS and set it to True. 
- Remove the DISABLE_COLLECTSTATIC from the variables. 
- In GitPod, create a file called custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S#Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION 
    ```
- To the before mentioned if statement from above, in settings.py, also add:
    ```
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
- Add, commit and push these changes. If you now go to the bucket, you will see all the static files. 
- Go to your bucket and add a new folder called media. Inside it, click 'upload' and then 'add files'. Then select all the images you'd like to use. Click 'next'. Under 'manage public permissions', select 'grant public read access'.
- On Stripe, add a new webhook endpoint, with the URL of your Heroku app, followed by 
```/checkout/wh/```. Select 'receive all events' and click 'add endpoint'.
## **Credits**

### **Content**
- The copy and text for this website was created by 
- Blogs are taken from [Brandpoint](https://www.brandpointcontent.com/)
- Product descriptions from the following sources:
  

### **Media**
- Logo Illustration is commissioned. 
- Products photos from the following sources:
    
    - Home page images from [Pexels](https://www.pexels.com//)

### **Code**
- Checkout progress: Original code with modifications from: https://bbbootstrap.com/snippets/bootstrap-4-ecommerce-checkout-form-progress-bar-44177913
- Exclude creator field from form https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
- For presenting extra content via context: https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/
- Products app:
    - User permissions: https://bit.ly/3mSsegO
    - Success message in DeleteView: https://bit.ly/3oRYlzG
- Page scroll up javascript feature: Orginal code from with modifications for the project from https://stackoverflow.com/questions/14249998/jquery-back-to-top and https://www.tutorialrepublic.com/faq/how-to-scroll-to-the-top-of-the-page-using-jquery.php 
- Scroll up button and icon Styling: Orginal code from with modifications for the project from https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
- Send email functionality:
    - https://docs.djangoproject.com/en/3.2/topics/email/
    - https://docs.djangoproject.com/en/3.2/topics/forms/
    - https://www.youtube.com/watch?v=w4ilq6Zk-08&list=PLXcnmXd-db_hO1v3SLAzVcNieoS_Tcn-6&index=6

### **Acknowledgements**
- Thanks to my mentor for guiding me throughout this project.
- Code Institute Tutors for giving me a guidance on how to solve issues.
- Slack

#### Back to [top](#table-of-contents)
