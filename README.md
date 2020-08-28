
# Fourth Milestone Project #

[Skydive Göteborg](https://goteborg-skydive.herokuapp.com/)
This project was made for the Fourth Milestone Project for Code Institute.
The objective is to build a full-stack site for the purpose to purchase items and a service and provide authentication mechanism to buy such things.

As such I have created a website for purchasing tandem skydives and film packages.

[Skydive Göteborg Old Website](http://tandemhopp.se//) is a club that runs on the edge of Göteborg and provides a skydiving experience. At the moment, their website is outdated and needs a fresh look.
As such, the website needs to look new, refreshing and sells the experience of the skydive as non threathing and an experience the customer wants to enjoy. Not only the customer can purchase a skydive, but also buy film packages to re-live the experience.


## UX ##
Skydive Göteborg is the only facility in Göteborg that offers the tandem experience. Their audience is anyone, but commonly its a gift to someone else for a special occasion (birthdays, bucks and hen parties). While skydiving is sometimes referred as an extreme sport, the website wants to show the surreal beauty of the experience.
As such the website has been built for the following ideals in mind.

- The website should have a fresh modern look.
- Should explain what skydiving is.
- Give a summary on what you can expect on your day.
- Show case a film package could look like.
- Explain the difference of the film packages.
- Customer can buy the experience for another person. 

The website achieves these goals with a simple look and lets the photos to do most of the talking. It needs to sell the experience and you want to give this a go!

### Vistor to the site ###
Goals for the customer to experience while visiting the site are:
    - Admire the surreal opportunity to experience something man is not meant to do.
    - The site should make the customer safe. Explains in detail on what happens on the day.
    - Shows what the customer will experience with a example video.
    - Be encouraged to buy a film package to re-live the experience at a later date.
    - To purchase a skydive package.

### Developer Goals for the company ###
As the developer for the site, my goals are to make the site professional and help Skydive Göteborg sell the tandem packages. As such I have:
    - The site is easy to navigate.
    - Allowing the experience to be the full focus of the site.
    - Explaning any details that the customer would want to know. 
    - An easy email service to ask questions.
    - Ensuring payments are made correctly.


## Features ##
### Existing Features ### 
1. NavBar:
    1. Navbar should be not over powering the main page, but blends nicely into the page. The navbar colour is off from the main page which showcase the different areas while not making it to obvious.
    1. The Navbar titles are relevant for the sub-heading. All titles are obvious to where the links will take you. 
    1. The Navbar is responsive for different views.
1. Heading:
    1. The heading image, gives that sense of wonder. It clearly shows what the user is in for. A surreal experience!
    1. The company name is clear without destroying the wanting effect of the image.
    1. As the main purpose of the site, is to sell skydive packages. The Buy button is available at any point.    
1. Main Page:
    1. The main page background colour is a very light blue which helps it to be separted from the NavBar.
    1. The main page details explain what tandem skydiving is which is supported by a short film of what the customer is in for.
    1. A quick return to top button is hiden until the page low enough, to give a good user experience to the page. 
1. Your Day:
    1. Your day page should explain in more details what the customer should expect when they purchase a package.
    1. The images are to entice the customer. First image is to show case our friendly staff and the second is to make the customer go "wow!"
    1. The information is relavent to what the customer is to expect. 
        - Who can jump?
        - What happens with the weather?
        - Can family and friends come along to the airport?
        - How heigh does the plane go and how long does it take?
        - What happens if you buy a film package? 
1. Custom your package:
    1. As the intended jumper could be different from the customer, the 'customize your package' page should feel like the package is for that jumper.
    1. As the base sevice is the tandem jump, addons are selected via the film package selection. Instead of having 4 different options, there is a base product and then you purchase film products as well. This allows skydive göteborg to be easily change the indivual price of each product. 
        - For example: If the price of the tandem skydive needs to increase, this can be done once and easily. If the products was tandem and a film product (a package), this would need to be done on every package.
    1. A discription of each different film packages and their cost and clearly labeled.
    1. The quick use of 'another jumper' allows the individual custom packages added to the 'checkout' without having to return from the checkout.  
1. Contact us:   
    1. A quick explaination on what this page should do. Allow the user to easily contact skydive göteborg with any questions.
    1. By filling in the form, the user will also recieve an email, telling the user that we have recieved their question and will responed in due time.
    1. Information about skydive göteborg with a link to google maps and their telephone.   
1. My Accounts:
    1. User can register to the site with their email, and password.
    1. Once logged in, user can see their previous orders. 
    1. User can easily change their details and also their details will be passed on to for fill insurance for the skydive jump, allowing quicker time at the drop zone.
1. Checkout:
    1. As the jumper could be different from the customer, the payment form can be customized including the billing details.
    1. A finally summary is shown and allows the users to either remove a package or add a package.
    1. A sub-cost per jumper experience is shown as well as an over all cost.
    1. Once the payment has been successfully recieved from stripe, an email will be sent with the recipt for the purchase. 


## Features Left to Implement ##
1. Booking service:
    - Once the customer has purchased their package. The next step is to book a date and time. As the plane has limited seats and the company changes location half way through summer. I would need to create a large booking service. As such, I had limited time and will be implemented at a later date.
    - A summary of bookings per day for for required staff.
    - Each jumper gets their own ticket receipt.
    - A jumper could change their bookings using their loggin or id from their purchase
1. Live google maps:
    - While the page has a image and a link to google map. I would like to implement a google search directly into the website.
1. Facebook loggin:
    - This would help advertise the experience and allow user feedback on both Facebook and the website.    
1. Extra Payment methods:
    - Sweden was another payment (Swish) option which is very common and widely used. I would like to add this payment plan when the site goes live for Skydive Göteborg.    



## Technologies Used ##
- [Python](https://www.python.org/)
    - Majority of the code is written using Python. Python is a great programming language that allows the front end and backend code to operate.
- [Django](https://www.djangoproject.com/)
    - Django was used as the framework. This allows the developer to focus on writing your app without needing to reinvent the wheel. It’s free and open source. 
    Some of the extra Django extensions used:
        - django-allauth
        - django-bootstrap4
        - django-countries
        - django-crispy-forms
        - django-storages
- [Stripe](https://stripe.com/en-gb-se) 
    - Stripe’s products allow online and in-person retailers, subscriptions businesses, software platforms and marketplaces. This allows the developer not to reinvent a great product, but easily intergrates into your project. 
- [Git](https://github.com/)   
    - Github has been used to save code not locally and help development of the site.
- [Heroku](https://id.heroku.com/login) 
    - Heroku is where the project is live to the world. Also stores secret variables to insure the site is safe.    
- [Bootstrap](https://getbootstrap.com/)
    - Bootstrap has great features and extensive prebuilt components. This allows the overall look to feel united and responsive. 
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Boto3 is used to configure AWS S3
- [AWS S3](https://aws.amazon.com/free/storage/s3/?trk=ps_a134p000003yHieAAE&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_ND&sc_publisher=Google&sc_category=Storage&sc_country=ND&sc_geo=EMEA&sc_outcome=acq&sc_detail=aws%20s3&sc_content=S3_e&sc_segment=444204369788&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|Product|ND|EN|Text&s_kwcid=AL!4422!3!444204369788!e!!g!!aws%20s3&ef_id=Cj0KCQjws536BRDTARIsANeUZ5-YwWFTEtUuvIDnoy-RZjHDoVT4Ofu3WB4zzzIg_0f9NN6bf7jL9z8aAlQGEALw_wcB:G:s&s_kwcid=AL!4422!3!444204369788!e!!g!!aws%20s3)
    - S3 is used to store the pictures and video used on this project.
- [postgresql](https://www.postgresql.org/)
    - A database from Heroku
- [JQuery](https://jquery.com/)
    - To help with HTML document traversal and manipulation, event handling.
- [Fontawesome](https://fontawesome.com/)
    - Has a database of icons, some which were used in this project


## Testing ##

### [Link to test stories](https://github.com/brendanoshea84/tandem_skydive/blob/master/static/TEST.md) ###
Here you will find the manual testing of the site


## Deployment ##
### Local ###
1. First insure you IDE (example: VSCode) is up to date and has python3, PIP and Git ready to use.
1. Download the zip version of [tandom_skydive](https://github.com/brendanoshea84/tandem_skydive).
1. Use GIT to clone the project by using
```
git clone https://github.com/brendanoshea84/tandem_skydive  
```
1. A virtual environment is needed to see the project locally. I used python's virtual environment from VSCode.
```
python -m .venv venv 
```
1. To run the virtual environment
```
python -m .venv venv 
```
1. To create quick short cuts for loading venv and running the project. Go into your bash settings by typing into your terminal
```
nano ~/.bashrc 
```
Then copy these two lines into the top of the bash
```
alias run="python3 manage.py runserver 4000"
alias venv="source venv/bin/activate" 
```
When you want to enter you virtual environment type: venv or run the project: run
1. To install all the requirements
```
pip -r requirements.txt 
```
1. As there is a fair bit of secret variables, I recommend creating a env.py at the base level of the project. Open the file, and at the top insert 'import os'.
Then:
```
os.environ.setdefault('SECRET_KEY', '<enter secret key for the django project>')
os.environ.setdefault('EMAIL_HOST_USER', '<enter a email address>')
os.environ.setdefault('EMAIL_HOST_PASSWORD', '<enter a email password>')
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<enter stripe public key>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<enter stripe secret key>')
os.environ.setdefault('STRIPE_WH_SECRET', '<enter webhook secret key>')
os.environ.setdefault('DATABASE_URL', '<enter postgres address>')
```
1. Now to migrate the database:
```
python manage.py migrate 
```
1. Django needs a superuser to access the admin panel and database
```
python manage.py createsuperuser
```
1. You need to set Allowed Host in settings 
```
ALLOWED_HOSTS = ['goteborg-skydive.herokuapp.com', '127.0.0.1']
```

1. The video will not work without the internet, if you wish to view the video locally. Go to home/templates/index.html line 20 and change
```
<source src="https://goteborg-skydive.s3.eu-north-1.amazonaws.com/media/film/tandem-example.mp4" type="video/mp4" autoplay= "true">
```
to 
```
<source src="/media/film/tandem-example.mp4" type="video/mp4">
```

### Deploy to Heroku ###
1. This project has already got a requirements.txt, if you need to create one, type this command into your terminal:
```
pip freeze > requirements.txt
```
1. The Procfile has also been created, if you need to create one:
```
echo web: python app.py > Procfile
```
1. Insure you have the up to date version of the project if you created the Procfile and/or requirements.txt by comminting them to GITHUB
1. Create a new app on heroku, give it a unique name and choose a location close to you.
1. Select "Heroku Git" as the deployment method and follow the instuctions to install the Heroku CLI tool.
1. Go to Resources and under add-ons, search for postgres. Select Heroku Postgres from the dropdown and add it.
1. Then go to your settings in heroku and reveal config vars and add the following:
```
('SECRET_KEY', '<enter secret key for the django project>')
('EMAIL_HOST_USER', '<enter a email address>')
('EMAIL_HOST_PASSWORD', '<enter a email password>')
('STRIPE_PUBLIC_KEY', '<enter stripe public key>')
('STRIPE_SECRET_KEY', '<enter stripe secret key>')
('STRIPE_WH_SECRET', '<enter webhook secret key>')
('DATABASE_URL', '<enter postgres address>')
```
Once the variables have been entered, restart the dynos or git push the project.







Photos
Wide screen- https://www.skydivegb.com/charity



django-alluth
https://django-allauth.readthedocs.io/en/latest/installation.html
copy to seetings from documentation