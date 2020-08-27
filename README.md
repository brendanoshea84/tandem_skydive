
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










Photos
Wide screen- https://www.skydivegb.com/charity



django-alluth
https://django-allauth.readthedocs.io/en/latest/installation.html
copy to seetings from documentation