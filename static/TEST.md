## Testing for Skydive Göteborg ##

This project has a fair bit of pages and so I will break it down into their major componets.

### Header ###
#### Navbar ####
1. All links has been tested so that they go to the correct links.
    - Logo link goes to the main page.
    - All dropdown Nav looks correct and goes to the right link.
    - My account only shows Register and login if the user is not logged in.
    - If logged in, the user can see their profile, checkout (if the user has saved their details but has left before payment, the details are saved) and log out.
    - The checkout, if the bag is empty redirects to the package page so that the user can fill their bag. If the user has something in their bag, they can see the checkout page.
    - Nav bar is responsive and will change depending on their screen size. Tested with chrome on desktop, as well as ipad and mobile device.

#### Main header #### 
1. The main head is seen on all device sizes 
    - The image is responsive and changes height depending on size device.
    - The logo of 'Skydive Göteborg' changes size depending on size device.
    - The 'Buy' button changes size and is at appropriate location on different devices.

#### Other features avaible on most pages ####
1. To insure the project has a nice user experience, extra features are avaible on most pages. Such as:
    - If the page is too long, a back to top button is avaible when scrolling.
    - Toast with error, info or success messages will pop up to let the user know what their doing. For example, add to bag.
    - Modal with extra information will pop up from links. This will insure the user does not lose track on which page they are own and provide more information without search webpages. 


#### Main Page / Whats tandom skydive? ####   
1. The main page has an introduction and a video on tandom skydiving.
    ##### Video #####
    - The video automatically starts when the page is loaded.
    - Sound is turned off.
    - The video changes position and size depending on device.
    ##### ERROR #####
    - As the video is linked to AWS S3, if the developer is running the site locally and does not have internet connection, the video wont work. Please see the README.md devployment is see how to change the lines in code to run the video locally.
    ##### Introduction #####
    - Text is correct size for all devices

#### Your day ####
1. This page gives more information about the skydive experience and what to expect.
    - The page is responsive on different device sizes.
    - Images will change position as well as size depending on device.
    - Top button works on scroll.

#### Customize your package ####   
1. This page is the add to cart page, where the user can enter details of the jumper and then custom their skydive experience.
    - The page is responsive with the text being muted to add effect to the page.
    - The form needs to be filled in to allow the user to add to bag. If the form is incorrect, a warning on the form shows the user where to fill in the missing details. If the user enters the wrong format in the form, a warning will pop up.
    - Cost of the tandem jump is clear and will change if the admin decides to change the price.
    - Film packages have their details plus the extra cost to the skydive if choosen.
    - Film packages will update if the admin decides to change cost, label and details. Extra packages could be entered at a later date and will be update here too.
    - Drop down menu shows all the options to customize the film packages.
    - Add another jumper will add to the bag (if all details have been entered) and redirect back to this page.
    - Go to checkout will add to the bag (if all details have been entered) and will procced to the checkout page.
    - The toast will show a link to the checkout, if the user does not want to add more jumpers but has clicked the wrong button.
    ##### ERROR #####
    - The phone number is entered into the form as a char model, this means the user can enter anything. At the moment, the phone number isn't that important but only would be used to inform the jumper that the jump has been cancelled due to weather. If that is the case, skydive göteborg would send a mass email as they would have many jumpers in one day. The jumper would have to sign insurance form at the dropzone, so if the number is incorrect, they would need to change it there.

#### Contact Us ####
1. This page is to show the user details about the club and allow the user to email skydive göteborg a question.
    - Link to google maps opens in a extra page. This allows the user not to lose the website. The location on google maps is correct.
    - The form has to be filled in to send a question. 
    - The question form has been tested and the email is sent to the user as well as an admin email address.

#### My account ####  
##### Not logged in ##### 
1. If the user is not logged in, only two options are avaible. 
    1. Register:
        - User has to enter a valid email address.
        - Password needs to be entered twice, to insure the user knows the password and not a mistake.
        - Password cant be too common.
        - An email is sent to the user to insure that the customer is real.
    1. Sign in:
        - Form needs to be filled in correctly and check against the user database to insure the user has an account.
        - Password needs to match the database user password.
        - If the user has forgotten their password, the page is directed to a password forget page. If the email address is valid, an email has been sent to the user email address.
##### logged in #####   
1. If the user is logged in, they can see their profile page, checkout (if they have not paid for their order but been directed away from the website) and logout
    1. My Profile:
        - Their details are presented in a form which can be updated if needed. If updated, the page is redirected back to your profile page.
        - If the user has bought anything here in the past, a previous order list is show. By cliking on the order number, the page is directed to a page to show what they have purchased. 
        - If the user has not purchased anything, the previous order list shows that you have not purchased anything at the moment.
    1. Checkout:
        - If the user has added a jumper then left the website, their order will be put on hold. All information is correct when testing the site by adding a jumper, leaving the site, then returning and logging back in. This is directed to the checkout page.
    1. Log out:
        - This is tested by logging out and seeing that the navbar has changed its options, meaning the user has indeed logged out.    

#### Checkout #### 
1. This is the user final chance to change anything in their bag before paying for the order. I will break this down into three stages.
    ##### Bag empty #####
    - If their is nothing inside the bag, the checkout button is redirected to the package page. The user could have pressed the wrong button and as the checkout is empty, the user will have a bad experience on the page. By redirecting the user to the the package page, it directs the user into the right format of purchasing the skydive experience.
    - If the user has a jumper in their bag, goes to the checkout, then removes the jumper. The bag is empty and the page is redirected to the package page. This has been tested on the site.
    ##### Before Payment #####
    - If the user is logged in, their details should be entered into the form else the user will enter their details. If the form has not been correct filled in, a warning will appear before the payment has been sent.
    - The jumper package is shown with all cost and a grand total.
    - Jumpers can be removed and added befor the payments with all totals updated.
    - Card information has to be correct and tested befor payment is sent.
    - You can test this by entering the card number as 4242 4242 4242 4242 then add the expire date and zip number.
    ##### After Payment #####
    - The page takes time to load the detail and send to stripe, as such a loading screen is shown to show the user that something is happening. Loading screen works and spins.
    - If the payment is correct the page is loaded to a checkout success page with the new order number, order date and time, and a quick sumary on what has been purchased.
    - The go back button takes the user to the start of the purchase cycle if they want to buy another skydive package.
    - Webhooks from stripe are being used to insure that the payment has been correct before giving the order number as well as an email of their purchase.
    - In settings, the payment is set as swedish krona as the company works in sweden. 
    

#### Interesting Errors found during construction ####  
##### Post/Redirect/Get #####
[Wikipedia info of the error](https://en.wikipedia.org/wiki/Post/Redirect/Get)
    While constructing this website, an error I came across was Post/Redirect/Get. This happened when if you were on the checkout page and refresh that page, the bag would enter another jumper. After doing some research, I found that my python code was allowing this. This was because I wasn't using the redirects correctly.

##### Add another jumper and go to checkout buttons #####
    On the package page, while this works I believe with more time I could come up with a different solution.
    As the user I want to enter my details, click a button and go straight to the checkout. But if you clicked another jumper button, then change your mind. The go to checkout still wants you to enter your details as it wants to add another jumper to the bag. The solution was to have the toast, give you the link to go to checkout or press the shopping bag. As skydiving is so expensive, I belive people would really think about paying for the experience, as such while this scenario could happen in real life, I believe it would be a small percantage.

##### Video on main page #####  
    While developing this site, I had the video as a local file. But when transferring all the static files to AWS S3 and running the page live, the video src was not correct. I changed the src to S3 and the video works live and well. While developing the site, I had some internet problems. I noticed that the video with out the internet and working local, the video did not work. As this would only occure when the developer is with out the internet, I did not waste to much time looking into different src depending on the internet, but I would like to research this further.

##### Adding Jumper/ remove jumper from bag #####  
    Adding to a nested dictionay is quite easy. What is hard is when you need to delete apart of that dictionary. First, I gave them an id, which worked well in the beginning. So I had a loop to find the next id number, add 1 and thats the new id for the next jumper.
    So for example, I have three jumper in the bag:
    bag = { 0:{jumper 1},
            1:{jumper 2},
            2:{jumper 3},
            }
    And I delete the second jumper. 
    bag = { 0:{jumper 1},
            2:{jumper 3},
            }
    Using that loop, the next jumper would be 1:{jumper4}. If that was entered, this would replace the third jumper as the index would be 1.     
    bag = { 0:{jumper 1},
            1:{jumper 4},
            }   
    To fix this, I made a loop to find the highest id, then add 1. This would make the bag:
    bag = { 0:{jumper 1},
            2:{jumper 3},
            3:{jumper 4},
            }     
    Looking back its a simple solution, but at the time and noticing that jumpers were being replaced, it was a head scratcher. But I learnt allot about nest dictionary.