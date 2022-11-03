# [WICKA](https://wicka-hampers.herokuapp.com/)

This website is designed and created for the Full Stack Frameworks with Django Milestone Project, for Code Institute's Diploma in Web Application Development.
The objective for this milestone project is to plan, design and develop a project with all the functionalities to work as an fully operational e-commerce website.

WICKA - Is a luxury hamper delivery company that creatively sources locally sourced products, carefully packages them to be delivered to the Airbnb, ready for the guests arrival.

![Responsive Mockup](/readme_assets/images/responsive.png)

**View the live [website](https://wicka-hampers.herokuapp.com/)**

<br>
<hr>

<a></a>
## Table of Contents 
* [UX](#ux)
    * [Strategy](#strategy)
        * [Site Owner Goals](#site-owner-goals)
        * [User Goals](#user-goals)
        * [Admin Goals](#admin-goals)
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
<br>
#### **User Goals**
*As a guest user*
- View and be able to easily purchase products easily and securely.
- Ability to register or log in to existing account.
- Purchase products. 
- Visual order confirmation after checkout to see purchase. 
- Add and remove items from the basket with update to the total.
- Contact site owner.
- View and search blogs.


*As a Registered returning user*
- Log in using latest saved details.
- Ability to reset password.
- Update acount information and view order history.
- Register and confirm email address to receive purchase notification.
- View, search and leave comments on blogs.
- Log out of account

<br>

#### **Admin Goals** 
- As an administrator, I want to have the same permissions as as registered users
- Have full access the admin dashboard to view all users, products and manage other information of the e-commerce store.
- To be able to post, edit and delete Blogs. 

## **Scope**
---
In order to complete the project in time for the deployment and submission deadline, functions of less importance will not be implemented in the first release of project, below are the main features to be implemented for the project:

- Landing Page displaying navbar with login, basket and menu items, hero image and footer elements containing contact information and social links.
- Products page linking to product details page through details button, from details page add to basket and keep shopping buttons.
- Basket page showing products to be purchased, with abilty to remove items.
- Checkout page where the total cost including shipping costs, delivery details, and card payment input using Stripe.
- User profile page where logged in user can view previous order information and update profile details
- Blog page featuring search function, and ability to comment for logged in users.
- Admin priveleges (to manage products and content)
- Brief page on the Wicka story, vision and ethos.

Features for future releases:
- Affiliate scheme for hosts through a host_user login, offering discounts for their guests, and earning through their purchases.
- Referral scheme where guests can earn credit on their account for referring new customers.
- Location based products.
- Working with us, Suppliers, FAQ's, Terms and conditions
- Postcode delivery checker
- Update to the Blog page to include images and document structure.
- About page to reflect the quality of product, story, vision and ethos.

## **Structure**
---
### **Data Structure**
A database structure was designed to be specifically suited for Wicka. It was important to make sure the data structure was logical. Each product is identified by a unque sku.
Each order has a unique order number which is generated when the order is processed and orders have the users and product details.
Users have the option to purchase products as guest users or as registered users. Guest users can complete the order process but their details will not be saved, they won’t be able to see a profile with their details, order history and shipping details. A Registered user will not only have access to their profile but will also have their details pre-populated the next time they shop. 
SQLite, which is Django built-in database is used for development mode and Heroku Postgres is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

<details>
<summary>Data Structure</summary


![Data Structure](/readme_assets/images/data_structure.png)
</details>
<br>

## **Skeleton**
---
### **Wireframes**

<br>

#### **Low Fidelity**
[Adobe XD](https://adobexd.com/) was used to create the low fidelity wireframes. These simple layouts were used to make the design process and decisions simple and consistant, help to outline the blueprint for web and communicate the projects ideas.

<details>
<summary>Home</summary>

![Wireframe: Home](/readme_assets/wireframes/home.png)
</details>

<details>
<summary>Profile - logged in user </summary>

![Wireframe: Profile](/readme_assets/wireframes/profile.png)
</details>

<details>
<summary>Products </summary>

![Wireframe: Products](/readme_assets/wireframes/products.png)
</details>

<details>
<summary>Product Details </summary>

![Wireframe: Product Details](/readme_assets/wireframes/product_details.png)
</details>

<details>
<summary>Basket </summary>

![Wireframe: Basket](/readme_assets/wireframes/basket.png)
</details>

<details>
<summary>Checkout </summary>

![Wireframe: Checkout](/readme_assets/wireframes/checkout.png)
</details>

<details>
<summary>Checkout Success </summary>

![Wireframe: Checkout Success](/readme_assets/wireframes/checkout_success.png)
</details>

<details>
<summary>Sign In </summary>

![Wireframe: Login](/readme_assets/wireframes/signin.png)
</details>

<details>
<summary>Register </summary>

![Wireframe: Registration](/readme_assets/wireframes/register.png)
</details>

<details>
<summary>Add Products Page - admin</summary>

![Wireframe: Add Products](/readme_assets/wireframes/add_product.png)
</details>

<details>
<summary>Edit Products - admin</summary>

![Wireframe: Edit Products](/readme_assets/wireframes/edit_product.png)
</details>

<details>
<summary>Blog Page </summary>

![Wireframe: Blog](/readme_assets/wireframes/blog.png)
</details>

<details>
<summary>Add a Blog - admin</summary>

![Wireframe: Blog](/readme_assets/wireframes/add_blog.png)
</details>

<details>
<summary>Edit a Blogpost - admin</summary>

![Wireframe: Blog](/readme_assets/wireframes/edit_blog.png)
</details>

<details>
<summary>Add a comment - logged in user</summary>

![Wireframe: Blog](/readme-assets/wireframes/wireframe_comment.png)
</details>

<br>

#### **High Fidelity**
[Adobe XD](https://adobexd.com/) was used to create a high-fidelity mock-up, the designs were used to make the coding process easier, havng made all the important decisions about layout, fonts, colours,buttons and styling. 
<details><summary>Desktop</summary>

![desktop](/readme_assets/wireframes/desktop.png)

</details>

<details><summary>Mobile</summary>

![mobile](/readme_assets/wireframes/mobile.png)

</details>
<br>

## **Surface**
---
### **Colour Palette**

The colors used throughout the webite have been chosen to reflect a clean, natural and fresh feel to tie in with the brands ethos, of delivering locally sourced, ethical hampers.
[Coolors](https://coolors.co) was used to create the colour palette.
<details><summary>Colour Palette</summary>

![Colour Palette](/readme_assets/images/palette.png)

</details>
<br>

### **Typography**

The website uses the [Google Fonts](https://fonts.google.com/) library to provide the fonts Raleway is used for the logo Lato and Merriweather are used in combination for headings, labels and body copy.

<details>
<summary>Body</summary>

![Lato](/readme_assets/images/lato-light.png)
![Merriweather](/readme_assets/images/merriweather-regular.png)

</details>
<details>
<summary>Logo</summary>

![Raleway](/readme_assets/images/raleway.png)

</details>
<br>

## **Existing Features**
---
- Landing Page displaying navbar with login, basket and menu items, hero image and footer elements contain contact information and social links
- Products page linkng directly to add to basket button
- Basket page showing products to be purchased, with abilty to remove items.
- Checkout page where the total cost including shipping costs, delivery details, and card payment input using Stripe.
- User profile page where logged in user can view previous order information and update profile details
- Blog page featuring search function, and ability to comment for logged in users.
- Admin priveleges (to manage products and content)
- Brief page on the Wicka story, vision and ethos.

## **Existing Features**
---
### Elements on all pages:
---
#### Top bar
- The carousel highlights the delivery threshold, sign up link for unregistered users and referrral scheme. 
#### Logo
- Used for brand identity, a clickable link returns the users to the index page.
#### Navbar
- This allows the user to easily navigate the website and find what they are looking for, mobile version uses a 'burger' icon and expands to full navbar options. All users can view links to the following pages.
    - Hampers
    - About
    - Blog
    - Profile
        - View of a user who is **not** logged in:
            - Register
            - Sign In
        - View of a user who **is** logged in:
            - My Profile
            - Log out
        - View of a user who **is** logged in as **Admin** :
            - All views of a user who **is** logged in
            - Product Management
            - Add a blog
    - Basket

#### Testimonial Carousel
- Highlighting the positive feedback from existing customers, using the first name and star rating icons.

#### Footer
- Quick links to Social Media
- Copyright information.
- Contact Information

### Page by Page features:
---
#### Home page (index.html) 
- This is the main page of the website and the shop front. 
- The landing page gives the user an immediate welcome by using a strong hero image and indication of what the site is about.
- There is one CTA buttons to view the hampers which is important as the primary goal of the user is to purchase products.
- The page reinforces the quality of the products with the descriptive slogan.

#### Profile
- This page can only be viewed by a user that is logged in.
- Then if the user logs in or registers successfully they are taken back to the login page to login.
- This page will feature their username at the top to personalise the user experience.
- The user will be able to see their user info, delivery info and order history

#### Log In
- The login page features a simple form where the user can enter either their username or their email address and their password.
- There is helper text under each input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also accompanied by colours to show validation (green for correct and red for incorrect).
- If the user lands on the log in page but realises they don't have an account yet and would like to register, there is a link on the page that will take them to the registration page or they can click on the navbar menu Sign up link.
- The page where users can log in to the website and access the Profile page to see their user info, delivery info and order history
- The form with built-in functionality is created with the Django Allauth package.

#### Hampers
- The pages where users can see all products and sort by a group of categories & category
- If a user clicks on the view details button, it will take them to the product details page.

#### Product Details
- These pages are where the users can see product details and to select the quantity;
- The user will see product detail like Name, Price, Category, and Sizes 
- Users can add a product to the shopping bag.
- The user will also be able to click on a link to go back to the products page
- If a user adds a product to their shopping bag, they are notified and a toast will popup with a summary of what is in their shopping bag then as well as the cost, product info and a link to the shopping bag.

#### Add Product - Admin Users
- This page can only be viewed by the admin user.
- The add products page features a simple form, where the admin user can input the basic information including adding an image for the product
- The admin user will receive validation or error feedback when they enter information in the input field.
- If the user clicks the add product button, it will add the new product to the database.
- If the user clicks on the cancel button it will take them back to the products page.

#### Edit Product - Admin Users
- This page can only be viewed by the admin user.
- The edit products page features a simple form, where the admin user can edit a product in the database
- If the admin user clicked on the Edit product button on the products page then they will be taken to this page. 
- The current product information will be shown and the admin user can change the information and save it. This will update the database with the new information.
- The admin user will receive validation or error feedback when they enter information in the input field.
- If the user clicks on the cancel button it will take them back to the products page.

#### Delete Product - Admin Users
- If the user is an administrator, they will see the option to delete a product.
- If they click it, they will be presented with a confirmation screen and then if they click delete, they can delete the product and the database will be updated.

#### Blog
- The blog page contains a list of blog posts shown in the order of most recently added. The page also has a search box above the blog post where the user can search for a blog post either by title or by a word in the content. 
- Each blogpost has a "read more"-link that when clicked takes the user to the blog details page. 
- For a signed in superuser, there are also two additional links on each blogpost. One for editing, that takes the superuser to an edit blogpost page, and one for delete that takes the superuser for a confirm deletion page.

#### Blog Comment - Logged In Users
- The blog details page contains the entire text content of the blogpost shown, and if the user is signed in to their account a button saying "comment blogpost" is shown. 
- If the user is not signed in, a text informing the user that they has to be signed in to comment is shown instead, along with a link to the login page and a link to the sign up-page to make it easy for the user to login or to create an account if they doesn't have one.

#### Add Blog - Admin Users
- This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). 
- This page contains a form where the superuser can fill in title and content and add a blogpost to the database by clicking "add blogpost". 
- The page also contains a "cancel"-link that leads back to the blogs-page when clicked.

#### Edit Blog - Admin Users
- This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). 
- This page contains a form where the superuser can edit title and content and update a blogpost in the database by clicking "edit blogpost". 
- The page also contains a "cancel"-link that leads back to the blogs-page when clicked.

#### Delete Blog - Admin Users
- This page is shown when superuser clicks the "delete"-link on a blogpost on the blog page. 
- This page only contains a question "Are you sure you want to delete (title of the blogpost) ? and the choices yes or no. Clicking no takes the user back the blogs page and clicking yes deletes the toy from the database.

#### Shopping Bag
- On this page users can view all the selected products and details. Users can update the quantity and there is an option to remove products. There is a button link to a checkout page for the final step of shopping.
- The order total, delivery cost and Total cost is clearly indicated to the user.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience

#### Checkout
- The checkout page is where users can enter their information to process their order. 
- The user can see a summary of their order at the top of the page.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience.
- The user will be able to click on a link to back to their bag if they want to adjust it
- The user will see a clear button/link to go to the next step in the order process which will be the payment page.

#### Payment
- Stripe is used to process the order payment. This is a secured platform for credit card payment.
- The user will see a simple form to fill in their payment information and securely pay. This is reinforced with the Stripe logo and the lock icon.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience.

#### Checkout Success
- The users will see the checkout success page if the payment is a success and the order is processed. Users can see the order number, shipping address and product details. 
- The user will be able to return to the products page.
- At the top of the page, there is an indication of where the user is in the buying/checkout - process for a better user experience.

#### Register
- The sign-up page features a simple form, where the user can input a username, email address and password. The form was kept deliberately simple so that signup has minimum barriers.
- If the user lands on the registration page but realises they already have an account and would like to log in, there is a link on the page that will take them to the login page or they can click on the navbar menu Log in link.
- There is a message to the user about not sharing their information to put the user's mind at ease.

#### Log Out
- If a registered or admin user clicks on the log out button, they will be logged out of their current session and will no longer be able to see the pages they would if they were logged in.
- A registered user will have to log in again if they want to see their Profile.
- An Admin user will have to log in again if they want to see their Profile or the Manage Products Page.


## **Future Features**
---
Features for future releases:

-  Affiliate scheme for hosts through a host_user login, offering discounts for their guests, and earning through their purchases.
-  Referral scheme where guests can earn credit on their account for reffering new customers.
- Location based products.
- Working with us, Suppliers, FAQ's, Terms and conditions
- Postcode delivery checker
- Update to the Blog to include images and document structure
- About page to reflect the quality of product
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

### Design
- [Adobe XD](https://adobexd.com/) used for wireframe and mockups
- [Illustrator](https://www.adobe.com/uk/products/illustrator) used to design the logo
- [Principle](https://principleformac.com/) used to create the loading gif

### Other Technologies
- [Squoosh](https://squoosh.app/) used for image formatting and resizing.

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
Product images and descriptions is from the following source:
- https://www.fortnumandmason.com/

### **Content**
Blogs are taken from 
- [Slate](https://helloslate.co.uk/now-more-than-ever-its-so-important-to-support-your-small-local-suppliers/)
- [lfm.org.uk](https://www.lfm.org.uk/farmers-blog/7-questions-parsons-nose/)

### **Media**
- Products photos from the following sources:
    - Home / About images from [Pexels](https://www.pexels.com//)

### **Code**
- Data structure and graphic diagram from http://www.graphviz.org
- Building A Blog Application With Django from https://djangocentral.com/building-a-blog-application-with-django/
- Adding Comments Model To The Administration Site from https://djangocentral.com/creating-comments-system-with-django/
- Send email functionality:
    - https://docs.djangoproject.com/en/3.2/topics/email/
    - https://docs.djangoproject.com/en/3.2/topics/forms/
    - https://www.youtube.com/watch?v=w4ilq6Zk-08&list=PLXcnmXd-db_hO1v3SLAzVcNieoS_Tcn-6&index=6

### **Acknowledgements**
- The Code Institute Slack community, has once again throughout this project, been a valuable resource.
- Stack Overflow is another constant source of helpful guidance and answers to so many questions.
- My mentor, Spencer Barriball, has been supportive and encouraging throughout this project.
- The Tutor Support on Code Institute has also been valuable resourse for this project.

#### Back to [top](#table-of-contents)
