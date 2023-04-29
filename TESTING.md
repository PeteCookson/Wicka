Back to [README](README.md)

## Index

* [Automated testing](#automated-testing)
  * [JavaScript](#javascript)
  * [CSS Validation](#css-validation)
  * [HTML Validation](#html-validation)
  * [Link Checker](#link-checker) 
  * [Lighthouse](#lighthouse)
  * [Responsinator](#responsinator)
  * [Am I Responsive](#am-i-responsive)
* [Manual testing](#manual-testing)

<br>
<hr>

## Automated Testing

### [JavaScript](https://jshint.com/)
- JSHint was used to test javascript code in this project. 
- All issues have been resolved. 
<br>

### [CSS Validation](https://jigsaw.w3.org/css-validator/)
- Validation of the CSS code of the project by address in direct input method.
- All issues were resolved.
<details>
<summary>CSS validation</summary>

![CSS Validation](/readme_assets/images/css-validation.png)
</details>
<br>

### [HTML Validation](https://validator.w3.org/)
- Validation of the HTML code of the project by address in direct input method.
- All issues were resolved except for 2 errors relating to Django crispy forms (see image below for more detail).
<details>
<summary>HTML validation</summary>

![HTML Validation](/readme_assets/images/html_validated.png)
</details>
<br>

### [Link Checker](https://validator.w3.org/checklink)
- Validation is used to check that all links are working and not broken. 
- The report has 3 issues relating to links in dummy phone number, email and facebook account used for reference only.
<details>
<summary>Link Checker</summary>

![Link Checker](/readme_assets/images/links_validated.png)
</details>
<br>

### [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- To test the accessibility and performance of the website. 
- After testing the site on Lighthouse, there were minor changes that needed to be made, for example the size of the image on the home page was found to be excessive and some aria labels were missing.
- After the above changes were made, the overall performance and accessibility have increased. 
- Additional future changes can be made in optimising images in next-generation formats.
<details>
<summary>Lighthouse</summary>

![Lighthouse](/readme_assets/images/lighthouse.png)
</details>
<br>

### [Responsinator](http://www.responsinator.com/)
- To test the responsiveness of the live website and functionalities on different size mobile devices.
- The allauth templates were styled to ensure they are responsive after testing.
- All pages are now responsive.
<br>

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
<details>
<summary>Am I Responsive</summary>

![Am I Responsive](/readme_assets/images/responsive.png)
</details>

<br>
<hr>

## Manual Testing
### Frontend
* The Register, Sign In and Logout system has no issues and is working accordingly. It shows the right 
  interactive messages to the user.
* The Profile Page is working properly, it updates the user information and uploads/updates the 
  users default delivery information. It shows the interactive message to the user once the update is complete.
* All the internal links are working and bring the user to the correct page on the website.
* All the external links are working and direct the user to the correct media page by 
  opening a new tab in the browser.
* The Hampers page shows the products and buttons without issues.
* The profile icon in the navbar shows a list of options depending on uder status.
* The blog comment form has no issues and it submits a new comment once the form is completed by 
  registered user. The comment is displayed once the submit button is pressed. 
* On the Blog page, logged in users can comment on blogs. Superuser has full CRUD functionality, such as creating, updating or deleting blogs.

### Backend/Admin Panel
* I have tested the Admin Panel and the all models are working without issues.  
* Full CRUD functionality has been tested in all models without errors. The models have the behavior expected for what they were built for.


### Further testing
- Usability tests were carried out using #peer-code-review through slack, friends and family to analyse the User Experience and to determine any issues. 

### Browser Compatibility
To ensure a wide range of accessibility on this site, I tested it with 3 browsers, on both desktop and mobile configuration. All functionality and responsiveness on different desktop browsers displayed correctly. The following browsers were used for testing:
- Chrome
- Firefox 
- Safari

### Device Testing
Chrome DevTools was used for testing different sized screens throughout the build of this project. using profiles for:
- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

The site has been tested throughout the build on these physical screens:
- iPhone SE
- iPhone XSmax
- Macbook Pro Retina 13'
- Imac 27"
- Philips 24" monitor

<br>
<hr>

## **Deployment**
- Ensured deployed page on Render loads up correctly.
- Ensured Debug variable is set to False.
- Confirmed that there is no difference between the deployed version and the development version.

<hr>

Back to [README](/README.md)