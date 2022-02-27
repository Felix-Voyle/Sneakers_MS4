# Up-Kicks


"Up Kicks" is a sneaker site catering for people looking for rare or limited edition trainers. As well as selling current products they also highlight upcoming releases and give users a place to comment and see other peoples opinons on upcoming and current products."
  

## User stories


### External User’s  Goal

- External user's would be seeking to find and purchase rare, desirable and guaranteed authentic sneakers for a reasonable price. 

 
### Site Owner’s Goal

- The site owners goal is to make an income from selling the commodities listed on the store. 

 
### First Time Visitor Goals
- As a first time visitor I want to instantly know the sites purpose

- As a first time visitor I would like to buy trainers

- As a first time visitor I want to be able view and navigate through the available products

- As a first time visitor I would like to be able to see reviews from previous users of the site 
  
### Returning Visitor Goals
- As a returning  visitor I would like to leave a review about my previous purchase

- As a returning visitor I would like to create an account

- As a returning visitor I would like to see upcoming releases

 
### Frequent Visitor Goals

- As a frequent visitor I would like to see upcoming releases and what
Other users think about them

- As a frequent visitor I would like my details to be stored on my profile for a faster more efficient checkout


  

## Design

---

  

### Colour Scheme
For the colour scheme I went with a main colour theme of #FF875C which is a slightly paler colour of coral. I also used #81000f a deep red colour which compliments the coral nicely and helps it really stand out. For the rest of the site I used whitesmoke and a range of grey to #222 which all go well with the main theme of coral.


### Typography

I used Oswald for headings as it is stylish and attention-grabbing in bold. The general text for the site is Rubik light which is easily readable and I fell compliments the Oswald style well.

  

### Imagery

Imagery for the homepage I used a range of six images. Three were for smaller mobile screens and therefore worked better as vertical images and three were wider horizontal images which work perfectly on larger screens. I used a dark transparent overlay to sit above these so that the callout text and "shop now" button really stood out. I feel these images instantly highlight the purpose of the site and let the user immediately know what the site is offering. 

## Database Schema 

[Databse Schema](media/planning/schema.png)



## Wireframes

---

[Small screens](media/planning/sm_screen.png)

[Medium screens](media/planning/med_screen.png)

[Large screens](media/planning/lrg_screen.png)

### Any updates made to the Wireframes?

  
## Features

---

### Features to implement in the future

-   A market place where users could buy and sell their own trainers.

- Ideally I should be making sure that a user has actually purchased an item before allowing them to review it. I haven't managed to implement this as I ran out of time but think it would make the reviewing system much more accurate given the time.
To do this I would probably link Orderlineitems to the User rather than or as well as UserProfile which would make them more readily available than needing a UserProfile instance.

- To make the site properly functional. I would also need to add a stock system which only lets products show availability if the correct stock is held.

## Technologies used

----

### Languages used

-   Html
-   CSS
-   JavaScript
-   Python

  

### Frameworks, Libraries & Programs Used

-   Bootstrap
-   Font Awesome
-   Django
-   JQUERY

  

**## Testing**

---

  

### Testing User Stories from User Experience (UX) Section

  

#### First Time Visitor Goals
- As a first time visitor I want to instantly know the sites purpose
1. On visiting the site a first time visitor is immediately presented with carousel images highlighting exactly what the site offers and a callout encouraging them to "shop now"

- As a first time visitor I would like to buy trainers
1. As a first time visitor the shop is easily accessible through a hamburger menu on smaller devices or via a navigation menu on larger screens. Navigating through the shop is easy and user freindly.
1. From adding an item to the bag which gives the user a notification to getting to the checkout and finally purchasing the product is all easily done and a clear path is given to the customer.

- As a first time visitor I want to be able view and navigate through the available products
1. As a first time visitor products ar easily accessible either from the hamburger or main nav menus depending on screen size.
1. Products can be easily ordered by price, rating or specific brand.
1. A search bar is accessible on both mobile and larger screens to allow the user to search more specifically to meet their individual needs.

- As a first time visitor I would like to be able to see reviews from previous users of the site
1. Reviews are available for each product. Each registered can only leave a review once on any one product and it is a simple 5 star system in terms of rating. 

  

#### Returning visitor Goals
- As a returning  visitor I would like to leave a review about my previous purchase
1. Reviewing a product is easy and clear. Each registered user can leave one review per product. This could however be improved further by only letting customers who have purchased the item to actually review it. 

- As a returning visitor I would like to create an account
1. Account creation is easy via the hamburger menu on smaller screens or on the main nav bar on larger screens. 

- As a returning visitor I would like to see upcoming releases
1. Upcoming releases are listed and a user can easily navigate to see them. Each upcoming product card clearly shows a release date and generates a countdown timer to clearly highlight how long it is until the release.

  

#### Frequent Vistor Goals
- As a frequent visitor I would like to see upcoming releases and what
Other users think about them

- As a frequent visitor I would like my details to be stored on my profile for a faster more efficient checkout
  

### Further Testing

  

## Deployment

I deployed this site on heroku through github, below are the steps that i took;

### Github 
The project was deployed to Heroku using the following steps;
1. Logged into my github accound and created a new workspace
1. Using the Code Institute template i named my new project and created the repository
1. using the method "pip3 freeze > requirements.txt" in the terminal you will create a requirements text file which heroku will need to deploy successfully"
1. Before being able to deploy the app an initial commit must be made, see below example
1. ```
   cd myapp
   git init
   Initialized empty Git repository in .git/
    git add .
    git commit -m "My first commit"
    Created initial commit 5df2d09: My first commit
    44 files changed, 8393 insertions(+), 0 deletions(-)
   create mode 100644 README
   create mode 100644 Procfile
   create mode 100644 app/controllers/source_file
1. Any changes then have to be pushed to Github before Heroku can display the site in it's current state.

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
1. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
1. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
1. Under the repository name, click "Clone or download".
1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
1. Open Git Bash
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type git clone, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

### Heroku
1. Once logged into Heroku click 'New' then 'Create New app.'
1. Inside the settings you need to 'reveal config vars' and update these variables to match any which you have stored locally. This information needs to remain updated with any new sensitive information you are keeping hidden from the front end.
1. You are given three deployment methods. I choose to use the second option which was through Github (you will need to connect your heroku to your personal github).
1. From here it is just a case of finding the repository you wish to deploy and selecting the correct branch. 

  

## Credits

---

  

### Code

  

### Content

  

### Media

- All images were free to use under the "Unsplash license" and sourced from <https://unsplash.com/s/photos/sneakers>
  

### Acknowledgements
- All of the course material provided allowed me to create this site. Specifically the Boutique Ado mini project.

- My mentor Narender who helped with any outstanding queries I had. 
