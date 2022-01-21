# EXPERIA - The unique experience platform.

[View the live project here.](https://experia-app.herokuapp.com/)

<img src="">

## Objective
This Website was created for the purpose of implementing a fullstack Django framework website with Stripe payment integration.
The project allows users to explore a range of different experiences, purchase them, and also create their own unique experiences available for purchase. The website was built using Bootsrap (HTML, CSS), JS, Python, Django, Stripe, AWS S3.

## UX & Design


## Strategy

#### Project Goal
The project goal or 'use case' of the website is to act as a platform where people can browse and purchase unique experiences in their own city or perhaps a city that they plan on visiting. There is also an option for a user to create their own unique experiences which they can make available for purchase.

The project is also to give me experience building a full stack e-Commerce website that handles payments.

#### Ideation
The concept for Experia came from my own experiences travelling, I found sometimes it would be hard to find things to do in some cities or I was not interested in what was on offer.
#### Site owner goals
- Make the website design user-friendly
- Make the website accessible for all
- Retain users and create recurring visits
#### User goals
- Ease of use
- Ease of navigation
- Ease of purchase
- Satisfaction
- Informative feedback
- Consistant features


## User Experience (UX)

-   ### User stories


|                              | As a:          | I want to be able to:                                     | So that I can:                                                                                              |   |   |
|------------------------------|----------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---|---|
|        View & navigate       |                |                                                           |                                                                                                             |   |   |
|                            1 | Customer       | View available products/service                           | Select ones to purchase                                                                                     |   |   |
|                            2 | Customer       | View products/service details                             | Identify, price, description, rating, availability, image                                                   |   |   |
|                            3 | Customer       | Identify products/service deals, special offers           | Purchase product/service(s) at a discount                                                                   |   |   |
|                            4 | Customer       | View my total spend at any time                           | Prioritise budget and stay generally informed                                                               |   |   |
| Registration & user accounts |                |                                                           |                                                                                                             |   |   |
|                            5 | Site browser   | Register for an account                                   | Have a personal account and view my profile                                                                 |   |   |
|                            6 | Site browser   | Login and logout                                          | Access my personal account info                                                                             |   |   |
|                            7 | Site browser   | Recover password if forgotten/lost/corrupted              | Recover access to my account                                                                                |   |   |
|                            8 | Site browser   | Receive email confirmation after registration             | Securely verify my account using personal email                                                             |   |   |
|                            9 | Site browser   | Have a personalised user profile                          | View order history, current orders and payment information                                                  |   |   |
|      Host an experience      |                |                                                           |                                                                                                             |   |   |
|                           10 | Account holder | Create an experiece                                       | Offer my own unique experience                                                                              |   |   |
|                           11 | Account holder | Host it on the website                                    | People can purchase the experience                                                                          |   |   |
|      Sorting & searching     |                |                                                           |                                                                                                             |   |   |
|                           12 | Customer       | Sort list of available products                           | Identify best rated, best priced and categorically sorted products                                          |   |   |
|                           13 | Customer       | Sort category of product                                  | Find best-price, best-rated product in a category or sort product by name                                   |   |   |
|                           14 | Customer       | Sort multiple categories simultaneously                   | Find best-price, best-rated product in a category or sort product by name across categories such as 'Tours' |   |   |
|                           15 | Customer       | Search for product by name or description                 | Find a specific product I'd like to purchase                                                                |   |   |
|                           16 | Customer       | See what I've searched and number of results              | Find out if a product I want is available                                                                   |   |   |
|                           17 | Account holder | Make a wish list                                          | Save products I may wish to purchase in the future                                                          |   |   |
|      Purchase & checkout     |                |                                                           |                                                                                                             |   |   |
|                           18 | Customer       | Easily select and quantity of product/service             | Avoid purchasing the wrong product, quantity                                                                |   |   |
|                           19 | Customer       | View items in shopping bag                                | Identify total cost of my purchase                                                                          |   |   |
|                           20 | Customer       | Adjust date, time and quantity of product in shopping bag | Easily make changes to my order on the fly                                                                  |   |   |
|                           21 | Customer       | Easily enter my payment information                       | Check out quickly and with no hassle                                                                        |   |   |
|                           22 | Customer       | Feel that my payment information is processed safely      | Pay with confidence                                                                                         |   |   |
|                           23 | Customer       | View an order confirmation after checkout                 | Check that what I purchased is correct and view details                                                     |   |   |
|                           24 | Customer       | Receive an email confirmation after check out             | Keep for my records                                                                                         |   |   |
|   Admin & store management   |                |                                                           |                                                                                                             |   |   |
|                           25 | Site Owner     | Add a product                                             | Add new experiences to the store                                                                            |   |   |
|                           26 | Site Owner     | Edit/update a product                                     | Change experience prices, descriptions, images etc.                                                         |   |   |
|                           27 | Site Owner     | Delete a product                                          | Remove experiences that are no longer for sale                                                              |   |   |
|                           28 | Site Owner     | Edit/update a review                                      | Review a particular experience                                                                              |   |   |
|                           29 | Site Owner     | Delete a review                                           | Delete a review that may be offensive or against the terms of the site                                      |   |   |




### Project scope

For the project to succeed in accomplishing it's objectives, a clear rule set must be established to keep the project on track. Mostly these objectives and features are tied in with the user stories and their goals. 

- #### Define the project
  - Connect objectives with creative strategies
- #### Project tasks
  - Preparing the build
  - Information Architecture - database design
  - Feature driven development 
- #### Review
  - Get feedback on design ideas and feature list
- #### Build
  - Commence build
  - Continiously review


### Project Structure

This project, where possible makes use of DRY (Dont repeat yourself) principles with the use of OOP classes, functions and Django templating language.
The core static (HTML, CSS) files `Base.html` and `Base.css` include the `main-nav.html` and `mobile-top-header.html` of which, all other HTML pages on the website inherit from with the use of extended block content.
The nature of Django's app components allows functionality to be tagged on in stages, this separation also makes for a cleaner and more readable development process. 

## Database design schema

This project makes use of a number of database tables or 'Models' as they are called in Django.
Django supports various databases, for this project the database chosen while in development was SQLite. When the project was deployed to Heroku the database was migrated and provisioned to PostgreSQL.

#### User model

One of the advantages of using Django is the ability to use 'out of the box' functionality, Django takes care of user authentication with its default configuration `django.contrib.auth.models`.
When setting up the project it is also a good time to create a superuser, this is achieved with the below command line entry and gives access to all site administration.
 - `$ python manage.py createsuperuser --username=joe --email=joe@example.com`

The primary attributes of the default user are:
|  User 'id' |
|------------|
| username   |
| password   |
| email      |
| first_name |
| last_name  |

#### Home app

- Path: /home
- Models: This app does not require a database table.
- Stores the account user's basic details.

#### Experiences app

- Path: /experiences
- Models: `Experiences` and `ExperienceCategory`
- `Experiences` stores the details associated with each experience with foreign keys connecting to other tables.
- `ExperienceCategory` stores the category of the experience.

| Experiences (id)    | PK           |
|---------------------|--------------|
| created_by          | FK(UserProfile)           |
| experience_category | FK(ExperienceCategory)           |
| name                | charfield    |
| description         | textfield    |
| location            | charfield    |
| price               | decimalfield |
| duration            | charfield    |
| age_restricted      | booleanfield |
| language_default    | booleanfield |
| image               | imagefield   |
| rating              | decimalfield |
| hosted_by           | charfield    |

| ExperienceCategory (id) | PK        |
|-------------------------|-----------|
| name                    | charfield |
| friendly_name           | charfield |


#### Bag app

- Path: /bag
- Models: This app does not require a database table. Instead, uses a context processor that stores the bag contents in session.


#### Checkout app

- /checkout
- Models: `Order` and `OrderLineItem`
- `Order` stores the information associated with a particular order.
- `OrderLineItem` stores details of each experience that is added to the order.

| Order (id)      | PK              |
|-----------------|-----------------|
| order_number    | charfield       |
| user_profile    | FK(UserProfile) |
| full_name       | charfield       |
| email           | emailfield      |
| phone_number    | charfield       |
| country         | countryfield   |
| postcode        | charfield       |
| town_or_city    | charfield       |
| street_address1 | charfield       |
| street_address2 | charfield       |
| county          | charfield       |
| date            | datefield       |
| order_total     | decimalfield    |
| grand_total     | decimalfield    |
| original_bag    | textfield       |
| stripe_pid      | charfield       |


| OrderLineItem (id) | PK              |
|--------------------|-----------------|
| order              | FK(Order)       |
| experience         | FK(Experiences) |
| quantity           | integerfield    |
| lineitem_total     | decimalfield    |


#### Help app

- Path: /help
- Models: This app does not require a database table.


#### Host app

- Path: /host
- Models: `PostExperienceView` inherits from `Experiences` table.
- This app modifes the Experiences model with the users created experience via a form.

#### Profiles app

- Path: /profiles
- Models: `UserProfile`
- `UserProfile` stores the users profile details 

| UserProfile (id)        | PK                  |
|-------------------------|---------------------|
| user                    | onetoonefield(User) |
| default_phone_number    | charfield           |
| default_street_address1 | charfield           |
| default_street_address2 | charfield           |
| default_town_or_city    | charfield           |
| default_county          | charfield           |
| default_country         | countryfield        |
| defualt_postcode        | charfield           |


#### Wishlist

- Path: /wishlist
- Models: `Wishlist` and `WishlistItem`

| Wishlist(id) | PK                           |
|--------------|------------------------------|
| user         | oneotonefield(User)          |
| experiences  | manytomanyfield(Experiences) |

| WishlistItem(id) | PK              |
|------------------|-----------------|
| experience       | FK(Experiences) |
| wish             | FK(Wishlist)    |





| HTML                 |   | PEP8       |   | CSS            |   |
|----------------------|---|------------|---|----------------|---|
| Index                | ✔ | See report | ✔ | See W3C report | ✔ |
| Experiences          | ✔ |            |   |                |   |
| Experiences_Detail   | ✔ |            |   |                |   |
| Host_Experience      | ✔ |            |   |                |   |
| Edit_Host_Experience | ✔ |            |   |                |   |
| Terms & Conditions   | ✔ |            |   |                |   |
| Contact              | ✔ |            |   |                |   |
| Wishlist             | ✔ |            |   |                |   |
| Profile              | ✔ |            |   |                |   |
| Bag                  | ✔ |            |   |                |   |