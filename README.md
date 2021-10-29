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

<img src="https://i.ibb.co/pn9shFW/Screenshot-2021-07-20-at-18-49-33.png">
<img src="https://i.ibb.co/CzQ66bK/Screenshot-2021-07-20-at-18-50-38.png">



# Features <a name="features"></a>




# Testing <a name="testing"></a>
<img src="https://i.ibb.co/0pNwW1c/Screenshot-2021-07-21-at-10-29-13.png">

For full testing section [click here](TESTING.md) 


# Deployment <a name="deployment"></a>

# Technologies Used <a name="technologies-used"></a>

# Credits <a name="credits"></a>


# Acknowledgements <a name="acknowledgements"></a>

* The Inspiration for this project came from a my love of records and my my favourite vinyl shop "Phonica Records"

* Thank you to the slack community for guiding me in the right direction.

* Thank you to my girlfriend for supporting me throughout my projects. 

* Thank you to the tutors at Code Institute.
 

