# ConorCreates - Milestone Project 4 - Full Stack Frameworks

[![Build Status](https://travis-ci.org/walshyc/conor-creates.svg?branch=master)](https://travis-ci.org/walshyc/conor-creates)

ConorCreates is a fictional ecommerce store which allows a grapgic designer to sell custom graphics to clients. The designer can add graphic design services to the backend, which once added cvan be purchased by the end user. The user has to register for an account to purchase a graphic design product. Once a user has purchased a graphic, the order is added to their profile. The graphic designer can then uplaod the completed graphic to the user's profile for the user to download. Finally once the user downlaods the graphic they can leave a review of their thoughts on the graphic, which gets added to the front end of the website.
 
## UX
 
The website is for users who require a graphic for their business, event, wedding etc. to purchase the graphic in an quick and easy way. When the user is purchasing a graphic they can add the colours that they wish the designer to use, along with a short brief to explain the finer details of what is required. The website also allows the graphic designer to showcase his previous work, customer reviews adn to sell his services online.

### Wireframes

I produced some wireframes to help plan the project. Some of the layout changed as the project developed but the main structure remained the same.

* Desktop
    * [Homepage](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+Homepage.png)
    * [Register](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+Register.png)
    * [Login](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+User+Login.png)
    * [All Services](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+All+Services.png)
    * [Single-Service](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+Single+Service.png)
    * [About/Contact](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+About+%26+Contact.png)
    * [Profile](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/desktop/Desktop+-+Profile.png)

* Mobile
    * [Homepage](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Homepage.png)
    * [Register](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Register.png)
    * [Login](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Login.png)
    * [All Services](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Services.png)
    * [Single-Service](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Single+Service.png)
    * [About/Contact](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+About.png)
    * [Profile](https://conor-creates.s3-eu-west-1.amazonaws.com/static/wireframes/mobile/Mobile+-+Profile.png)


### User Stories

- As a graphic designer, I can market skills online and help grow my business.
- As a graphic designer, I can easily manage all the orders that I have by viewing the profile page.
- As a graphic designer, I can approve reviews left for my work, for the general public to view on my website.
- As a business owner, I require a facebook advert for an upcoming sale, I can purchase a custom made facebook advert on ConorCreates and download it for use online.
- As a owner of a new startup, I require a new logo for my business, I can give the designer colors and a brief fro them to create a brand logo for me.
- As a potential customer I can browse examples of previous work by the graphic designer. I also can view reviews from past customers.

## Features

- Services - The graphic desginer can add servies to sell to the website through the administration panel.
- E-Commerce - The end user can purchase a graphic design service by filling out the order form on a single service page.
- Contact - The end user can learn more about the hsitory of the graphic designer on the contact page. They can also fill out a form to send a messaeg to the graphic designer.
- Previous Work - The graphic designer can upload images of previous work to be displayed on the website.
- Reviews - The end user can leave reviews for the services they have purchased. The graphic designer has to approve the review, which will appear on the website once approved. 

 
### Existing Features
- Services - allows the grpahic designer to manage what services they display on their website, by adding or deleting services from the Services table in the administration section of the website.
- Purchase a Service - allows businesses to purchase marketing graphics, by using the order form to give the designer a description of what they require. The payments are handled by Stripe.
- Reviews - allows end users to review the services that they have purchased by filling out the review form, which appears as a link from their profile page once a grpahic has been uploaded.
- Order Management - allows the graphic designer to manage all the orders they have placed with them by viewing their profile when logged in as the administrator they can view a list of all their orders.
- Contact - allows the end user to send an email to the graphic designer with any queries that they may have, by filling out the contact form on the About page.
- Image Slideshow - allows for the graphic designer to upload images of rpevious work to he website to be shown on the homepage and on a service page.

### Features Left to Implement
- HTML Email Templates
- Email notification when a graphic is uplaoded to a customers account

## Technologies Used

- [Django 1.11.17](https://www.djangoproject.com/)
    - I used the python web framework Django to build the website
- [Bootstrap 4.3.1](https://getbootstrap.com/)
    - Bootstrap was used to for stylign and general layout of the website.
- [Flatly Bootswatch Theme](https://bootswatch.com/flatly/)
    - The Flatly theme was used to further enhance the look of the Bootstrap framework throught the website.
- [Font Awesome](https://fontawesome.com/)
    - Font Awesome icons are used to add to the visual aspect of the website
- [Stripe](https://stripe.com/)
    - I used Stripe to handle and process the payments on the website.
- [Slick](https://kenwheeler.github.io/slick/)
    - Slick was used for the image slideshows that appear on the homepage and on each service page.
- [jQuery 3.3.1](https://jquery.com/)
    - jQuery was used in to allow Bootstrap and Slick work on the website.
- [PostgresSQL](https://www.postgresql.org/)
    - I used a Postgres database on the Heroku platform to store all the information used on the website.
- [Amazon Web Services - S3](https://aws.amazon.com/s3/)
    - I used an S3 bucket from Amazon Web Services to store all the static files such as images, CSS and Javascript in the cloud.


## Testing

I used Travis-CI for automated testing where applicable in the website. I created testing files in each app and wrote test to test the forms, models and views. I ran the following command in the command line to check these tests:

```
python3 manage.py test
```

When running the automated tests I had to change the database url back to the sqlite3 database that I had been running locally as the tests would not run on the Postgres database on Heroku.

I also performed manual testing on the website on sections that I hadn't covered in the automated testing. I created a number of test users in addition to the admin superuser. The test usernames are as follows, with them all having a password of testing1:

claire
conor
cormac
gerry
john
kevin
laura
tom

The superuser has a username of admin and a password of testing1 also.

I added 6 services to the website for testing purposes. Within each servicve I then placed a minimum of 4 orders across the differernt users I had created. I then uplaoded fake graphics to some of the orders and left reviews for these graphics. I checked that none of the reviews showed until I had logged in as an administrator and approved the reviews. I also checked that the order confirmation emails were sent to both the user and the administrator as expected, which they did. I tested that the review button on an order only dsiplays after the graphic has been uploaded.

When building the website I used the payment processer Strip in test mode. This allowed me to test that the poayments worked. I was able to use the Stripe test cards as outlined in the Stripe documentation to perform test transcations. I could then login to my Stripe dashboard to check if the payents registered with Stripe which they did.

I also tested that when I logged in as the superuser the profile page showed all orders and not just the orders of one user as is the case for a normal user. 



## Deployment

I build the websaite locally initially and then used Heroku to deploy the website to the internet. To veiw the website I would run the runserver command in the commad line to view the webiste locally:

```
python manage.py runserver
```
When building the website I used the enviroment variables on my local PC to store certain infgormation such as email password and Stripe secret keys. All these variables were then added to the Config Variable section of the settinsg in my Herroku app to allow the variables to be stored securly. The Postgres database URL was stored in an config variable also. I used this code in my settings.py file to default back to the sqlite3 database if the Postgres database coudln't be accessed:

```python
if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Database URL not found. Using SQLite instead")
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
     }
```

I used Git and Github fro version control on this project. I committed and pushed any changes to github regulary by using the Source Control feature on the code editior VSCode which I sued for this project. I have just over 100 commits on this project so far.

If you wish to clone this repository and run it locally, wou can run the following command in your command line:

```
$ git clone https://github.com/walshyc/conor-creates.git
```

You will then need to install all the Python libraries by running:
```
pip -r install requirements.txt
```

## Credits

### Content
- I used [Canva](https://canva.com/) to retreive most of the graphic images for this project.
- I used [Pexels](pexels.com) for some of the background images
- I borowsed some Graphic design websites to help create the text descripotion for the services currently on the database.
- I got the .gitignore file from [here](https://github.com/github/gitignore/blob/master/Python.gitignore)


### Acknowledgements

- The Code Institute lectures were very helpful with giving me the foundations in Django to complete this project. The e-commerce and user apps in this project are inspired from these lectures.
- I consulted with StackOverflow and teh Code Institute slack channel with any issues I had in getting some of the code to work. Both sources were very helpful.
- I watched some videos on YouTube from Corey Schafer and Traversy Media after I had finished the Code Institute lectures
