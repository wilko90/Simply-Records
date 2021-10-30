<h1 align="center">Full Stack Frameworks Milestone Project - Simply Records</h1>

For full readme [click here](README.md)

# Table of Contents

1. [User Story Testing](#user-story)
2. [Features Testing ](#manual-testing)
3. [Further Testing](#further-testing)
4. [Browser Testing](#browser-testing)
5. [Validation Testing](#validation-testing)
6. [Bugs](#bugs)



# User Story Testing <a name="user-story"></a>

All user stories are tested in full and all came out successful. the users stories below are picked from each user story section, as a customer, user and site owner.  

# As a customer i want to tbe able to View all of the products available from the store
### Benchmark - To be able to view all products 
* On intial contact the user is displayed with a C2A marked "shop now" once user clicks they are taken to the all products page
#### Outcome - Successful 

<img src="https://i.ibb.co/6J5xFdb/Screenshot-2021-10-29-at-16-59-34.png">

# As a customer i want to be able to Select individual products to view
### Benchmark - To be able to see a detailed view of a product
* When a user initiates a product by selecting the title of image, they are then taken to the detailed view of that product 

### Outcome Successful 

<img src="https://i.ibb.co/KKpG29N/Screenshot-2021-10-29-at-20-50-54.png">

# as a site user I want to be able to Have a personalised account page
### Benchmark - To be able to see previous orders and contain my delivery information so I dont need to re add eveery time I make a purchase 
* When a user navigates to the "My account button at the head of the page. when selected the user is displayed with there delivery information and previous orders. the user can also update this if needed. 

### Outcome Successful 

<img src="https://i.ibb.co/WnGXMd5/Screenshot-2021-10-29-at-21-02-30.png">

# As a store owner I want to  Provide a secure shopping experience
### Benchmark - To be able to see previous orders and contain my delivery information so I dont need to re add eveery time I make a purchase 
* The websites payment function is powered by "stripe" this is one of the biggestes payment methods and is used by all mayjor brands. The user will have to input there 16 digit card number, expiry and security code. the user is all so clear of the total amount been charged to the card.  

### Outcome Successful 

<img src="https://i.ibb.co/QHChKVG/Screenshot-2021-10-29-at-21-08-42.png">

# As a store owner I want to be able to add products with ease.
### Benchmark - To be able to navigate with ease and add a product 
* At the head of the page there is a plus icon that displays add product. when selected the user is presented with a form where they can add products.   

### Outcome Successful 

<img src="https://i.ibb.co/rHV5cr0/Screenshot-2021-10-29-at-21-16-52.png">

<img src="https://i.ibb.co/16GGVTQ/Screenshot-2021-10-29-at-21-17-07.png">

# As a user I want to be able to sign up to a newsletter  
* At the foot of the page there is a banner that says sign up to newsletter in bold, there the user is prompted to enter there email address then is shown a successful message when completed.    

### Outcome Successful 

<img src="https://i.ibb.co/dgFNhks/Screenshot-2021-10-29-at-21-24-33.png">
<img src="https://i.ibb.co/jh6V5zb/Screenshot-2021-10-29-at-21-25-30.png">





# Features Testing <a name="manual-testing"></a>

Features below are manual testing and described below

## Registration
* Ensure that when a user is not logged in, they can access the Register link within the NavBar/SideNav from any location on the site.
* Ensure that when a user interacts with the Register link in the NavBar/SideNav, the registration page appears
* Ensure that the form presented shows the fields username, password, confirm password, email address
* Ensure that the following validation occurs
  * Username
     * Alert box pops up when fields are not entered correctly and hints to correct validation
     * Ensure form can not be submitted if the username does not contain letters numbers and one case sensitive.
  * Email address 
    * Ensure the email is valid and contains the correct format
    * Ensure that email has not already been used twice
    * Ensure that email is confirmed by the user via email  
  * Password
      * Requirements: Required/Between 8 characters, with upper and lowercase letters
      * If a user does not provide a password, a required message will prompt the user
      * If the field is in an invalid state, and the user provides a valid password, they attempt to submit the form, the field reverts to its valid state.
  * Password Confirmation
    * Required/Must match Password
    * if a user provides a valid confirmation password that matches, flash message registration is successful
    * If a user does not provide a confirmation password, a required message prompts the user to provide a confirmation password
    * If the users' password does no match, a user is prompted with a "passwords do not match" flash message
* Ensure that when a user successfully registers, they are sent an email to activate there account. 
* If a user has attempted to register an account with a username that already exists in the database, registration is unsuccessful, and the user is informed via a flash message that the username already exists.
* If a user already has an account and needs to go to the login screen the link takes them there successfully
## Login
* Ensure that when a user is not logged in, they can access the login link within the NavBar/SideNav from any location on the site.
*  Ensure that when a user interacts with the login link in the NavBar/SideNav, the login page appears
* Ensure that the following validation occurs appropriately
   * Username
      * Alert box pops up when fields are empty
      * If users enter incorrect details they are shown an Unsuccessful flash message
      * If a user still has not created an account, the button is active and sends a user to a registration page 
      * If a user matches the database with the correct username and password, a flash message is shown welcoming them with their name and is sent to the home page.
* ## User Logout
* Ensure that when a user is logged in, they can access the LogOut link within the NavBar/SideNav from any location on the site.
* Ensure that when a user selects the Log Out link, they are logged out of the website.
* Ensure when a user logs out they are prompted with a message and returned to the the home screen 

## Nav Bar
* On initial load ensure the navigation bar loads the full width of the screen with correct links and logo.
* Ensure all links are active and not broken and send a user to the correct location
* Ensure the navbar is sticky and is constantly at the head of a page
* Ensure the logo is active and redirects the user to the home page
* Ensure the shipping banner is present and shows correct price for free delivery

## Home Page
* Ensure all Images render correctly.
* Ensure the C2A button is working correctly and directs the user to the all products page
* Ensure carousel is active and displays product cards.
    * Ensure each product card is interactive and when initiated sends the user to the films information.
* Ensure footer is at the base of the page at all times.
* Ensure search bar is active and function is working correctly .
* Ensure relevant product categories are showing only 6 products.
* Ensure all social links are active, open in a new tab when initiated and send a user to the correct location .

## Products
* On initial load Product cards render with amlunt of products at the right and filter options on the left.
* Ensure the filter bar is working and filters to correct statment.
    * Ensure if no search results are found the user is prompted with this
* Product cards
  * Ensure each Product card is active.
  *  Ensure all Product cards show the title, price and cateogory link.
  * Ensure when initiated it sends the user to the correct product.
  * Ensure all category links are wokring and user is sent to correct category 
  * Ensure six products are rendered on each line and are all in uniform

## Product Detail
* Ensure user is greeted with an image, title,price,raiting,description, QTY fields, edit/delete if created user, keep shopping button and add to bag.
* ensure all link are working
* Ensure qty field cant go below zero
* Ensure back button send user back one step
* Ensure when product is added to bag that the user is noted and the bag is updated
* Ensure the correct qty is shown in bag

## Add Product
* Ensure all fields are shown
* Ensure the form can only be validated when passed certain criteria 
* Ensure if image is not added that placeholder is showed instead 
* Ensure data renders corectly

## Edit Product
* Enusre all fields are shown from previous input
* Ensure data is edited successfully 
* Ensure image placeholder is present
* Ensure image can be deleted

## Delete 
* Ensure user can delete product and the item be removed from DB
* User is promted with are you sure you want to delete message

## Bag
* Ensure when there are no items in the cart the user is pompted with a keep shopping C2A
* Ensure when user adds product to bag they are prompted with a toast that displays there order and discount information 
* Ensure the bag shows the correct price at the head of the nav bar and the user can be sent to the bag items when selected
* Ensure teh relevnt information is shown in the bag with grand total and information on how to qualify for the discount
* Ensure the keep shopping and the secure payment buttons are working
* Ensure the user can update ther cart with the input field and the price adjust accordingly 
* Ensure the user can remove items

## Checkout
* Ensure page renders correctly 
* Ensure 10 input fields are shown and a detailed view of order on right 
* Ensure inout fields are:
    * Name
    * Email
    * phone
    * Street
    * street 2
    * Town
    * County
    * Postcode
    * Country
    * Payment field
* Ensure correct total is displayed 
* Ensure user can edit bag
* Ensure user can complete order 

## Success Page
* Ensure Page renders and is titled "Thank You"
* Ensure all details are correct and email confirmation is sent
* Ensure user can continue shopping if the wanted 

## News Letter

* Ensure news letter is rendered at bottom of home page
* Ensure text is clear and centered
* Ensure only an email can be validated 
* Ensure an email can not be entered twice
* Ensure is prompted each of the steps in the toast section 

## Toasts

* Ensure toast renders below bag
* Ensure all items added to the bag are displayed in toast 
* Ensure user can navigate to bag through toast
* Ensure user is prompted with a warning to spend more and apply for discount
* Ensure user can clearly see the bag total
* Ensure error toast is shown when error happens
* Ensure info toast is shown when information is displayed 
* Ensure warning toast is shown for warning 

# Further Testing <a name="further-testing"></a>

## Responsive Design

All testing above was again tested on multiple devices through chrome developer tools with their `toggle device tool bar`

Devices used for testing:
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2XL
* iPhone 5/SE
* iPhone 6/7/8 (plus)
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold

# Browser Testing <a name="browser-testing"></a>

All browser testing was done with the same method above

 Problems usually occurred when my CSS was not compatible with most browsers. Running my CSS code through an Auto-Prefixer solved these compatibility issues.

## Chrome/Mircrosoft Edge

* All testing successful

## Mozilla Firefox

* All testing successful

## Safari

* All testing successful

## Internet Explorer

* My project uses ES6 which has compatibility issues with Internet Explorer. No further testing was made.


# Validation Testing <a name="validation-testing"></a>

Validation testing was done with third party applications below:

## [W3 Vailidator](https://validator.w3.org/)

* HTML successfully passes W3 Validator

## [Jigsaw Validator ](https://jigsaw.w3.org/css-validator/)
* CSS successfully passes the W3 Jigsaw Validator
<img src="https://i.ibb.co/cCw8VpC/Screenshot-2021-07-21-at-14-49-59.png">
## [JSHint](https://jshint.com/)

* JS Hint was used to flag any errors or mistakes in the javascript code and was used consistently throughout the development process.
* No errors are present 
* Two warnings present are due to " 'let' is available in ES6 (use 'version: 6') or Mozilla JS extensions"
<img src="https://i.ibb.co/gzXcBVL/Screenshot-2021-10-30-at-18-42-35.png">


## [Python](http://pep8online.com/)

All code was formated with "black" a python code formatter 
* The project's Python was validated for PEP8 compliance using Pep8,
* These warnings have been considered, however, they appear to be incorrectly reporting `env.py` as being unused, due to how `env.py` works. Once deployed, this will not be imported anyway, and therefore this has been added to the ignore file.

There are some extra errors due to line of code been to long, ive decided to leave these here as when chnaged I started to find mulitple issues with functions through out the site.

# [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)

#### The project's Accessibility, Performance, and Best Practices audit were undertaken with Google Lighthouse. Webpages graded are below:

<img src="https://i.ibb.co/tDSfBkc/Screenshot-2021-10-30-at-20-15-24.png">

# Bugs and Problems <a name="bugs"></a>

### Deployment
* I had great difficulty deploying my databse to postgres. the issue was due to adding all the data to the admin page and not directly to the json file. Issue was resolved by dumping the data to a products.json file when connected to Sqlite 3, then connecting to the Postgres database and loading the data there.

Solution: Resolved

### Rendering the search function for mobile screens 
* I was unable to render the search function on mobile screens without causing layout issues. By adding a javascript to block the search bar in small screens then shows when initiated.

Solution: Reolved

### QTY plus and minus buttons reduced size

* I had issues with posistion on smaller screens which when fixed resulted on the + - buttons reducing size, unable to target them them i re posisitoned them to be more central for a quick fix. 

Solution: Unresolved

For full readme [click here](README.md)