# Seaside Sewing - Testing

image of the site

[Visit Seaside Sewing Here](https://seaside-sewing.herokuapp.com/)

---

## Contents

* [Validation Testing](#validation-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
  * [Wave](#wave)
* [Automated Testing](#automated-testing)
  * [Coverage](#coverage-testing)
* [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [Bugs](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

Testing was ongoing throughout the entire build. During development I made use of Googles Developer Tools to ensure everything was working as expected and to assist me with troubleshooting when things didn't work as they should.

I have gone through each page of the site using the Chrome Developer Tools to ensure each page is responsive on a variety of different screen sizes and devices, as well as manually testing this using a variety of devices in person.

---

## Validation Testing

### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass| [Home Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2F) |
| Privacy Page | Pass | [Privacy Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fprivacy) |
| Terms & Conditions Page | Pass | [Terms & Conditions Page Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fterms) |
| Delivery Policy Page | Pass | [Delivery Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fdelivery) |
| Contact Form Page | Pass | [Contact Form Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fcontact%2F)|
| Contact Form Success Page| Pass | [Contact Success Page Validation](documentation/testing/validation/html/contact-success-validation.png) |
| Product Page | Pass |[Product Page Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fproducts%2F%3Fcategory%3Dby_the_metre) |
| Product Detail Page | Pass | [Product Detail Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fproducts%2F75%2F) |
| Profile Page | Pass | [Profile Page Validation](documentation/testing/validation/html/profiles-validation.png) |
| Bag Page | Pass | [Bag Page Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fbag%2F) |
| Checkout Page | Pass | [Checkout Page Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fcheckout%2F) |
| Checkout Success Page | Pass | [Checkout Success Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fcheckout%2Fcheckout_success%2F411B10FD64CA410DA6A130331F2B74CA) |
| 404 Error Page | Pass | [404 Page Validation](documentation/testing/validation/html/404-page-validation.png) |
| Add Product Page | Pass | [Add Product Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fproducts%2Fadd%2F) |
| Edit Product Page | Pass | [Edit Product Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fproducts%2Fedit%2F10%2F) |

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/base.css | Pass | [static/base.css validation](documentation/testing/validation/css/base-validation.png) |
| checkout/static/checkout/css/checkout.css | Pass | [checkout.css validation](documentation/testing/validation/css/checkout-checkout-validation.png) |
| profiles/static/profiles/css/profile.css | Pass | [profile.css validation](documentation/testing/validation/css/profiles-profile-validation.png) |
| static/admin/css/base.css| Pass | [base.css validation](documentation/testing/validation/css/admin-base-validation.png) |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result | Evidence |
| :--- | :--- | :---: |
| checkout/static/checkout/js/stripe-elements.js | Pass | [stripe-elements.js](documentation/testing/validation/js/checkout-stripe-elements-validation.png) |
| profiles/static/profiles/js/countryfield.js | Pass |[countryfield.js](documentation/testing/validation/js/profiles-countryfield-validation.png) |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

| File | Result | Evidence |
| :--- | :--- | :---: |
| custom_storages.py | Pass | [custom_storages.py validation](documentation/testing/validation/python/custom_storages-validation.png) |
| **SEASIDE_SEWING** |
| seaside_sewing/settings.py | Pass | [settings.py validation](documentation/testing/validation/python/settings-validation.png) |
| seaside_sewing/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/seaside_sewing-urls-validation.png) |
| **BAG** |
| bag/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/bag-apps-validation.png) |
| bag/contexts.py | Pass | [contexts.py validation](documentation/testing/validation/python/bag-contexts-validation.png) |
| bag/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/bag-urls-validation.png) |
| bag/views.py | Pass | [views.py validation](documentation/testing/validation/python/bag-views-validation.png) |
| bag/templatetags/bag_tools.py | Pass | [bag_tools.py validation](documentation/testing/validation/python/bag-bag_tools-validation.png)|
| **CHECKOUT** |
| checkout/admin.py | Pass | [admin.py validation](documentation/testing/validation/python/checkout-admin-validation.png) |
| checkout/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/checkout-apps-validation.png) |
| checkout/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/checkout-forms-validation.png) |
| checkout/models.py | Pass | [models.py validation](documentation/testing/validation/python/checkout-models-validation.png) |
| checkout/signals.py | Pass | [signals.py validation](documentation/testing/validation/python/checkout-signals-validation.png) |
| checkout/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/checkout-urls-validation.png) |
| checkout/views.py | Pass | [views.py](documentation/testing/validation/python/checkout-views-validation.png) |
| checkout/webhook_handler.py | Pass | [webhook_handler.py](documentation/testing/validation/python/checkout-webhook_handler-validation.png) |
| checkout/webhooks.py | Pass| [webhooks.py](documentation/testing/validation/python/checkout-webhooks-validation.png) |
| checkout/test_forms.py | Pass | [test-forms.py validation](documentation/testing/validation/python/checkout-test-forms-validation.png)|
| **HOME** |
| home/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/home-apps-validation.png) |
| home/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/home-urls-validation.png)|
| home/views.py | Pass | [views.py validation](documentation/testing/validation/python/home-views-validation.png) |
| **PRODUCTS** |
| products/admin.py | Pass | [admin.py validation](documentation/testing/validation/python/products-admin-validation.png) |
| products/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/products-apps-validation.png) |
| products/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/products-forms-validation.png) |
| products/models.py | Pass | [models.py validation](documentation/testing/validation/python/products-models-validation.png) |
| products/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/products-urls-validation.png) |
| products/views.py | Pass | [views.py validation](documentation/testing/validation/python/products-views-validation.png) |
| products/widgets.py | Pass | [widgets.py validation](documentation/testing/validation/python/products-widgets-validation.png) |
| **PROFILES** |
| profiles/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/profiles-apps-validation.png) |
| profiles/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/profiles-forms-validation.png) |
| profiles/models.py | Pass | [models.py validation](documentation/testing/validation/python/profiles-models-validation.png) |
| profiles/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/profiles-urls-validation.png) |
| profiles/views.py | Pass | [views.py validation](documentation/testing/validation/python/profiles-views-validation.png) |
| **CONTACT** |
| contact/admin.py | Pass |[admin.py validation](documentation/testing/validation/python/contact-admin-validation.png) |
| contact/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/contact-apps-validation.png) |
| contact/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/contact-forms-validation.png) |
| contact/models.py | Pass | [models.py validation](documentation/testing/validation/python/contact-models-validation.png) |
| contact/test_forms.py | Pass | [test_forms.py validation](documentation/testing/validation/python/contact-test-forms-validation.png) |
| contact/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/contact-urls-validation.png) |
| contact/views.py | Pass | [views.py validation](documentation/testing/validation/python/contact-views-validation.png) |

### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](documentation/testing/lighthouse/home-desk-lh-val.png) |
| Products Page | ![Products Desktop Lighthouse Testing](documentation/testing/lighthouse/products-desk-lh-val.png) |
| Product Details Page | ![Product Detail Desktop Lighthouse Testing](documentation/testing/lighthouse/product-detail-desk-lh-val.png) |
| Add Product Page | ![Add Product Desktop Lighthouse Testing](documentation/testing/lighthouse/add-product-desk-lh-val.png) |
| Edit Product Page | ![Edit Product Desktop Lighthouse Testing](documentation/testing/lighthouse/edit-product-desk-lh-val.png) |
| Bag Page | ![Bag Desktop Lighthouse Testing](documentation/testing/lighthouse/bag-desk-lh-val.png) |
| Checkout Page | ![Checkout Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-desk-lh-val.png) |
| Checkout Success Page | ![Checkout Success Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-success-desk-lh-val.png) |
| Profile Page | ![Profile Desktop Lighthouse Testing](documentation/testing/lighthouse/profile-desk-lh-val.png) |
| Contact Us Page | ![Contact Us Desktop Lighthouse Testing](documentation/testing/lighthouse/contact-desk-lh-val.png) |
| Privacy Policy Page| ![Privacy Desktop Lighthouse Testing](documentation/testing/lighthouse/privacy-desk-lh-val.png)  |
| Terms & Conditions Page | ![Terms Desktop Lighthouse Testing](documentation/testing/lighthouse/terms-desk-lh-val.png) |
| Delivery Policy Page | ![Delivery Desktop Lighthouse Testing](documentation/testing/lighthouse/delivery-desk-lg-val.png)  |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Page Mobile Lighthouse Testing](documentation/testing/lighthouse/home-mob-lh-val.png) |
| Products Page | ![Product Mobile Lighthouse Testing](documentation/testing/lighthouse/products-mob-lh-val.png) |
| Product Details Page | ![Product Detail Mobile Lighthouse Testing](documentation/testing/lighthouse/product-detail-mob-lh-val.png) |
| Add Product Page | ![Add Product Mobile Lighthouse Testing](documentation/testing/lighthouse/add-product-mob-lh-val.png) |
| Edit Product Page | ![Edit Product Mobile Lighthouse Testing](documentation/testing/lighthouse/edit-product-mob-lh-val.png) |
| Bag Page | ![Bag Mobile Lighthouse Testing](documentation/testing/lighthouse/bag-mob-lh-val.png) |
| Checkout Page | ![Checkout Mobile Lighthouse Testing](documentation/testing/lighthouse/checkout-mob-lh-val.png) |
| Checkout Success Page | ![Checkout Success Mobile Lighthouse Testing](documentation/testing/lighthouse/checkout-success-mob-lh-val.png) |
| Profile Page | ![Profile Mobile Lighthouse Testing](documentation/testing/lighthouse/profile-mob-lh-val.png) |
| Contact Us Page | ![Contact Us Mobile Lighthouse Testing](documentation/testing/lighthouse/contact-mob-lh-val.png) |
| Privacy Policy Page| ![Privacy Mobile Lighthouse Testing](documentation/testing/lighthouse/privacy-mob-lh-val.png) |
| Terms & Conditions Page | ![Terms Mobile Lighthouse Testing](documentation/testing/lighthouse/terms-mob-lh-val.png) |
| Delivery Policy Page | ![Delivery Mobile Lighthouse Testing](documentation/testing/lighthouse/delivery-mob-lh-val.png) |

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

| Page | Errors |
| :--- | :--- |
| Home Page | No errors|
| Products Page | No errors |
| Product Details Page | No errors |
| Add Product Page | No errors |
| Edit Product Page | No errors |
| Bag Page | No errors |
| Checkout Page | No errors |
| Checkout Success Page | No errors |
| Profile Page |No errors. It is showing 1 low contrast warning, however I am unable to find where it is as the badge for the contract warning is not actually displaying on the page |
| Contact Us Page | No errors |
| Privacy Policy Page| No errors |
| Terms & Conditions Page | No errors |
| Delivery Policy Page | No errors |
| 404 Error Page | No errors |

## Automated Testing

Automated testing for this project was carried out with [Django TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/). I would write a test, run the test and fix any issues raised before running the test again to confirm it passed. When a test passed I committed it to GitHub.

I also used [coverage](https://pypi.org/project/coverage/) to enable me to see where I was missing tests from to enable me to test my application more thoroughly.

### Coverage Testing

| Coverage for | Result | Evidence |
| :---| :--- | :---: |
| checkout forms.py | 100% | ![checkout forms.py coverage results](documentation/testing/coverage/checkout-forms.png) |
| checkout models.py | % | |
| checkout signals.py | % ||
| checkout views.py | % ||
| checkout webhook_handler.py | % ||
| checkout webhooks.py | % ||
| **CHECKOUT TOTAL** | **%**||

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |
| 1 | Shopper | Easily navigate the site | Find products/information that I am require | A navbar is provided at the top of the page which allows users easy access to their account, shopping bag, search bar and the product categories.   | [Lg Screen Navbar](documentation/testing/user-stories/us-1-a.png) & [Sm Screen Navbar](documentation/testing/user-stories/us-1-b.png) |
| 2 | Shopper | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products | When a user clicks on a category, they are then provided a dropdown with a breakdown of items within the chosen category. If a user choses the view all link, the page will display all items but the user will also be given the choice to refine the products shown via links to the sub-categories at the top of the page. | [Categories Dropdown Menu](documentation/testing/user-stories/us-2.png) |
| 3 | Shopper | View more detail on products | to make an informed decision of if the item suits my requirements | When the user selects a product, they will be taken to the product detail page which lists more information about the item, such as the item name, price and description. A tag will display showing what category the product belongs to, along with a stock tag that displays the stock level for the product. If a rating and colour are available for the product, these will also be displayed in the tags section. A user may hover over the image and they will be shown a magnified view of the item. If they wish to view a larger image, they may click on the image and a larger version of the image will open in a new browser tab.  | [Product Details](documentation/testing/user-stories/us-3.png) |
| 4 | Shopper | View items on clearance/sale easily | Save money  | There is a category choice for users called special offers which allows users to view deals or clearance items. | [View Special Offers](documentation/testing/user-stories/us-4.png) |
| 5 | Shopper | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) | When a user adds a product to their shopping bag, a toast will display to let the user know their addition to their bag was successful, along with showing them the items currently in their bag with their value and price. The toast also displays their total. If a user hasn't reached the threshold for the free delivery offer, they will be notified of this within the toast, which will let them know how much more they need to spend to take advantage of this offer. The shopping bag icon on the navbar will also display their total throughout their visit to the site. | [Toast (free delivery not met)](documentation/testing/user-stories/us-5-a.png) -  [Toast (delivery met)](documentation/testing/user-stories/us-5-b.png) - [Bag Running Total](documentation/testing/user-stories/us-5-c.png) |
| 6 | Shopper | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantities if required | Users are able to view all items selected for purchase from their bag. Their bag will list each item selected for purchase, along with the quantity, item price and subtotal for that item. At the bottom of their bag will be a section that lets them know the total for the items in their bag, the delivery charge (if applicable) and their grand total. | [Bag Page](documentation/testing/user-stories/us-6.png) |
| 7 | Shopper | View ratings for products | make informed decisions about purchasing products | If a rating is available for a product, this will be displayed underneath the item on the products page and also in the tags section on the product details page. | [Products Page Ratings](documentation/testing/user-stories/us-7-a.png) - [Product Detail Page Rating](documentation/testing/user-stories/us-7-b.png) |
| **REGISTRATION & USER ACCOUNTS** |
| 8 | Shopper | Register for an account | Have an account with the site and view my profile | Users can register for an account via the account icon in the navbar, which is available on all pages of the site. If a user doesn't have an account during checkout, they are given an option to create an account on the checkout page. | [Register Dropdown](documentation/testing/user-stories/us-8-a.png) - [Register Link on Checkout Page](documentation/testing/user-stories/us-8-b.png) |
| 9 | Shopper | Receive an email to verify my registration | Verify my account was created successfully | Users receive an email asking them to click the link in the email to verify their email address and complete the registration proces. | [Email Verification for creating an account](documentation/testing/user-stories/us-9.png) |
| 10 | Shopper | Log in and out | Keep my account information secure | Users are able to log in and out of their account through the account icon on the navbar which is accessible on all pages of the site. | [Account Logout](documentation/testing/user-stories/us-10.png) |
| 11 | Shopper | View a profile page | Set a default delivery address and view previous purchases | Users are able to view their profile page once logged in via the account icon on the navbar which is accessible on all pages of the site. Their profile allows them to select their default delivery information (which if filled out will pre-populate the checkout delivery information if the user is signed in). Users are also able to view their previous orders within their profile. These are listed most recent first and give the first part of the order number, the date and time of the order, items ordered with their quantities along with the order total. If the user clicks on the order number, they will then be taken to a more detailed breakdown of their order. | [Profile Page](documentation/testing/user-stories/us-11.png) |
| 12 | Shopper | Reset my password | Recover my account | If a user has forgotten their password, they can click on the forgotten password button during login to reset their password. | [Forgotten Password](documentation/testing/user-stories/us-12.png) |
| **SORTING & SEARCHING** |
| 13 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products | Users may view products bases on their price, rating or category from the navbar by selecting all products and then the option they want from the dropdown.  | [Category Sorting](documentation/testing/user-stories/us-13.png) |
| 14 | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name | Users are given chance to sort products on the products pages via a sort dropdown in the top right. This allows users to sort products by their name, price, rating and category - ascending or descending. | [Sort Products](documentation/testing/user-stories/us-14.png) |
| 15 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as fabric or haberdashery | Users may select the all products link on the navbar and then choose how they wish to sort | [All Products sorting](documentation/testing/user-stories/us-15.png) |
| 16 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | Users are provided with a search bar in the navbar which allows them to search for items. The search not only checks the product name, but also their description for the search term used.  | [Search Bar](documentation/testing/user-stories/us-16.png) |
| 17 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | Users are given feedback on their search term and the number of products which match the search term on the results page in the top left. | [Search Results](documentation/testing/user-stories/us-17.png) |
| **PURCHASING & CHECKOUT** |
| 18 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product quantity | Users are provided a quantity input box on the product detail page which allows them to increase or decrease the quantity required using the plus or minus buttons. The buttons are coloured to also provide visual understanding for the user of their purpose. Users may also type the value they wish to purchase directly into the quantity box. Once a user adds a product to their bag they receive a toast notification of the product they've added together with the quantity.  | [Quantity Selection](documentation/testing/user-stories/us-18.png) |
| 19 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive | When the user views their bag, they will be presented with a list of all items selected for purchase, information shown will include an image of the item, the items name, the quantity of the item selected, the unit price of the item and the subtotal price for that item. At the bottom of the bag the user will be given the subtotal for all the items they are purchasing, the delivery fee (if applicable) and the grand total of their order. | [Bag Page](documentation/testing/user-stories/us-19.png) |
| 20 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout | The users are given a quantity selector in the bag that looks the same as on the product detail page to provide continuity and familiarity for the user. Once the user has selected the new quantity of the item, they click the update link under the quantity input and the page will reload with the new quantities. If a user decides they would like to remove the item completely from their bag they can remove the item by clicking the remove link under the product. This removes the product and shows a toast which confirms that the user has successfully deleted the selected item from their bag.  | [Bag Quantity Selector](documentation/testing/user-stories/us-20.png) |
| 21 | Shopper | Easily enter my payment information | Check out quickly and with no hassles | When a user is taken to the checkout page they can clearly see 3 sections of information that need to be completed to complete their order - their details, the delivery information and the payment information. Feedback is provided to the user whilst completing the checkout if any information they give is invalid. | [Payment](documentation/testing/user-stories/us-21.png) |
| 22 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | Seaside Sewing provides its checkout facilities through Stripe | [Stripe Security](https://stripe.com/docs/security?locale=en-GB) |
| 23 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | Users are taking to an order confirmation page once they have successfully checked out which provides them with their order information, such as their order details and the order date.  They are also shown their order details which lists the items they have purchased along with their quantity and the price of the item. A delivery section provides them with information on where they are having their order delivered to and finally they are shown the billing information section which provides them with their total, the delivery fee (if applicable) and the grand total for their order. | [Order Confirmation](documentation/testing/user-stories/us-23.png) |
| 24 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records | Upon successful checkout, a user will be sent a confirmation email to the email address provided at checkout to confirm their order. | [Email Confirmation](documentation/testing/user-stories/us-24.png) |
| **ADMIN & STORE MANAGEMENT** |
| 25 | Store Owner | Add a product | Add new items to my store | Admin are able to add new products to the store directly from the store website when logged in as a superuser. This option is provided to them under the account icon in the navbar - product management. If an admin clicks on this link, they will be taken to the add product page where they can add a new item to be added to the store. | [Add Product](documentation/testing/user-stories/us-25.png) |
| 26 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria | When a superuser is logged in, they are shown an edit button underneath each product on the products page, and are also shown an edit button when viewing a product. Once clicked they will be taken to a page similar in layout to the add product page (to provide continuity and familiarity) and are able to edit the products information. | [Edit Product](documentation/testing/user-stories/us-26.png) |
| 27 | Store Owner | Delete a product | Remove items that are no longer for sale | When a superuser is logged in, they are shown a delete button underneath each product on the products page, and are also shown a delete button when viewing a product. Once clicked they a modal will pop up asking them to confirm they wish to delete this product, and notifying them that this action cannot be undone. The superuser is given a choice to delete the product or cancel. The modal provides a layer of protection to product deletion and should prevent accidental deletion of products. | [Delete Product](documentation/testing/user-stories/us-27.png) |

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
| **NAVBAR** |
| Search Bar | Search with no search term entered will display a toast error message letting the user know they haven't entered any search criteria and to try again | Clicked search button with no search term | Error toast displayed | Pass |
| | Search with search terms entered will display the results of that search on the products page. In the top left corner the user will be told how many products matched along with search term entered | Searched for soft | Products page loads up with results of search. Top left tells me there were 16 products found for "soft"| Pass |
| Account Icon | User not logged in - 2 options should be presented to a user if they are not logged in, one to register and one to login | Clicked account icon when not logged in | Dropdown menu with login and register presented | Pass |
| | User Logged in - When a user is logged in they should be shown a dropdown menu dependant on their privileges - standard users are shown the profile and logout links. Superusers are shown product management, profile and logout links. | Viewed links as a superuser and as a standard user | The correct links are displayed dependant on the users privileges | Pass |
| | Account icon links should take the user to the expected page - eg the profile link should take the user to their profile | Clicked on links | Each link takes the user to the correct page for the link | Pass |
| Bag icon | When items are added to the bag, the value underneath the bag should automatically update (this will include the delivery charge if the free delivery limit has not been reached) | Add items to cart to check the value is added | The value adds the correct amount for each product added, and includes the delivery fee if the free delivery limit has not been reached | Pass |
| | Clicking on the bag icon takes the user to their bag page which will display what they have in their bag (if any) or a message to let them know their bag is empty | Clicked on the bag icon with an empty bag and with items | Taken to the bag page, which displays items (if any in bag) or a message if no items | Pass |
| Categories Navbar | Home link - this loads the home page if clicked | Clicked home | Taken to home page | Pass |
| | All products - this allows the user to select how they would like to display all the products, either by rating, price, category or show all products. All links in the dropdown menu should take you to the correct page | Tested each of the links to ensure products display correctly | |
| | Categories links when clicked display a dropdown menu of the products within that category. Each link should direct you to the correct page  | Clicked each of the links to ensure taken to the correct page | Taken to the correct page  | Pass |
| Navbar Responsiveness | Navbar should be displayed using a hamburger menu toggle on smaller screens | Checked the site on smaller screens | Navbar is displayed using a hamburger menu toggle | Pass |
||||||
| **FOOTER** |
| About Section | The links in the about section should open the correct page when clicked | Clicked each link | Taken to the correct page | Pass |
| Contact Section | Clicking on Contact Us Form should take the user to the contact form | Clicked link | Taken to the contact form | Pass |
|| Social Media Icons open the social page in a new browser tab | Clicked each icon | Social page opened in a new browser tab | Pass |
| Kera Cudmore Link | Takes the user to my Github Profile in a new browser tab | Clicked link | Github profile opened in a new tab | Pass |
| Footer Responsiveness | The footer sections should become stacked on smaller screens | Looked at site on smaller screens | Sections of footer became stacked | Pass |
||||||
| **HOME PAGE** |||||
| Category Cards | Clicking on a card should take the user to the products page for that category | Clicked cards and checked the right category loads | The correct categories are displayed for the right cards | Pass |
||||||
| **PRODUCTS PAGE** ||||||
| Sort By | Sort By dropdown | Products are sorted correctly depending on which option is chosen | Chose the different options and check to see the products are displayed by that criteria | Products are displayed according to the chosen criteria | Pass |
| Product details | Clicking on a product image will load the products detail page | Clicked on a product image | The product detail page loads for that product | Pass |
| Back to top button | Clicking on the back to top button will return the user to the top of the page to enable them to easily use the sites navigation | Clicked the back to top button while partway down the all products page | Returned to the top of the page | Pass |
| Category Tag underneath product | Clicking on the category tag will load the products page for that category | Clicked a product tag on the all products page | The products page reloads showing only the category of the tag clicked | Pass |
||||||
| **PRODUCT DETAIL PAGE** |||||
| Hover over image | When hovering over an image, you should be able to see the magnify lens to see a more details view of the product. | hovered over the image | Magnify lens appears showing a more detailed view of the product | Pass |
| Click on image | When you click on an image, a new tab should open displaying the image| Clicked on the product image | A new browser tab opened with the image | Pass |
| Quantity Plus Button | When you click the plus button the quantity should increase by one until you reach the stock level for the product. Once you reach the stock level, the button becomes disabled. If you lower the quantity, the plus button will reenable. | Clicked on the plus button to the stock level | Clicking on the plus button increments the quantity by 1, and once you reach the stock level the button is disabled. Lowering the quantity reenabled the plus button. | Pass |
| Quantity Minus Button | The minus button will be disabled at 1, if the quantity is more than one, the minus button will be enabled. The minus button should decrement the quantity by one | Added product, then used the minus button to lower the quantity |The button is disabled when the product quantity is 1. The quantity is decreased by 1 each time you click. | Pass |
| Quantity input | If a user manually enters a value larger than the stock level and tries to add the product to their bag, they will be presented with a tooltip that lets them know the value must be equal to or less than the stock level | Add 200 to quantity input for a product with stock level of 44 and click add to bag. | A tooltip pops up with a message letting me know that the value must be equal or less than 44. | Pass |
| Add to bag button | When clicked the quantity of the item will be added to the bag. A success toast message will display letting the user know the quantity of the product added to the bag. | Incremented quantity to 4 and clicked add to bag button | A toast displays to let the user know that they have added 4 of the product to their bag and shows the image of the item with the title and quantity in the bag | Pass |
| Back button | When clicked the user will be taken back to the products page | Clicked the back button | Taken to the products page | Pass |
||||||
| **BAG** |||||
| Quantity Plus Button | When you click the plus button the quantity should increase by one until you reach the stock level for the product. Once you reach the stock level, the button becomes disabled. If you lower the quantity, the plus button will reenable. | Clicked on the plus button to the stock level | Clicking on the plus button increments the quantity by 1, and once you reach the stock level the button is disabled. Lowering the quantity reenabled the plus button. | Pass |
| Quantity Minus Button | The minus button will be disabled at 1, if the quantity is more than one, the minus button will be enabled. The minus button should decrement the quantity by one | Added product, then used the minus button to lower the quantity |The button is disabled when the product quantity is 1. The quantity is decreased by 1 each time you click. | Pass |
| Quantity input | If a user manually enters a value larger than the stock level and tries to update their bag, they will be presented with an error toast that lets them know the stock level for the product and asks them to adjust the quantity and try again. | Add 200 to quantity input for a product with stock level of 44 and click update. | An error toast displays with a message letting me know that the stock level of the product is 44 and to edit my quantity and try again. | Pass |
| Update Link | When a products quantity has been updated and the link clicked, a success toast displays to let the user know the update was successful along with the product and the quantity. If the user tries to update a product over the stock level they are shown an error toast. | Updated a products quantity within the stock level. Updated a products quantity over the stock level | Within the stock level, a success toast is shown with the product information and quantities. Over the stock level an error toast is displayed informing the user of the stock level and asking them to try again | Pass |
| Remove Link | When clicked the product will be removed from the basket and a success toast displayed to let the user know the action was successful, along with letting them know which product they have removed and the shopping bag page updates | Clicked the remove link and a success toast is shown letting me know what product has been removed from the bag | Pass |
| Back to shop button | When clicked this will take the user to the products page | Clicked back to shop button in an empty bag and in a bag with products | Taken back to the products page each time. | Pass |
| Special Offers Button in empty bag | Clicking the button takes the user to the products page displaying all the products in the special offers categories | Clicked button | Taken to the special offers categories products page | Pass |
| Secure Checkout Button | When clicked the user is taken to the checkout page to fill in their details and make payment | Clicked button | Taken to checkout | Pass|
| Go to secure checkout button on success toast | A toast will be displayed each time a user adds an item to their bag which lets them know the product and quantity along with the total excluding delivery and if they haven't reached the free delivery threshold, they will be informed of how much more they need to spend to qualify. They are also shown a go to secure checkout button that allows them to navigate to the bag to confirm their items before checking out | Add product to bag, click the checkout button | The toast displays the item added to the bag, and any previous items added, together with the quantity, total excluding delivery and the spend to get free delivery message as I haven't reached the threshold. Clicking the button takes me to the bag to review my order | Pass |
||||||
| **CHECKOUT PAGE** |||||
| Form Validation | The user is informed if they have not filled in required information | Submitted the form with required fields left blank | A tooltip informs the user that they need to fill in the required fields. | Pass |
| Save delivery information checkbox | When clicked, the current delivery information in the form is saved to the profile | Filled out form and checked the profile after checkout | Profile information was populated with the correct information | Pass |
| Login link on checkout page | Users are given the option to log into their account during checkout, which will allow them to save their order to their profile. If clicked the user is taken to the log in page, once logged in they can navigate to their basket to continue checkout | Not logged in as a user. Clicked the log in link, logged in | Logged in successfully and received a success toast, redirected to the home page and products are still saved in basket | Pass |
| Register Link on checkout page | Users are given the option to register for an account to be able to save their order details before checking out | Click the link, create an account | Redirected to home page and bag available | Pass |
| Payment information section | If the user has entered incorrect information in the payment section, they are given feedback about the error| Entered an invalid card number in the payment section | Information is displayed in red text below the payment information section informing the user that the number they have entered is invalid | Pass |
| Complete order button | Once the user has clicked the complete order button they should be shown a loading status overlay to let the user know their payment is processing. Once checkout has been completed they are then redirected to the checkout success page which gives a breakdown of the order | Clicked button | A loading overlay displays and then the checkout success page is displayed | Pass |
||||||
| **CHECKOUT SUCCESS PAGE** |||||
| View our latest deals button | When clicked the user is taken to the product page showing the deals category | Clicked the button | Taken to the products page showing products in the deals category | Pass |
| Order Confirmation Email | Upon successful checkout the user should also receive an email confirming their order at the email address provided during checkout | Made a successful purchase through the site | An email confirmation was received (this can sometimes go to junk) | Pass |
||||||
| **PROFILE PAGE** |||||
| Update default delivery information | Once the user has filled in the default delivery information they wish to store and clicked the update button, the information should be saved and be available in their profile and at checkout | Add default delivery information, save and then check the information displays in their profile and at checkout | Page reloads with the updated information pre-populated and a success toast is displayed to let the user know their profile was updated successfully | Pass |
| View previous orders made from my account | Users should be able to click on the first part of their order number in the order history section and be taken to the checkout success page for that order. A toast will also inform the user that they are viewing a previous order summary for the order number | Clicked on an order number | The checkout success page is displayed with the order summary and an alert toast is displayed letting the user know this is a past confirmation for the order number | Pass |
||||||
| **CONTACT US FORM** |||||
| Form Validation | If the user doesn't fill in the required fields and tries to submit the form, they will be shown a tooltip letting them know they need to fill in the required fields | Submit the form without filling in the required fields | Tooltip lets me know which fields I need to fill in | Pass |
| Send contact form | Once sent the user should be shown the contact page with a message thanking them for their enquiry and giving them a button to view the latest deals. A toast should also be displayed letting them know their enquiry was sent successfully | Fill in the contact form and clicked send. | Contact us page displays with thank you message and toast displayed letting me know enquiry was sent successfully. | Pass |
| **SUPERUSER OPTIONS**|||||
| Account icon Product management dropdown link | This links should only be displayed to a superuser. When clicked, the superuser will be taken to the add product page. If a regular user tries to manually view this page by using the url, they are not able to view the page and an error toast displays to let them know only administrators can perform that task. | Signed in as superuser and clicked the link. Signed in as a regular user and added the url into the address bar. | Link only shown to superuser. Superusers are taken to the add product page. Regular users are shown an error toast that informs them only administrators can perform that action. | Pass |
| Add Product Form Validation | The form will only be submitted and the new product created if the required fields have been filled in | Tried to submit the form without filling in all required fields | Tooltips let me know which fields need to still be filled in | Pass |
| New product created saved in the products section of the admin page | When a product is created, a record of it should also be displayed in the products section of the admin page | Create a new product, navigate to the admin products section | We can see the record created for the new product | Pass |
| Edit Product Link | This link should only be shown when logged in as a superuser. When the edit link is clicked (either on the products page or from the product detail page) superusers are taken to the edit product page. If a regular user tries to manually access the edit page using the url, they are given an error toast letting them know only administrators can perform that action | Clicked the Edit link as a superuser.  Logged in as regular user and manually enter the url into the address bar. | The edit link is only shown when logged in as a superuser. Superusers are shown the edit product page and regular users are shown an error toast letting them know that only administrators have permission to perform that action. | Pass |
| Delete Product Link | This link should only be shown to superusers. when clicked a superuser should be shown a modal asking them to confirm they would like to delete the product, and reminds them that this action cannot be undone. If a regular user tries to manually access this page using the url, they should be shown an error toast telling them they cannot perform the action. | Clicked the link as a superuser. Manually accessed the url as a regular user. | This link is only shown to superusers. The superuser is shown a modal that asks if they are sure they want to delete the product as this action cannot be undone. Regular users are shown an error toast letting them know that only administrators can perform that action | Pass |
| Contact form sent | All contact forms submitted to the site are stored in the contact form section of the admin page. It will display the name, email address, phone number (if filled in) and message, and will also detail the date of the contact along with a replied checkbox to enable the admin to keep track of whether they have responded | Open the admin page and navigate to the contact form section, select a contact email and view the information. | Information is displayed about the users name, email address, phone number (if entered), message sent and the date it was sent along with a checkbox for replied. | Pass |

## Bugs

### Solved Bugs

| No | Bug | How I solved the issue | Evidence |
|:--- | :--- | :--- | :---: |
| 1 | The jQuery was not working for the toasts. | I researched this issue on slack and it seemed to be a known error with the toasts and bootstrap 5. As I am on a very tight deadline for this project and could not find a solution over an afternoon, despite bootstrap 5 being compatible for use with jQuery, I have decided to unfortunately bite the bullet and revert the bootstrap version used in the project down to 4.6.2. This has also meant that I have had to spend a bit of time updating some of the bootstrap classes used in the project (such as float-end to float-right) and has meant a large refactor of the categories and account navbars. | |
| 2 | Update link in bag not updating quantities | I spent a lot of time looking into this issue, only to come back the next day and realise that I had placed the update link after the delete link. This meant that the previous element was then the delete link and not the form as it should have been. I have moved the update link above the delete link and it now works correctly. | |
| 3 | Delete link in bag and update quantity to 0 were throwing a keyerror and internal server error 500 | I had added int: into the item_id part of the path in the bag urls file. This was preventing the functions working correctly | |
| 4 | Instance in the checkout view | When trying to checkout I received a valueError stating there was no HttpResponse object, and that it returned None. This was due to me not defining the instance. I needed to add line 40 to my checkout views, and also needed to add a return for if the instance failed (this step was missing from the BA tutorial) | ![instance-error](documentation/bugs/instance-error.png) |
| 5 | Float error in checkout | I was getting the following error when checking out. This error was due to my delivery fee in the settings.py file being declared as a float, and the order total being a decimal. I could either cast the order total to a float or import decimal into settings and define the delivery fee as a decimal to prevent an error with the delivery fee. I decided to import decimal into the settings folder. | ![Float Error](documentation/bugs/float-error.png) |
| 6 | Delivery Fee not displaying correctly in the admin | it was adding the total to the delivery fee - so just needed to remove the total and only reference the delivery fee |  |
| 7 | Webhooks returning 400 & 500 errors | There were 2 spelling errors and a wrong class name causing the issues, once these were corrected, the webhooks work as expected | ![Webhook error](documentation/bugs/wh-error.png) |
| 8 | Success toasts were not displaying when adding items, but did display when logging in | I checked that the syntax was correct for the bootstrap version being used and knew that the toast was there as it was showing in the page code. Ed from tutoring saved the day when he spotted that I had omitted the `block.` from the front of my super tag in the bag.html. This meant that I was overwriting the toasts script with the scripts in the base.html file rather than adding to it. |
| 9 | Adding additional products already in the bag were not being added to the current quantity but overwriting it. The item_id was being passed to the view as an integer, but was then being converted to a string in the bag. | This one really puzzled me. I went back through the course content, searched on slack and did some googling but couldn't find a way to fix this. I therefore contacted tutor support and after trying a number of different possible solutions the only way we could find that worked was to cast the item_id as a string at the beginning of the add to bag view. This is obviously not a perfect solution, but works for the moment until I can dig into this further to find the cause. Update: We discovered that I was actually specifying the item_id as an integer in the path for the add to bag view, by removing this from the path, the add to bag function works as it should without having to cast the item_id to a string. This solution is much more elegant and so has been implemented. | ![Solved Bug No 9 - interger and string values](documentation/bugs/solved-bug-9.png) |
| 10 | Implementing enabling/disabling of the quantity buttons using the stock value in the shopping bag. I had managed to get this feature working within the product details page, however in the bag the plus button would disable once it reached the stock value, but if the value was lowered it would not enable. | This was an easy fix once someone pointed out to me that an item only had a quantity and product being passed to it. To solve the issue I needed to pass the stock value to the bag in the bags context. Once I did this the quantity buttons worked as I expected, the plus button would disable once it reached the stock value, and if the user reduced the quantity to under this amount, the plus button was enabled. | ![Solved bug 10](documentation/bugs/solved-bug-10.gif) |
| 11 | Product description was turning bold on addition of item to cart | Removed some strong tags not needed from the success toast | ![Solved bug 11](documentation/bugs/solved-bug-11.gif) |
| 12 | The confirmation email is not rounding the values to 2 decimal places and the contact.email value is not displaying | I solved this by adding `float:2` to the values in the confirmation email body file. | ![Confirmation Email Bug](documentation/bugs/confirmation-email.png) |
| 13 | I was receiving an error in validation due to using `mailto:` with a subject that contained spaces. | I decided that it would probably be better practice to have a contact form on the site itself, and link to the contact page. |
| 14 | Getting side scroll on pages with a small white slice on the right | Using dev tools I could see that this was being caused by the footer having a margin added from the bootstrap column classes. I have solved this by adding the contents of the footer into a container. | ![Side Scroll Bug](documentation/bugs/solved-bug-14.png) |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |
| 1 | The confirmation email for orders is not displaying the contact email variable | ![Email not showing](documentation/testing/user-stories/us-24.png) |
