# Seaside Sewing - Testing

image of the site

[Visit Seaside Sewing Here](https://dashboard.heroku.com/apps/seaside-sewing)

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

## Bugs

### Solved Bugs

| No | Bug | How I solved the issue | Evidence |
|:--- | :--- | :--- | :---: |
| 1 | The jQuery was not working for the toasts. | I researched this issue on slack and it seemed to be a known error with the toasts and bootstrap 5. As I am on a very tight deadline for this project and could not find a solution over an afternoon, despite bootstrap 5 being compatible for use with jQuery, I have decided to unfortunately bite the bullet and revert the bootstrap version used in the project down to 4.6.2. This has also meant that I have had to spend a bit of time updating some of the bootstrap classes used in the project (such as float-end to float-right) and has meant a large refactor of the categories and account navbars. | |
| 2 | Update link in bag not updating quantities | I spent a lot of time looking into this issue, only to come back the next day and realise that I had placed the update link after the delete link. This meant that the previous element was then the delete link and not the form as it should have been. I have moved the update link above the delete link and it now works correctly. | |
| 3 | Delete link in bag and update quantity to 0 were throwing a keyerror and internal server error 500 | I had added int: into the item_id part of the path in the bag urls file. This was preventing the functions working correctly | |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |
| 1 | | |
