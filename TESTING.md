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

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

#### Mobile Results

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved?	| |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |
| 1 | Shopper | Easily navigate the site | Find products/information that I am require | | |
| 2 | Shopper | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products | | |
| 3 | Shopper | View more detail on products | to make an informed decision of if the item suits my requirements | | |
| 4 | Shopper | View items on clearance/sale easily | Save money  | | |
| 5 | Shopper | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) | | |
| 6 | Shopper | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantites if required | | |
| 7 | Shopper | View reviews for products | make informed decisions about purchasing products | | |
| **REGISTRATION & USER ACCOUNTS** |
| 8 | Shopper | Register for an account | Have an account with the site and view my profile | | |
| 9 | Shopper | Receive an email to confirm my registration | Verify my account was created successfully | | |
| 10 | Shopper | Log in and out | Keep my account information secure | | |
| 11 | Shopper | View a profile page | Set a default delivery address and view previous purchases | | |
| 12 | Shopper | Reset my password | Recover my account | | |
| 13 | Shopper | Review products | Leave a rating/review on products | | |
| **SORTING & SEARCHING** |
| 14 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products | | |
| 15 | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name | | |
| 16 | Shopper | Sort multiple categories of products simutaneously | Find the best-priced or best-rated products across broad categories, such as fabric or habedashery | | |
| 17 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | | |
| 18 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | | |
| **PURCHASING & CHECKOUT** |
| 19 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product quantity | | |
| 20 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive | | |
| 21 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout | | |
| 22 | Shopper | Easily eneter my payment information | Check out quickly and with no hassles | | |
| 23 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | | |
| 24 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | | |
| 25 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records | | |
| **ADMIN & STORE MANAGEMENT** |
| 26 | Store Owner | Add a product | Add new items to my store | | |
| 27 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria | | |
| 28 | Store Owner | Delete a product | Remove items that are no longer for sale | | |

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
| 9 | Adding additional products already in the bag were not being added to the current quantity but overwriting it. The item_id was being passed to the view as an integer, but was then being converted to a string in the bag. | This one really puzzled me. I went back through the course content, searched on slack and did some googling but couldn't find a way to fix this. I therefore contacted tutor support and after trying a number of different possible solutions the only way we could find that worked was to cast the item_id as a string at the beginning of the add to bag view. This is obviously not a perfect solution, but works for the moment until I can dig into this further to find the cause. |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |
| | | |