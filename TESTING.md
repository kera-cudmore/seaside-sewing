# Seaside Sewing - Testing

image of the site

[Visit Seaside Sewing Here](https://seaside-sewing.herokuapp.com/)

---

## Contents

* [Validation Testing](#validation-testing)
  * [HTML & CSS](#html--css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
  * [Wave](#wave)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [Bugs](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

Tsting was ongoing throughout the entire build. During development I made use of Googles Developer Tools to ensure everything was working as expected and to assist me with troubleshooting when things didn't work as they should.

I have gone through each page of the site using the Chrome Developer Tools to ensure each page is responsive on a variety of different screen sizes and devices, as well as manually testing this using a variety of devices in person.

---

## Validation Testing

### HTML & CSS

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

* checkout app
  * [stripe-elements.js](documentation/testing/validation/js/checkout-stripe-elements-validation.png)
* profiles app
  * [countryfield.js](documentation/testing/validation/js/profiles-countryfield-validation.png)

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

* seaside_sewing app
  * settings.py
  * [urls.py](documentation/testing/validation/python/seaside_sewing-urls-validation.png)
* bag app
  * [apps.py](documentation/testing/validation/python/bag-apps-validation.png)
  * [bag_tools.py](documentation/testing/validation/python/bag-bag_tools-validation.png)
  * [contexts.py](documentation/testing/validation/python/bag-contexts-validation.png)
  * [urls.py](documentation/testing/validation/python/bag-urls-validation.png)
  * [views.py](documentation/testing/validation/python/bag-views-validation.png)
* checkout app
  * [admin.py](documentation/testing/validation/python/checkout-admin-validation.png)
  * [apps.py](documentation/testing/validation/python/checkout-apps-validation.png)
  * [forms.py](documentation/testing/validation/python/checkout-forms-validation.png)
  * [models.py](documentation/testing/validation/python/checkout-models-validation.png)
  * [signals.py](documentation/testing/validation/python/checkout-signals-validation.png)
  * [urls.py](documentation/testing/validation/python/checkout-urls-validation.png)
  * [views.py](documentation/testing/validation/python/checkout-views-validation.png)
  * [webhook_handler.py](documentation/testing/validation/python/checkout-webhook_handler-validation.png)
  * [webhooks.py](documentation/testing/validation/python/checkout-webhooks-validation.png)
* home app
  * [apps.py](documentation/testing/validation/python/home-apps-validation.png)
  * [urls.py](documentation/testing/validation/python/home-urls-validation.png)
  * [views.py](documentation/testing/validation/python/home-views-validation.png)
* products app
  * [admin.py](documentation/testing/validation/python/products-admin-validation.png)
  * [apps.py](documentation/testing/validation/python/products-apps-validation.png)
  * [forms.py](documentation/testing/validation/python/products-forms-validation.png)
  * [models.py](documentation/testing/validation/python/products-models-validation.png)
  * [urls.py](documentation/testing/validation/python/products-urls-validation.png)
  * [views.py](documentation/testing/validation/python/products-views-validation.png)
  * [widgets.py](documentation/testing/validation/python/products-widgets-validation.png)
* profiles app
  * [apps.py](documentation/testing/validation/python/profiles-apps-validation.png)
  * [forms.py](documentation/testing/validation/python/profiles-forms-validation.png)
  * [models.py](documentation/testing/validation/python/profiles-models-validation.png)
  * [urls.py](documentation/testing/validation/python/profiles-urls-validation.png)
  * [views.py](documentation/testing/validation/python/profiles-views-validation.png)
* [custom_storages.py](documentation/testing/validation/python/custom_storages-validation.png)

### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

#### Mobile Results

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

## Automated Testing

Automated testing for this project was carried out with python unit testing?

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |
| 1 | Shopper | Easily navigate the site | Find products/information that I am require | A navbar is provided at the top of the page which allows users easy access to their account, shopping bag, search bar and the product categories.   | |
| 2 | Shopper | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products | When a user clicks on a category, they are then provided a dropdown with a breakdown of items within the chosen category. If a user choses the view all link, the page will display all items but the user will also be given the choice to refine the products shown via links to the sub-categories at the top of the page. | |
| 3 | Shopper | View more detail on products | to make an informed decision of if the item suits my requirements | When the user selects a product, they will be taken to the product detail page which lists more information about the item, such as the item name, price and description. A tag will display showing what category the product belongs to, along with a stock tag that displays the stock level for the product. If a rating and colour are avaiable for the product, these will also be displayed in the tags section. A user may hover over the image and they will be shown a magnified view of the item. If they wish to view a larger image, they may click on the image and a larger version of the image will open in a new browser tab.  | |
| 4 | Shopper | View items on clearance/sale easily | Save money  | There is a category choice for users called special offers which allows users to view deals or clearance items. | |
| 5 | Shopper | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) | When a user adds a product to their shopping bag, a toast will display to let the user know their addition to their bag was successful, along with showing them the items currently in their bag with their value and price. The toast also displays their total. If a user hasn't reached the threshold for the free delivery offer, they will be notified of this within the toast, which will let them know how much more they need to spend to take advantage of this offer. The shopping bag icon on the navbar will also display their total throughout their visit to the site. | |
| 6 | Shopper | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantites if required | Users are able to view all items selected for purchase from their bag. Their bag will list each item selected for purchase, along with the quantity, item price and subtotal for that item. At the bottom of their bag will be a section that lets them know the total for the items in their bag, the delivery charge (if applicable) and their grand total. | |
| 7 | Shopper | View ratings for products | make informed decisions about purchasing products | If a rating is avaialble for a product, this will be displayed in the tags section on the product details page. | |
| **REGISTRATION & USER ACCOUNTS** |
| 8 | Shopper | Register for an account | Have an account with the site and view my profile | Users can register for an account via the account icon in the navbar, which is available on all pages of the site. If a user doesn't have an account during checkout, they are given an option to create an account on the checkout page. | |
| 9 | Shopper | Receive an email to confirm my registration | Verify my account was created successfully |  | |
| 10 | Shopper | Log in and out | Keep my account information secure | Users are able to log in and out of their account through the account icon on the navbar which is accessible on all pages of the site. | |
| 11 | Shopper | View a profile page | Set a default delivery address and view previous purchases | Users are able to view their profile page once logged in via the account icon on the navbar which is accessible on all pages of the site. Their profile allows them to selet their default delivery information (which if filled out will prepopulate the checkout delivery information if the user is signed in). Users are also able to view their previous orders within their profile. These are listed most recent first and give the first part of the order number, the date and time of the order, items ordered with their quantities along with the order total. If the user clicks on the order number, they will then be taken to a more detailed breakdown of their order. | |
| 12 | Shopper | Reset my password | Recover my account | If a user has forgotten their password, they can click on the forgotten password button during login to reset their password. | |
| 13 | Shopper | Review products | Leave a rating/review on products | | |
| **SORTING & SEARCHING** |
| 14 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products | Users may view products bases on their price, rating or category from the navbar by selecting all products and then the option they want from the dropdown.  | |
| 15 | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name | Users are given chance to sort products on the products pages via a sort dropdown in the top right. This allows users to sort products by their name, price, rating and category - ascending or descending. | |
| 16 | Shopper | Sort multiple categories of products simutaneously | Find the best-priced or best-rated products across broad categories, such as fabric or habedashery | | |
| 17 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | Users are provided with a search bar in the navbar which allows them to search for items. The search not only checks the product name, but also their description for the search term used.  | |
| 18 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | Users are given feedback on their search term and the number of products which match the search term on the results page in the top left. | |
| **PURCHASING & CHECKOUT** |
| 19 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product quantity | Users are provided a quantity input box on the product detail page which allows them to increase or decrease the quantity required using the plus or minus buttons. The buttons are coloured to also provide visual understanding for the user of their purpose. Users may also type the value they wish to purchase directly into the quantity box. Once a user adds a product to their bag they receive a toast notification of the product they've added together with the quantity.  | |
| 20 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive | When the user views their bag, they will be presented with a list of all items selected for purchase, information shown will include an image of the item, the items name, the quantity of the item selected, the unit price of the item and the subtotal price for that item. At the bottom of the bag the user will be given the subtotal for all the items they are purchasing, the delivery fee (if applicable) and the grand total of their order. | |
| 21 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout | The users are given a quantity selector in the bag that looks the same as on the product detail page to provide continuity and familiarity for the user. Once the user has selected the new quantity of the item, they click the update link under the quantity input and the page will reload with the new quantities. If a user decides they would like to remove the item completely from their bag they can remove the item by clicking the remove link under the product. This removes the product and shows a toast which confirms that the user has successfully deleted the selected item from their bag.  | |
| 22 | Shopper | Easily eneter my payment information | Check out quickly and with no hassles | When a user is taken to the checkout page they can clearly see 3 sections of information that need to be completed to complete their order - their details, the delivery information and the payment information. Feedback is provided to the user whilst completing the checkout if any information they give is invalid. | |
| 23 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | Seaside Sewing provides its checkout facilities through Stripe | |
| 24 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | Users are taking to an order confirmation page once they have successfully checked out which provides them with their order information, such as their order details and the order date.  They are also shown their order details which lists the items they have purchased along with their quantity and the price of the item. A delivery section provides them with information on where they are having their order delivered to and finally they are shown the billing information section which provides them with their total, the delivery fee (if applicable) and the grand total for their order. | |
| 25 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records | Upon successful checkout, a user will be sent a confirmation email to the email address provided at checkout to confirm their order. | |
| **ADMIN & STORE MANAGEMENT** |
| 26 | Store Owner | Add a product | Add new items to my store | Admin are able to add new products to the store directly from the store website when logged in as a superuser. This option is provided to them under the account icon in the navbar - product management. If an admin clicks on this link, they will be taken to the add product page where they can add a new item to be added to the store. | |
| 27 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria | When a superuser is logged in, they are shown an edit button underneath each product on the products page, and are also shown an edit button when viewing a product. Once clicked they will be taken to a page similar in layout to the add product page (to provide continuity and familarity) and are able to edit the products information. | |
| 28 | Store Owner | Delete a product | Remove items that are no longer for sale | When a superuser is logged in, they are shown a delete button underneath each product on the products page, and are also shown a delete button when viewing a product. Once clicked they a modal will pop up asking them to confirm they wish to delete this product, and notifying them that this action cannot be undone. The superuser is given a choice to delete the product or cancel. The modal provides a layer of protection to product deletion and should prevent accidental deletion of products. | |

### Full Testing

Full testing was performed on the following devices:

* Mobile:
  * iPhone 13 Pro
  * iPhone 14
  * iPhone 11 Pro
* Tablet:
  * iPad Air 2
* Laptop:
  * Macbook Pro 2021 14 inch Screen
* Desktop
  * 34 inch ultrawide Monitor

Testing was also performed using the following browsers:

* Chrome
* FireFox
* Safari

Additional testing was carried out by friends and family on a variety of devices and screens.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| NAVBAR |
| | | | | |
| FOOTER |
| | | | | |

## Bugs

### Solved Bugs

| No | Bug | How I solved the issue | Evidence |
|:--- | :--- | :--- | :---: |
| 1 | The jQuery was not working for the toasts. | I researched this issue on slack and it seemed to be a known error with the toasts and bootstrap 5. As I am on a very tight deadline for this project and could not find a solution over an afternoon, despite bootstrap 5 being compatible for use with jQuery, I have decided to unfortunately bite the bullet and revert the bootstrap version used in the project down to 4.6.2. This has also meant that I have had to spend a bit of time updating some of the bootstrap classes used in the project (such as float-end to float-right) and has meant a large refactor of the categories and account navbars. | |
| 2 | Update link in bag not updating quantities | I spent a lot of time looking into this issue, only to come back the next day and realise that I had placed the update link after the delete link. This meant that the previous element was then the delete link and not the form as it should have been. I have moved the update link above the delete link and it now works correctly. | |
| 3 | Delete link in bag and update quantity to 0 were throwing a keyerror and internal server error 500 | I had added int: into the item_id part of the path in the bag urls file. This was preventing the functions working correctly | |
| 4 | Instance in the checkout view | When trying to checkout I received a valueError stating there was no HttpResponse object, and that it returned None. This was due to me not defining the instance. I needed to add line 40 to my checkout views, and also needed to add a return for if the instance failed (this step was missing from the BA tutorial) | [instance-error](documentation/bugs/instance-error.png) |
| 5 | Float error in checkout | I was getting the following error when checking out. This error was due to my delivery fee in the settings.py file being declared as a float, and the order total being a decimal. I could either cast the order total to a float or import decimal into settings and define the delivery fee as a decimal to prevent an error with the delivery fee. I decided to import decimal into the settings folder. | [Float Error](documentation/bugs/float-error.png) |
| 6 | Delivery Fee not displaying correctly in the admin | it was adding the total to the delivery fee - so just needed to remove the total and only reference the delivery fee |  |
| 7 | Webhooks returning 400 & 500 errors | There were 2 spelling errors and a wrong class name causing the issues, once these were corrected, the webhooks work as expected | [Webhook error](documentation/bugs/wh-error.png) |
| 8 | Success toasts were not displaying when adding items, but did display when logging in | I checked that the syntax was correct for the bootstrap version being used and knew that the toast was there as it was showing in the page code. Ed from tutoring saved the day when he spotted that I had omitted the `block.` from the front of my supertag in the bag.html. This meant that I was overwriting the toasts script with the scripts in the base.html file rather than adding to it. |
| 9 | Adding additional products already in the bag were not being added to the current quantity but overwriting it. The item_id was being passed to the view as an integer, but was then being converted to a string in the bag. | This one really puzzled me. I went back through the course content, searched on slack and did some googling but couldn't find a way to fix this. I therefore contacted tutor support and after trying a number of different possible solutions the only way we could find that worked was to cast the item_id as a string at the beginning of the add to bag view. This is obviously not a perfect solution, but works for the moment until I can dig into this further to find the cause. Update: We discovered that I was actually specifying the item_id as an integer in the path for the add to bag view, by removing this from the path, the add to bag function works as it should without having to cast the item_id to a string. This solution is much more elegant and so has been implemented. |
| 10 | Implementating enabling/disabling of the quantity buttons using the stock value in the shopping bag. I had managed to get this feature working within the product details page, however in the bag the plus button would disable once it reached the stock value, but if the value was lowered it would not enable. | This was an easy fix once someone pointed out to me that an item only had a quantity and product being passed to it. To solve the issue I needed to pass the stock value to the bag in the bags context. Once I did this the quantity buttons worked as I expected, the plus button would disable once it reached the stock value, and if the user reduced the quantity to under this amount, the plus button was enabled. | [![Image from Gyazo](https://i.gyazo.com/0004fc42c2cc75b0756fda3b154c1a5e.gif)](https://gyazo.com/0004fc42c2cc75b0756fda3b154c1a5e) |
| 11 | Product description was turning bold on addition of item to cart | Removed some unrequired strong tags from the success toast | [![Image from Gyazo](https://i.gyazo.com/df5b7fa8d2bbda30e78a6c3c4afde9cd.gif)](https://gyazo.com/df5b7fa8d2bbda30e78a6c3c4afde9cd) |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |
| | | |
