<h1 align="center"><img src="https://i.ibb.co/syF3MqP/logo3.png" alt="logo">

Full Stack Frameworks Milestone Project - Simply Records </h1>

Simply Records is an online e-commerce store, offering a collection of Vinyls, Merchandise and Equipment for Music Lovers. User's can create their own account, saving their details for faster checkout for future purchases, but are not limited, and can make a purchase as a guest if wanted. The registered user can edit their personal details and access their shopping history. Users can add products to the website if logged in snd verified also for users that would like more information a newsletter sign up is offered.


This site was developed using HTML, CSS, Bootstrap, JavaScript, jQuery, Python, Django, and it uses a SQL database through PostgreSQL.

 View Deployed site on Heroku here [Simply Records](https://simply-records.herokuapp.com/)

 **This website is for educational purposes only**

 # Table of Contents
 1. [UX](#ux)
    * [Strategy](#sratergy-plane)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton-plane)
    * [Surface](#surface-plane)
2. [Features](#features)
3. [Technologies](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

<h1 align="center">UX</h1> <a name="ux"></a>

# Strategy <a name="sratergy-plane"></a>

## Research
### What are the most important aspects of a Ecommerce website?
"I would like to navigate with a user-friendly interface and find a certain product"<br>

"I would like to find a product that has an attractive Image that draws me in" <br>

"I would like to be able to purchase items with an easy userfriendly interface"<br>


## opportunities and problems to be solved from user stories
 
|Opportunities | Importance | Viability / Feasibility
|-----|:------:|:-----:|
|**Purpose Of Webpage Explained** | 5 | 5 |
|**Intuitive Design** | 5 | 5 |
|**Clear Instructions** | 5 | 5 |
|**Easy Point Of Contact** | 5 | 3 |
|**Database Access**| 5 | 5 |
|**CRUD Functionality** | 5 | 5 |
|**Stripe Functionality** | 5 | 5 |

### Similar Record Shops

[Juno](https://www.juno.co.uk/) <br>

Juno Records is a UK-based online dance music retail store, selling vinyl records, CDs, music downloads and music accessories

[Phonica](https://www.phonicarecords.com/) <br>
Independent specialist in vinyl records, offering the latest releases, pre-orders and merchandise.

[Vinyl Tap](https://www.vinyltap.co.uk/) <br>
UK based online mail order record shop. We specialise in rare, deleted and promo items. We have an extensive stock of 7.
</div>


# Scope <a name="scope"></a>

# Business Approach


### Mission Statment
 Help users to find there desired products and purchase them. Allow the user to search for a paticular product by typing in the keyword of the product they want, Allow users to be be able to purchase products with out registering an account.
 


### Branding
* Branding defines you as your business
* Identify key values
* Consistency
* Clear focus that knows their target audience


### Content
* Simplify existing sites like Juno
* Clear from the outset
* User Connection
* Intuitive Content
* Interactive features 
 
### Aesthetics
* Deliberate use of colours to influence the user experience on a website.
* Make it easy for visitors to find what they are looking for. Multiple tools for accessing information
* keyword-rich content. Use headings and subheadings
* Consistent throughout so that a visitor navigating from page to page will always know where they are and how to get to the next item of interest.
* Elements to be visually connected and balanced

## User stories

| User Story ID | As A        | I want to be able to...                                      | So that I can..                                              |
| ------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|               |             |                                                              |                                                              |
| 01-01         | Customer    | View all of the products available from the store            | Select a product to purchase                                 |
| 01-02         | Customer    | View a list of products that are available for preorder | Take advantage of new product, a new product early  |
| 01-03         | Customer    | Select individual products to view                           | Read additional product details to confirm that this is the item I am looking for and add to my shopping cart |
| 01-04         | Customer    | Access my shopping cart at any time                          | Check added items and view the purchase total to ensure I am within my budget |
|               |             |                                                              |                                                              |
| 02-01         | Customer    | View the products available by music genres             | More easily find products by a specific genre   |
| 02-02         | Customer    | Sort by name/price/category/raiting                      | Easily identify the cheapest/most expensive product and most highly rated |
| 02-03         | Customer    | Be able to search for a product by name | Find a specific product that I am looking to purchase     |
| 02-04         | Customer    | Easily view the search results                               | Quickly determine whether the product I want is available    |
|               |             |                                                              |                                                              |
| 03-01         | Customer    | Easily select the quantity of products I would like to buy | Buy multiples of one product in the same purchase            |
| 03-02         | Customer    | View the items in the shopping cart that I have selected to purchase | Keep track of what I have added and the total cost           |
| 03-03         | Customer    | Adjust the quantity of the individual items in my shopping cart and remove them if I wish | Easily make changes to my purchase before checkout           |
| 03-04         | Customer    | Easily enter delivery and payment information                | Check out quickly and confidently with zero hassle           |
| 03-05         | Customer    | Feel that my payment is easy and secure| Confidently provide the needed information to make a purchase |
| 03-06         | Customer    | View an order after a purchase is made and checkout is complete | Verify that I have not made any mistakes in my order         |
| 03-07         | Customer    | Receive an email confirmation after checkout is complete     | Have a record of what has been purchased should there be any issues |
|               |             |                                                              |                                                              |
| 04-01        | Customer    | Sign up for the newsletter                                   | Be kept up to date with the latest news and offers |
| 04-02         | Customer    | Link to social media                        | Be kept up to date with the latest news and annoucements     | 
|               |             |                                                              |                                                              |
| 05-01         | Site User   | Easily register for an account                               | Have a personal account, a profile to view and streamline the checkout |
| 05-02         | Site User   | Receive an email confirmation after registering              | Be sure that my account is created and verify that it is myself that set it up |
| 05-03         | Site User   | Easily log in or log out                                     | Access my personal account and streamline the checkout       |
| 05-04         | Site User   | Easily recover my password in case I forget it               | Recover access to my account                                 |
| 05-05         | Site User   | Have a personalised account page                             | View order history, wishlist, and save, view and update contact and delivery information |
|               |             |                                                              |                                                              |
| 06-01         | Store Owner | Add a product                                                | Add new items to the store through streamlined interface     |
| 06-02         | Store Owner | Edit and Update a product details                            | Change product prices, descriptions, images, and other product criteria |
| 06-03         | Store Owner | Delete a product                                             | Remove items that are no longer available to buy             |
| 06-04         | Store Owner | Manage the attributes assigned to a product                  | Display and categorise products                              |
| 06-05         | Store Owner | Provide a secure shopping experience                         | Have customers confidently returning to the store                 |



# Structure <a name="structure"></a>

### The website uses Multiple pages with the content being Powered with Python, NoSQL, Javascript, HTML, CSS as the user navigates through the website.


### Header
The header of the page contains the NavBar and the Logo, It is a static element, and is fixed to the top of the page at all times.

### Navigation
On larger viewports, the navigational elements are separated into separate links within the NavBar. On medium viewports and lower, the navigational elements are collapsed into a SideNav, which can be activated with a toggler in the upper-left corner.

### logo
A logo is placed within the Header element in the centeron medium viewports and small.

### Pre Orders/ New Releases/ Back in Stock / Merchandise / Logout / Login / Register/ Cart
Users can access these pages regardless of where they are on the webpage.

### Footer
The footer is positioned at the bottom of the page. this is not a sticky element, and when the content exceeds the viewport of the device, the footer is pushed out of the viewport. The footer contains the name of the web page and social links to Github, Facebook, Youtube, Instagram and Soundcloud

### Products
A stylistic design of all results showing the products available for the user to read.

### Product Detail 
Details descriptive information of specific Product that is extracted from the database for users to read.

## Interactive
### Navbar
The navbar contains eight pages for an unregistered user and nine for registered users. Each page is highlighted when hovered over. When viewed in medium to smaller devices a burger icon is active and navigation opens from the side.

### Login/Register/Logout
If a user is not logged in, the NavBar/SideNav provides the relevant login/Register links. When a user is logged in, the Logout link replaces the login/Register links.

### Add Product
Registered users are shows the 'Add Film' tab when logged in, this is a detailed form that prompts the user to add specific details which are then sent to the database and render to the films tab if successful.

### Edit Film/Delete
Users that have added data to the database are highlighted with a choice to edit the data of that specific film and also have the option to delete

### Toasts
Interactive Toast will render to reflect each type of action. e.g When a user adds a product to their basket, the success toast is rendered



 
# Skeleton Plane <a name="skeleton-plane"></a>

### Wireframes
During the development process, changes have been made. All wireframes are the core skeleton to aid in the planning process and are not the final look of the design. I recommend that the PNGs are downloaded to be viewed in your browser.

[Homepage](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/Home.png)<br>
[Products](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/Products.png)<br>
[Product details](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/product%20details.png)<br>
[Register](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/Register.png)<br> 
[shopping bag](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/Shopping%20bag.png)<br>
[Sign in](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/Sign%20in%20.png)<br>
[Checkout](https://github.com/wilko90/Simply-Records/blob/main/static/wireframes/checkout.png)<br>

# Database
During the development of this Django project, I worked with the SQLite3 database, which is the default database used by Django. For deployment of this project, I changed to a PostgreSQL database, that is provided by Heroku.

Using Django Allauth and it's default `django.contrib.auth.models`, provided me with the the **User model** used in the profile app.

The structure of the Product and Checkout apps are guided by the Code Institute's walkthrough project, **Boutique Ado**.

### Data Models

#### Profile app

##### UserProfile model

| Name             | Database Key         | Field Type           | Validation                                          |
| ---------------- | -------------------- | -------------------- | --------------------------------------------------- |
| User             | user                 | OneToOneField 'User' | on_delete=models.CASCADE                            |
| Full Name        | default_full_name    | models.CharField     | max_length=50, default='', blank=True               |
| Phone Number     | default_phone_number | models.CharField     | max_length=20, default='', blank=True               |
| Street Address 1 | street_address1      | models.CharField     | max_length=80, default='', blank=True               |
| Street Address 2 | street_address2      | models.CharField     | max_length=80, default='', blank=True               |
| Town or City     | default_town_or_city | models.CharField     | max_length=40, default='', blank=True               |
| County           | default_county       | models.CharField     | max_length=80, default='', blank=True               |
| Postcode         | default_postcode     | models.CharField     | max_length=20, default='', blank=True               |
| Country          | default_country      | models.CharField     | blank_label='Select Country', null=True, blank=True |

#### Products app

##### Category model

| Name          | Database Key  | Field Type | Validation                             |
| ------------- | ------------- | ---------- | -------------------------------------- |
| Name          | name          | CharField  | max_length=254                         |
| Friendly Name | friendly_name | CharField  | max_length=254, default='', blank=True |

##### Product model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Category    | category     | models.ForeignKey   | 'Category', default='', blank=True, on_delete=models.SET_NULL |
| Sku         | sku          | models.CharField    | max_length=254, default='', blank=True                        |
| Label       | label_name         | models.CharField    | max_length=254                                                |
| Genre       | genre        | models.CharField    | max_length=24 default=False, null=True, blank=True                                             |
| Price       | price        | models.DecimalField | max_digits=6, decimal_places=2                                |
| Format       | fomat_size        | models.DecimalField | max_digits=2, decimal_places=0                              |
| Format Sizes       | has_formats    | models.BooleanField | default=False, null=True, blank=True                          |
| Description | description  | models.TextField    |                                                               |
| Rating      | rating       | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True         |
| Image       | image        | models.ImageField   | default='', blank=True                                        |
| Image URL   | image_url    | models.URLField     | max_length=1024, default='', blank=True                       |

#### Checkout app

##### Order model

| Name                     | Database Key    | Field Type           | Validation                                                                          |
| ------------------------ | --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| Order Number             | order_number    | models.CharField     | max_length=32, null=False, editable=False                                           |
| User Profile             | user_profile    | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True,related_name='orders' |
| Full Name                | full_name       | models.CharField     | max_length=50, null=False, blank=False                                              |
| Email                    | email           | models.EmailField    | max_length=254, null=False, blank=False                                             |
| Phone Number             | phone_number    | models.CharField     | max_length=20, null=False, blank=False                                              |
| Country                  | country         | CountryField         | blank_label='Select Country \*', null=False, blank=False                            |
| Postcode                 | postcode        | models.CharField     | max_length=20, default='', blank=True                                               |
| Town or City             | town_or_city    | models.CharField     | max_length=40, null=False, blank=False                                              |
| Street Address 1         | street_address1 | models.CharField     | max_length=80, null=False, blank=False                                              |
| Street Address 2         | street_address2 | models.CharField     | max_length=80, null=False, blank=False                                              |
| County                   | county          | models.CharField     | max_length=80, default='', blank=True                                               |
| Date                     | date            | models.DateTimeField | auto_now_add=True                                                                   |
| Promotion Cost           | promotion_cost  | models.DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                               |
| Order Total              | order_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Grand Total              | grand_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Original Basket          | original_basket | models.TextField     | null=False, blank=False, default=''                                                 |
| Stripe Payment Intent ID | stripe_pid      | models.CharField     | max_length=254, null=False, blank=False, default=''                                 |

##### Order Line Item model

| Name            | Database Key   | Field Type          | Validation                                                                         |
| --------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Order           | order          | models.ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | models.ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size    | product_size   | models.CharField    | max_length=2, default='', blank=True                                               |
| Quantity        | quantity       | models.IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            |




# Surface Plane <a name="surface-plane"></a>

## Brand Image

<img src="https://i.ibb.co/syF3MqP/logo3.png"><br>

The brand image/logo for "Simply Records" had to be simple, easy on the eye and be relevant to the webpage. It is located at the head of the page and when engaged navigates the user back to the home section.



## Colour Schemes
The project's design is to remain consistent throughout, the aim was to implement a subtle palette that is eye-catching for the user. This was designed with the main font [Roboto](https://fonts.google.com/specimen/Roboto) a smart and professional font.
<img src="https://i.ibb.co/z5dnqSb/Screenshot-2021-09-15-at-10-10-48.png">

All colour choices were assessed within the guidelines of [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG20/). Each colour was used with [Contrast Ratio](https://contrast-ratio.com/#%23212121-on-%23F0F3F4) and graded within the guidelines of [W3](https://www.w3.org/TR/WCAG20/).

## Text colours
#### Blackish (#2D2D2B)
predominantly all text is Black on a Whiote background which I have added to make content easy to read across all devices.

<img src="https://i.ibb.co/qpcYB1n/Screenshot-2021-10-29-at-16-55-35.png"> <img src="https://i.ibb.co/6J5xFdb/Screenshot-2021-10-29-at-16-59-34.png">

## Typography
### Body
[Roboto](https://fonts.google.com/specimen/Roboto) was my font of choice due to its clean simplistic properties which adds professionalism. 

### Logo
[Bungee](https://fonts.google.com/specimen/Bungee) was used as the logo font which has a fun and friendly feel 
## Images

### Imagery Used
All images are taken from a record shop called phoinica [Phonica](https://www.phonicarecords.com/) which what the project insporation came from. images are stored on a web imaging service as well as the media file.

### Image Placeholder

If a user does not add an image URL when adding a product to the database a placeholder will take that space. The image was sourced from [Adobe Stock](https://stock.adobe.com/uk/)
### Logo
The logo was made from a free editor called [Free Logo Design](https://editor.freelogodesign.org/)
### Favicon
Favicon was made from a free editor called [Icons8](https://icons8.com/icons/set/favicon)


## navbar
The navbar is the main method of navigating throughout the site and is a key role in aiding in strong UX. When hovered over the desired link a 'Supple' colour change is shown. 

<img src="https://i.ibb.co/9bn9sB8/Screenshot-2021-10-29-at-17-05-27.png">

### Call To Action Buttons
The point of contact needs to be appealing and interactive. for the main C2A points, I went into detail about styling which provides the user with a visual appearance. As C2A points are important in providing a good UX, I kept the consistent feel of freshness. When ideal the C2A are white text with a slate background, once initiated the colours change opposite. 

<img src="https://i.ibb.co/y5sVSRR/Screenshot-2021-10-29-at-17-07-03.png">
<img src="https://i.ibb.co/jTV1qrV/Screenshot-2021-10-29-at-17-10-56.png">



# Features <a name="features"></a>

## Existing Features
### Home Page and Featured Products 
The home page contains a button that redirects a user to the "All Products" page. It also displays an active carousel that features products from the database. The home page also displays a sample of six products from three diferent categories.

<img src="https://i.ibb.co/ww1Zr0m/Screenshot-2021-10-29-at-17-19-37.png">
<img src="https://i.ibb.co/BjxnYTW/Screenshot-2021-10-29-at-17-20-51.png">

### All Products Page

The Products page displays cards sorted from the oldest to the most recently added.
The user can filter these products by price,raiting,name or category. All product cards are clickable and redirect a user to the individual product page with detailed information. and a place to add to there cart.

<img src="https://i.ibb.co/pPNKgRY/Screenshot-2021-10-29-at-17-25-46.png">

### Product Detail

Individual products are viewed on this page, with the image to the left, and details to the right. The details are presented the same as the products card on the products pages, along with the products description. A quantity selector box is given on this page for the user to input manually or use selector buttons (+/-) to increase/decrease the quantity of the respective product. There are two buttons below this for the user to go back to the all products page to 'Continue Shopping', or 'Add to Basket' to add the product to the user's basket.The edit/delete buttons are presented here also to only a superuser. If any products on the enitre site contain a format, then a dropdown above the format selector box is presented for the user to select a format e.g '12'.

<img src="https://i.ibb.co/5Bsph7M/Screenshot-2021-10-29-at-17-30-43.png">

### Register
The register page allows a user to create a new account. The user is asked to fill the fields "username", "password" "confirm password" and "email address". When adding a username, the code compares it against existing usernames to ensure that it is unique. The "confirm password" field must match the original password. All passwords are hashed for security purposes. If the user's input does not meet requirements, toast messages will inform a user about the error. When the form is submitted successfully, a user is asked to confirm there email address by clicking a link that will get sent to there inbox. then the user will be allowed full user functionality.

<img src="https://i.ibb.co/Z2Q2trX/Screenshot-2021-10-29-at-17-37-07.png">

### Shopping Bag
This page lists to the user everything they have added to their basket. Basic product information is shown, along with a quantity selector box for the user to ammend their order. There is an update button to update the given quantity, and a remove button to completely remove the product fromt their basket. The basket total is given at the bottom right of the page  and then the grand total. If the user has not hit the delivery thresh hold, text is shown informing how much more the user needs to spend to get the discount. If that threshold is hit, then the logic is executed to deduct the discount from the basket total, ammending the grand total to match. There are two buttons below this, one to 'Continue Shopping' taking the user back to all products, and the other the procedd to the checkout page.

<img src="https://i.ibb.co/7nWDNxH/Screenshot-2021-10-29-at-17-44-29.png">

### Checkout
The checkout page is split into two columns.To the right is a brief order summary, giving the user a final opportunity to check thier basket. On the left, a form to enter personal and delivery information. If the user is a new user, then the form will be empty. If the user has palced an order previously, or entered their information on the profile page, then the form will be pre filled with what was entered last time. Below the form, a checkbox offers the user to save the input information to their profile, and if not logged in then links to create an account or login are presented. An input box is then found to input the users payment method. Finally, there are again two buttons, one to go back to adjust user's basket, and one to complete their order. Upon clicking 'Complete Order', a black overlay takes the screen with a spinning gif indicating the order is being placed.

### Checkout Success:

This page is accessed once a user completes an order. but can also be accessed through the profile page by clicking on the order number from their 'Order History'. Here, the user will have a summary of their order, a confiramtion message of the successfully placement of the order, and a button to check out the lastest deals, to encourage further shopping. If accessing this page through their order history, a user will be notifued that they are viewing a past confirmation.

<img src="https://i.ibb.co/wB980Sd/Screenshot-2021-10-29-at-17-57-20.png">

### Profile Page

This page is accessed through the 'My Account' link from the navbar.  when clicked the user is hsown  a form that has there default delivery information, which will be empty for the first time, and then updated whenever an order is placed and details are entered into the checkout form. The user can also update their details here by filling in the ofrm and clicking the 'Update Information' button below the form. The second dropdown holds the users order history. This is presented as a simple table, showing the order number, date, items and order total. The order number is given as the forst 5 digits of the unoquie number, and can be hovered over to reveal the entire number, and clicked to take the user to that orders confirmation page.

<img src="https://i.ibb.co/QJbNLT4/Screenshot-2021-10-29-at-18-00-21.png">

### Toasts:

All pages have the ability to display toast messages to the user, which are displayed below the navbar on the right hand side. There are four different types of toast messages: success, error, warning and info. The toast colours will change to reflect each type of message. When a user adds a product to their basket, the success toast is rendered, displaying the contents of their basket, and the total excluding the discount. At the bottom of the toast a button is given for the user to go to secure checkout and open their basket page to review their order.

<img src="https://i.ibb.co/0FgV6gf/Screenshot-2021-10-29-at-18-05-02.png">

### News Letter

A section found as part of the footer for a user to enter their email address and subscribe to a newsletter. Notification is shown if user has already subscribed.

<img src="https://i.ibb.co/gr0NvjM/Screenshot-2021-10-29-at-18-12-48.png">

## Features To Implement

* Custom Reviews
* Music Player for sample of tracks
* Log in via social media account

# Technologies Used <a name="technologies-used"></a>

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) - Language used to create the structure of the pages.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Language used to add styling across all pages.

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Language used to create interactivity across the pages.

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>) - Language used to create the back-end functionality of the app.

### Libraries, Frameworks and Editors

- [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

- [Bootstrap](https://getbootstrap.com/) - used as the base structure and layout of the site, using its grid system to aid responsiveness across screen sizes.

- [jQuery](https://jquery.com/) - utilising it's extensive library to simplify and help writing Javascript code.

- [Google Fonts](https://fonts.google.com/) - used to embed the 'Montserrat' and 'Quiksand' fonts used across the site.

- [Font Awesome](https://fontawesome.com/) - used for their free range of icons.


- [Gitpod](https://www.gitpod.io/) - used as preferred choice of IDE for writing my code. Halfway through this project gitpod upgraded their IDE to [Visual Studio Code](https://code.visualstudio.com/) which I then continued using as the main IDE to write my code.

- [Git](https://git-scm.com/) - used for version control by making use of the Gitpod terminal to add, commit and push to Github.

- [Github](https://github.com) - used to host the project's repository and store the code, and linked to Heroku to push latest changes to the deployed build version.

- [Heroku](https://www.heroku.com/) - used as a hosting platform for deploying my live version of this CRUD application.

### Packages

- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - used as an authentification system, utilising it's templates and logics.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to format forms, automatically using Bootstrap styling.

- [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library to help store imagery into a database.

- [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for the Python.

### Databases

- [Sqlite 3](https://www.sqlite.org/index.html) - used as the database during development.

- [PostgresSQL](https://www.postgresql.org/) - used as the database for deployment, enabling it as an add on through [Heroku](https://www.heroku.com/postgres).

### Tools

- [Stripe](https://stripe.com/gb) - used as the payment infrastructure to take payments on the site.

- [Google](https://www.google.co.uk/) - used for researching various techniques, styles and information.

- [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging.

- [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQjwt-6LBhDlARIsAIPRQcIBcIOv97xfPkc4bspdS1_RmjQXlcnJFJtcsCsHDUTLxu53aTTdp-0aAkbfEALw_wcB) - used for creating the wireframes in the design stage.

- [Coolors](https://coolors.co/) - used to find and compare colours.

### Validators
- [Am I Responsive](http://ami.responsivedesign.is/) - used for showing the responsiveness of the site across different screen sizes and providing the image at the top of this document.
* My projects colour ratio was tested with [webaim](https://webaim.org/resources/contrastchecker/).
* My projects logo and typography was graded with [W3](https://www.w3.org/TR/WCAG/#contrast-minimum) guidelines.
* The project’s HTML was validated using [W3C](https://validator.w3.org/) HTML Markup Validator.
* The project’s CSS was validated using W3C [Jigsaw](https://jigsaw.w3.org/css-validator/) CSS Validator.
* The project’s JS was validated using [JSHint](https://jshint.com/).

# Testing <a name="testing"></a>
<img src="https://i.ibb.co/ZYwgkLB/Screenshot-2021-10-29-at-18-35-19.png">

For full testing section [click here](TESTING.md) 


# Deployment <a name="deployment"></a>

## **Deployment**

### Local Deployment

To run your own version of this project, it can be cloned or downloaded from Github. Once you have decided on which IDE you want to use, make sure that you have the following installed:

- Git - for version control
- PIP - to install packages
- Python - the programming language used for the backend logic

Github offers a few ways to clone a repository. You can simply download the entire repo as a zip file, and then upload that zip into a new workspace. Otherwise, on the repositories page in Github, follow these steps:

1. Click the 'Code' button.

2. In its dropdown menu, click the clipboard icon to copy the URL.

3. In the terminal window back in your IDE, make sure the current working directory is the location where you wan to clone the repository.

4. In the command line, paste in the URL retrieved from the repo using the command:

```bash
git clone <copied-repository-url-from-Step-2-^^>
```

5. Create your environment variables. You can either go to the Gitpod dashboard, go to Settings => Variables => and then add them there, or create a env.py file, and add the env.py file to your .gitignore file in your projects rot directory. Either way works the great and the same way, just make sure these variables are included:

```bash
DEVELOPMENT = True
SECRET_KEY = YOUR_SECRET_KEY
STRIPE_PUBLIC_KEY = YOUR_STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = YOUR_STRIPE_SECRET_KEY
STRIPE_WH_SECRET = YOUR_STRIPE_WH_SECRET
```

You will need to sign up to stripe. Upon doing so, you can get the PUBLIC and SECRET keys from the left column of the page, clicking "Developers", and API Keys. Once you have set up the webhook endpoints, you will be given a unique STRIPE_WH_SECRET key.

More information on this can be found [here](https://stripe.com/docs).

6. Install the required dependencies needed to run the app by typing in the command line:

```bash
pip3 install -r requirements.txt
```

7. This project will now be set up and ready to run. In the command line, type:

```bash
python3 manage.py runserver
```

You can create a super user to access the admin backend.

```bash
python3 manage.py creatsuperuser
```

To access the admin backend add to the end of the sites url:

```bash
https://<simply-records-url>/admin
```

This will allow to do add, edit and delete products, categories, users, orders, as well as verify any email addresses.

8. Your models will need to be migrated in order to create them in the database. In the command line, type:

```bash
python3 manage.py makemigrations

***FOLLOWED BY***

python3 manage.py migrate
```

Whenever a model is edited they will need to be migrated. To make sure you are migrating the correct models, you can run a dry run flag on makemigrations to make sure you know which models are to be migrated, and a plan flag on migrate before actually using 'makemigrations' and 'migrate',

```bash
python3 manage.py makemigrations --dry-run

python3 manage.py migrate --plan
```

### Deployment to Heroku

Deploying this site to Heroku.

1. If you haven't got one already, create an account for Heroku. From signing in on their website, click 'New', found at the top right of the dashboard, and then 'Create new app'.

2. Give the app a unique name, and set the region to whatever region is closet to your own location, then click 'Create app'.

3. Once created, click on the 'Resources' tab, and in the add ons search bar, type postgres, and click 'Heroku Postgres', and then use the free plan, and confirm. This will provision a new Postgres database.

4. There are some extra dependencies and files needed. You will also need to install:

- psycopg2-binary - a PostgreSQL database adapter for the Python programming language.
- dj_database_url - a Django utility which allows you to utilise the 12factor inspired DATABASE_URL environment variable to configure your Django application.

You will also need to install - gunicorn - a Python Web Server Gateway Interface(WSGI) HTTP server., which will act as our web server.

5. After installing these dependencies, run the command:

```bash
pip3 freeze > requirements.txt
```

This will ensure that Heroku installs all our apps requirements when we deploy.

6. To save having to manually re-create your database (Postgres is the database used for deployment, and files aren't automatically transferred), you can easily transfer from the development database.

- Make sure you are connected to your mysql database.

- Backup your current database and load it into a db.json file by typing in the command line:

```bash
python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

7. Now to set up the new database. Head to your projects 'settings.py', and import dj_database_url at the top.

8. Scroll down to database's setting, and comment out the default configuration, replacing it with a call to dj_database_url.parse and give it the database URL from Heroku:

```bash
DATABASES = {
        'default': dj_database_url.parse("<YOUR_Postrgres_database_URL>")
    }
```

This can be found from the settings tab on Heroku, clicking 'Reveal config vars' and copying the value there from the DATABASE_URL key. It will start with 'postgres://'.
You can also get this from typing in the command line:

```bash
heroku config
```

Note: This is a temporary set up, and you should NOT add, commit and push to Github with this URL in your settings file. You DO NOT want this Heroku database config URL in version control for security reasons.

This is now connecting your manage.py file to your new Postgres database. As this is now a new database, you will need to run migrations again to get the database all set up.

9. After this, you can load your product data from the db.json file into Postgres using:

```bash
python3 manage.py loaddata db.json
```

10. Next you want to create a superuser to use on the Postgres database:

```bash
python3 manage.py createsuperuser
```

Follow the prompts it suggests, and your super user will be created.

11. In 'settings.py', you want to create an if statement so when the Heroku app is running, you connect to the Postgres database, otherwise, you connect to the development database. Replace the database setting with this code:

```bash
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

12. Create a Procfile, to tell Heroku how to run this project. Inside this file, add:

```bash
web: gunicorn simply_records.wsgi:application
```

13. Login to Heroku on the command line, using:

```bash
heroku login -i
```

14. Disable collect static so Heroku won't try to collect static files when we deploy. Type in the command line:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1
```

15. Add the hostname of your Heroku app to allowed hosts in 'settings.py'.

Heroku can be connected to Github to automatically deploy each time you issue a git push in the command line. The easiest way to enable this is:

1. Open Heroku and navigate to the 'Deploy' tab.

2. Under 'Deployment Method' select 'Connect to Github'.

3. Search for your repositories name and click connect.

4. Then scroll down and click 'Enable Automatic Deploys'.

Your code will now be automatically deployed with every git push from you IDE command line. Upon a git push, you will see the build in progress in the 'Activity' tab on Heroku. You are now deployed to Heroku.

### Hosting Images on Amazon Web Service S3

For this site, the static and media files are hosted in an AWS S3 bucket. You will need to create an account with AWS, and create an S3 bucket, giving it public access. Once this is complete, upload your static and media files into the correct folders. The CORS configuration I used was what Code Institute provided, which is:

```bash
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

This is the basic setup of the S3 bucket with AWS, more details can be found [here](https://docs.aws.amazon.com/s3/index.html).

You will the need to set the static and media files in your workspace. For this, you will need to do the following:

1. First, do a pip install of 'boto3' and 'django-storages', and then freeze them into the requirements.txt file so they get installed upon the next push to Heroku.

2. In 'settings.py', add 'storages' under INSTALLED APPS. Then add these following settings to tell Django which bucket it should be communicating with:

```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'simply-records'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and Media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

When you set up your S3 bucket, you would have downloaded a csv file. In this file you will find your AWS access key and secret access key.

NOTE: It is very important to keep these keys private. If they end up in version control then someone can use them to move and store data through your S3 bucket, where Amazon would bill YOUR registered credit card if it exceeded the limit.

3. Add these keys to your Heroku config variables.

4. Add a variable here with the key of 'USE_AWS' with a value of 'True'. This ensures your settings file knows to use the AWS configuration when deploying to Heroku.

5. Delete the DISABLE_COLLECTIC static variable from Heroku so Django can collect static files automatically uploading them to the S3 bucket.

6. Create a file called 'custom_storages.py'. This will contain the following:

```bash
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

This file will link with the settings from above ^^ and tells Django that during production, use the S3 bucket to store the static files whenever collectstatic is run, and any uploaded product images.

7. Add and commit all of these changes, then issue a git push command. This will trigger an automatic deployment to Heroku, and then all of this logic will be implemented, and your static and media files will be applied to your deployed site.


# Credits <a name="credits"></a>

## Written Content
* I started by adding content myself under my username, all detailed information and content taken from [Phonica](https://www.phonicarecords.com/) which the website was based upon.
* All other content will be added by the users
* All other content is written by me 


 
## Images
* Content images come from the users and can be sourced from multiple places. For the boilerplate content I created a user and added content myself, Images came from [Phonica](https://www.phonicarecords.com/)
* Image PlaceholderImage was sourced from [Adobe Stock](https://stock.adobe.com/uk/)
* logo was made from a free editor called [Free Logo Design](https://editor.freelogodesign.org/)
* Favicon was made from a free editor called [Icons8](https://icons8.com/icons/set/favicon)
* Product images are added via an image hosting service or added directly by the user .


# Acknowledgements <a name="acknowledgements"></a>

* The Inspiration for this project came from a my love of records and my my favourite vinyl shop "Phonica Records"

* Thank you to the slack community for guiding me in the right direction.

* Thank you to my girlfriend for supporting me throughout my projects. 

* Thank you to the tutors at Code Institute.
 

