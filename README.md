# Seaside Sewing

image

Seaside Sewing is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe as the payment processor.

This project was created as my fourth milestone project for my Level 5 Diploma in Web Application Development with the Code Insitute.

link to deployed site: here

![GitHub contributors](https://img.shields.io/github/contributors/kera-cudmore/seaside-sewing) ![GitHub last commit](https://img.shields.io/github/last-commit/kera-cudmore/seaside-sewing) ![GitHub language count](https://img.shields.io/github/languages/count/kera-cudmore/seaside-sewing) ![GitHub top language](https://img.shields.io/github/languages/top/kera-cudmore/seaside-sewing)

---

## Contents

* [User Experience](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
  * [User Journey](#user-journey)
* [Features](#features)
  * [General Features of The Site](#general-features-of-of-the-site)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Database Used](#database-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
  * [Stripe](#stripe)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

responsive site image here

---

## User Experience

### Project Goals

Seaside Sewing is a Business to Consumer (B2C) ecommerce site.

The sites audience is people who have a love of sewing and quilting and will cater to sewists from beginners through to experts, by selling a range of items over different price points.

### User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| 1 | Shopper | Easily navigate the site | Find products/information that I am require |
| 2 | Shopper | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products |
| 3 | Shopper | View more detail on products | to make an informed decision of if the item suits my requirements |
| 4 | Shopper | View items on clearance/sale easily | Save money  |
| 5 | Shopper | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) |
| 6 | Shopper | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantites if required |
| 7 | Shopper | View reviews for products | make informed decisions about purchasing products |
| **REGISTRATION & USER ACCOUNTS** |
| 8 | Shopper | Register for an account | Have an account with the site and view my profile |
| 9 | Shopper | Receive an email to confirm my registration | Verify my account was created successfully |
| 10 | Shopper | Log in and out | Keep my account information secure |
| 11 | Shopper | View a profile page | Set a default delivery address and view previous purchases |
| 12 | Shopper | Reset my password | Recover my account |
| 13 | Shopper | Review products | Leave a rating/review on products |
| **SORTING & SEARCHING** |
| 14 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products |
| 15 | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 16 | Shopper | Sort multiple categories of products simutaneously | Find the best-priced or best-rated products across broad categories, such as fabric or habedashery |
| 17 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| 18 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |
| 19 | Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 20 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| 21 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 22 | Shopper | Easily eneter my payment information | Check out quickly and with no hassles |
| 23 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 24 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 25 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **ADMIN & STORE MANAGEMENT** |
| 26 | Store Owner | Add a product | Add new items to my store |
| 27 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 28 | Store Owner | Delete a product | Remove items that are no longer for sale |

---

## Design

### Colour Scheme

I have based the colour theme for the site around the main image used at the top of the site, a lighthouse on an island surrounded by water. The shades of blue fit nicely with a seaside theme, and the red gives a nice contrast to the blue.

Text throughout the site will be either black or white, depending on the background colour.

image of colour scheme here

### Typography

All fonts were sourced from [Google Fonts](https://fonts.google.com/). I used [Font Joy](https://fontjoy.com/) to enable me to view the font choices together to make sure that they worked well together.

![Fonts Chosen for the site](documentation/fonts.png)

I have chosen to use Parisienne, a handwriting font, for the site name as I feel that it gives a look of an ocean wave, with its ebb and flow. I am limiting the use of this font to the sites name as due to the font being a cursive, it is not very accessible.

![Parisienne Font](documentation/parisienne-font.png)

I have chosen to use Overpass for all other text on the site. This font is sans-serif font, which is very accessible as a web font.

![Overpass Font](documentation/overpass-font.png)

### Imagery

Due to the name of the site, I have chosen to go with images of the seaside.

The hero image for the site is of a lighthouse on an island surrounded by water. The footer is an image of sealife underwater on the ocean floor. I feel these images give the site a cohesive feel - as we start at the top of the site above the water, and then we travel down until we get to the bottom of the page to the footer, which is the ocean floor. I feel it gives the site a bit of a whimsical feel, which I wanted, as a lot of e-commerce sites can be very bland and all look the same.

### Wireframes

Wireframes for the project were created using [Balsamiq](https://balsamiq.com/)

* Home
* Register
* Login
* Profile
* Bag
* Checkout
* Checkout Success
* Products
* Product Detail
* Edit Product
* Delete Product
* 404 Error

### Database Schema

I have used a relational database for this project, due to the relationships

image of schema

### User Journey

flow of site

---

## Features

### General Features of of the site

Each page of the site shares the following:

* Favicon
* Navbar
* Footer

site pages images

### Future Implementations

In future implementations I would like to:

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. This has been have achieved by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient colour contrast throughout the site.

---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python

### Database Used

sqlite3 for development.
[ElephantSQL](https://www.elephantsql.com/) for deployment.

### Frameworks Used

[Django](https://www.djangoproject.com/) - Version 3.2.16 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version *** - A framework for building responsive, mobile-first sites.

### Libraries & Packages Used

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 0.41.0 - Used for authentication, registration & account management.

### Programs Used

[Am I Responsive](https://ui.dev/amiresponsive) - To create the responsive images of the site on a variety of device sizes.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Favicon.io](https://favicon.io/) - To create the favicon.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

[Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

[Shields.io](https://shields.io/) - To add badges to the projects documentation.

[Tiny PNG](https://tinypng.com/) - To compress images used in the README.

### Stripe

[Stripe](https://stripe.com/gb) has been used in the project to implement the payment system.

---

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project to Heroku:

1.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click on the fork button in the top right of the page.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

---

## Credits

### Code Used

### Content

### Media

* [Lighthouse Header Image](https://www.vecteezy.com/vector-art/8273454-lighthouse-in-on-the-island-in-the-middle-of-the-sea) - Designed by Graphics RF, sourced from Vecteezy
* [Underwater Footer Image](https://www.vecteezy.com/vector-art/9102436-silhouette-of-coral-reef-with-fish-and-divers-on-blue-sea-background-underwater-vector-illustration) - Designed by duangdee123050146, sourced from Vecteezy

* [Groves & Banks Ltd](https://www.grovesltd.co.uk/) - For allowing me permission to use any of the images of their products from their website.

* [Noimage](https://www.canva.com/search/templates?q=lighthouse) - Created for free on Canva, utilising their design elements (Elegant minimalistic logo with lighthouse for seafood cafe) in the colour theme of my site.

### Acknowledgments

I would like to acknowledge the following people who have helped me with completing this project:

* My family for their patience and support whilst working on my final project.
* My Code Institute mentor [Adegbenga Adeye](https://github.com/deye9).
* Nerd Alert for their constant support and encouragment while completing this project.
