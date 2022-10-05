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

## **Skeleton**
---
### **Wireframes**

Mobile
Desktop
Tablet

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

The website uses the [Google Fonts](https://fonts.google.com/) library to provide the fonts:

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

### Tools

### Design

### Other Technologies

## **Bugs and Testing**
Bugs & Testing information can be found in the seperate [bugs & testing](/TESTING.md) file.

## Deployment

The site is hosted on heroku.com.

Deployment of the site has been achieved by the steps following below, outlined in the Code Institue Walkthorugh Project:
## Credits

## Acknowledgements

#### Back to [top](#table-of-contents)
