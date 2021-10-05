# DaMovies

<img src="assets/images/readme-img/responsive.png" alt="about section" width="70%"/> !!!

[Link to the live site on Heroku](http://milestone-project-3-damovies.herokuapp.com/)

#### Overview

This is "DaMovie", a website dedicated to cinema lovers who want to share opinions on their favoirite movies and discover new ones! Once they have created their account, users can add, comment and rate movies in the catalogue.

---

### Table of Contents

- [UX](#ux)
    - [User Stories](#user-stories)
    - [Strategy](#A-strategy)
    - [Scope](#B-scope)
    - [Structure](#C-structure)
    - [Skeleton](#D-skeleton)
    - [Surface](#E-surface)
- [Features](#Features)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Integration](#integration)
    - [Workspace, version control and Repository storage](#workspace-version-control-and-repository-storage)
- [Resources](#resources)
    - [Sources of knowledge](#sources-of-knowledge)
    - [Other resources](#other-resources)
- [Code Validation](#code-validation)
    - [Testing](#testing)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
- [GitHub Pages](#github-pages)
    - [Deployment](#deploying-the-project-on-github-pages)
    - [Forking](#forking-the-github-repository)
    - [Cloning](#making-a-local-clone-of-the-github-repository)
- [Credits](#credits)
    - [Media](#media)
    - [Content](#content)
    - [Code](#code)
    - [Acknowledgement](#acknowledgement)

--- 

## UX

The service is aimed at an english-speaking audience that wants to watch new movies and share their thoughts on movies they've seen before.

#### User Stories 

- As a first time visitor
    - I want to easily understand the main purpose of the site
    - I want the site navigation to be intutive and user friendly
    - I want to easily access the movies' catalogue
    - I want to create an account to become part of the website community 
    - I want to see information about movies in the catalogue (i.e. director, year of release)
    - I want to see the audience rating of movies in the catalogue
    - I want to add my rating
    - I want to see other users comments on movies in the catalogue
    - I want to add my own comment
    - I want to add movies that I like to the catalogue 
    - I want to be able to edit information of the movies I have uploaded in the catalogue
    - I want to be able to delete movies I have uploaded

- As a returning and/or frequent visitor
    - I want to easily sign-in in to the website
    - When I have questions about the website, I want to find information about the website owner/administrator  

#### Strategy 

##### Project Goals:
- To provide users with a web application where to share and discuss movies (via CRUD operations):
    - Create: By adding movies to the catalogue
    - Read: By searching and filtering movies in the catalogue
    - Update: By editing, commenting and rating existing movies in the catalogue
    - Delete: By deleting movies uploaded in the catalogue
- To increase traffic and expand the website community
- Developing a partnership with streaming services as a future goal 

##### Customer Goals:
- To find new movies to watch
- To see other users' reviews about the movies from the catalogue
- To rate and comment movies I have already watched
- To contribute to the website community by adding new movies to the catalogue
- To navigate the website smoothly and intuitively.

#### Skeleton

- [Wireframes](assets/docs/wireframes.pdf)
- Interactive navbar (fixed on mobile browsers) with 4 links + logo.
- Home, About, Locations (map) and Contact sections.
- Footer with social media links and copyright message.

#### Design  

##### Colors 

The color scheme for the website consist of three main colors: black, gold and white. Black is used as based color for the website, gold for texts, buttons and decorations, and white for texts and icons. Grey shades are also used to differentiate certain elements from the black background (i.e. navbar, forms and buttons). 

Combining black and gold seemed like the right choice to create a classy cinematic feel for the website. Using white creates contrast with the black background and keeps text as readable as possible.


- ![#c7bc65](https://via.placeholder.com/15/c7bc65/000000?text=+) `#c7bc65`
- ![#fffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`
- ![#00000](https://via.placeholder.com/15/00000/000000?text=+) `#000000`
- ![#131313](https://via.placeholder.com/15/131313/000000?text=+) `#131313`
- ![#1a1a1a](https://via.placeholder.com/15/1a1a1a/000000?text=+) `#1a1a1a`

##### Typography

- "Monoton" for: Logo, with the intention of giving it a cinematic feel.
- "Roboto" for: for the rest of the text. This is the default font when using the Materialize library. The choice of using it was due to the fact that is simple, clean and gives the website a professional look.
- "Sans-serif" as fall-back font for every text.


##### images

- On the home page, images were chosen to give the user the feeling of being at the movies as well as add a retro look to the website. 

--- 

## Features 

- Designed with HTML5, CSS3, JavaScript + libraries (Materialize, jQuery).

    <img src="assets/images/readme-img/homepage.png" alt="homepage" width="70%"/>

- **General features (apply to all pages except 404)**:
    - Fixed navbar on top of the page with links to:
        - Home, catalogue (for all users)
        - Sign-in/register (for not signed-in users)
        - Add movies, Profile, sign-out (for signed-in users)
        - Manage generes (for website administrator only)
    - Footer with link to home page and Github account
    - Responsive site on all devices
    - Collapsible navbar, with 'hamburger button', under 992px breakpoint 

- **Home page**:
    - Information about the website and its purpose.
    - Links to 'catalogue' and 'log-in/register' pages for users who have not signed-in yet.
    - Links to 'catalogue' and 'add movie' pages for users who have already signed-in. 
    <br><br>
    
    <img src="assets/images/readme-img/about.png" alt="about section" width="70%"/>

- **'Catalogue' page**:
    - Search bar to look for specific movies (filtered by title or director's name).
    - List of movies with movie cover image, movie title and icon to reveal specific movie information (for all users)
        - Edit and Delete buttons (visible for users who posted the movie and administrator)
    - Movie info-card (by clicking on movie reveal icon), with:         
        - Specific information about the movie (i.e. director, plot, etc.)
        - Average rating by users on a scale from 1 to 5
        - Form with radio buttons to add rating (only for sign-in users)
        - List of users' comments
        - Text area to add comment (only for sign-in users)
    - Flash messages sections (Informs the user whether his/her actions were successfully completed, i.e. upload a movie, edit a movie, add a comment, etc.)
    <br><br>

    <img src="assets/images/readme-img/locationsd.png" alt="location section 1" width="70%"/>

- **'Add Movies' page (only for signed-in users)**:
    - Form where the user can provide information about the movie they want to upload:
        - Genre
        - Title
        - Director
        - Year
        - Plot 
        - Movie cover image (optional)
    - Submit button (which also redirects the user to the movie catalogue)
    - Flash messages sections (Informs the user whether his/her actions were successfully completed, i.e. upload a movie, edit a movie, add a comment, etc.)

- **'Manage Genres' page (only for administrator)**:
    - 'Add genre' button (which redirects to the 'Add genres' page)
    - List of movie genres, each featured with:
        - Edit button (which redirects to the 'Edit genre' page)
        - Delete button
    - Flash messages sections (Informs the user if there is any issue, i.e. user cannot delete specific unless all movies of that genre in the catalogue are also deleted)

- **'Profile' page (only for signed-in users)**:
    - Section with:
        - User's username and email
        - List of movies uploaded by the user
        - Flash messages sections (To welcome the user once he/she has signed-in)

- **'Sign-in' page (only for NOT signed-in users)**:
    - Form that requires the user to insert correct username and password
    - Submit button (which also redirects the user to the profile page)
    - Link to 'Register' page
    - Flash messages sections (Informs the user if there is any issue, i.e. wrong password)

    <img src="assets/images/readme-img/contact.png" alt="contact section" width="70%"/>

    <img src="assets/images/readme-img/footer.png" alt="footer" width="70%"/>

### Pages not accessible via navbar 

- **'Register' page (only for NOT signed-in users)**: Accessible via link from 'Sign-in' page 
    - Form that requires the user to insert:
        - Username
        - Email
        - Password
        - Password confirmation
    - Submit button (which also redirects the user to the profile page)
    - Flash messages sections (Informs the user if there is any issue, i.e. username already exists, passwords do not march)

- **'Edit Movie' page (only for signed-in users)**: accessible by clickin on movie 'edit' button - see above in 'Catalogue' page
    - Form identical to the 'Add movie' page's one. However it is already filled in with the old movie infos.
    - Submit button (which also redirects the user to the movie catalogue)

- **'Add genre' page (only for webiste administrator)**: Accessible by clicking on genre 'Add Genre' button - see above in: 'Manage Genres' page
    - Form with selected genre name to be edited
    - Submit button (which also redirects the user to the 'Manage Genres' page)

- **'Edit genre' page (only for webiste administrator)**: Accessible by clicking on genre 'edit' button - see above in: 'Manage Genres' page
    - Form with selected genre name to be edited
    - Submit button (which also redirects the user to the 'Manage Genres' page)


- **'Error' page**:
    - Link to home page

    <img src="assets/images/readme-img/404.png" alt="404 page" width="70%"/>

#### Future prospects

- Section where users can watch movie trailers 
- Section to show what streaming services provide the movies from the catalogue

---

## Technologies Used 

#### Languages 


1. [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
2. [HTML5](https://en.wikipedia.org/wiki/HTML5)
3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
4. [Python](https://www.python.org)

#### Integration

1. [BSON](https://bsonspec.org)
    - bson.objectid: required dependency for MongoDB management system.
2. [Flask](https://flask.palletsprojects.com/)
    - Framework used to create and populate the templates.
3. [FontAwesome](https://fontawesome.com/)
    - Used as source of icons for the website.
4. [Google Fonts](https://fonts.google.com/) 
    - Used to import 'Monoton' font.
5. [Jinja](https://jinja.palletsprojects.com/)
    - Templating language used to simplify and display backend data in html format.
6. [jQuery](https://jquery.com/)
    - Included with Materialize and used to simplify scripts.
7. [Materialize](https://materializecss.com/)
    - Used to assist with styling and responsiveness of the website.
8. [Pymongo](https://pypi.org/project/pymongo/)
    - flask_pymongo: used to allow MongoDB database - Python interaction.
9. [Werkzeug](https://werkzeug.palletsprojects.com/)
    - Used for password hashing and authentication.


#### Workspace Version control, Repository storage and Deployment

1. [Gitpod](https://www.gitpod.io/) 
    - Used as workspace IDE (Integrated Development Environment).
2. [GitHub](https://github.com/) 
    - Hosting platform for version control, used to manage my repositories.
3. [Git](https://git-scm.com/) 
    - Version control software to record file changes and updates.
4. [Heroku](https://dashboard.heroku.com/)
    - Cloud platform used to deploy application.


---

## Resources !!!!!!!!!!!!!!!

#### Sources of knowledge
- SLACK Community - Source of assistance and inspiration. 
- [Stack Overflow](https://stackoverflow.com/) - General resource. 

#### Other resources 
- [Balsamiq](https://balsamiq.com/wireframes/) - For designing wireframes.
- [TinyPNG](https://tinypng.com/) - For compression of images.
- [Toolur](https://compressimage.toolur.com) - For re-sizing images.
- [Autoprefixer](https://autoprefixer.github.io/) - Used to parse CSS and add vendor prefixes.
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - To check whether the website is Mobile-friendly.

---
## Code validation 

### Testing

Testing documentation, including User Stories, can be found here: [Testing](static/docs/TESTING.md) 

#### Solved bugs

1. The website used to delete all comments and ratings attached to a movie when it was edited. To solve this problem I have adjusted the add_movie function so that it would create empty fields for "Ratings", "Average" (of ratings) and "Comments" when a new movie was added to the catalogue. Then, if a  Movie was edited, in case there were any rating or comment attached to it, I made sure the edit_movie function would keep the existing values for "Ratings", "Average" (of ratings) and "Comments". 
2. The website used to change the name of the user who posted a movie when it was edited. To solve the problem I made sure that the original name would be saved in the edit_movie function and not substituted by the name of the current user who edited the movie. 
3. When a movie genre was deleted from the genres list while still being connected to a movie, the action was causing some movies from the catalogue to switch another genre. This problem has been solved by ensuring that the admin must take away all movies attached to a genre before deleting the genre.

#### Unsolved bugs

1. Sometimes, the home slideshow becomes shows the white background instead of displaying the next picture.
2. When clicking on a location button for the first time, the map does not center the marker's popup. This causes the popup to partly overflow out of the map in small screen sizes. However, the problem does not reoccur after the first click. 
3. On certain mobile browsers (i.e. Safari), it is sometimes necessary to hold pressed on a marker (on the map) in order to open the popup attached, instead of just tapping on it.

---

## GitHub Pages

#### Deploying the project on GitHub Pages

  1. Log in to GitHub and locate the GitHub Repository
  2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu ("gear" icon).
  3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
  4. You will find the current message: "Pages settings now has its own dedicated tab! Check it out here!". Click the link.
  5. Under "Source", click the dropdown called "None" and select "Master Branch".
  6. The page will automatically refresh.
  7. Go back to step 4, once you have clicked the link, you will find the published site link.

#### Forking the GitHub Repository

  By forking the GitHub Repository you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository. Forking requires the following steps:

  1. Log in to GitHub and locate the GitHub Repository
  2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
  3. You should now have a copy of the original repository in your GitHub account.

#### Making a local clone of the GitHub Repository

  1. On GitHub, navigate to the main page of the repository.
  2. Above the list of files, click the green 'Code' button.
  3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
  4. Open Terminal
  5. Change the current working directory to the location where you want the cloned directory to be made.
  6. Type 'git clone', and then paste the URL you copied in Step 3: (https://github.com/Hidnish/Milestone-Project-2-Kyoto.git).
  7. Press Enter. Your local clone will be created.

---

## Credits

#### Media 

- All the pictures uploaded were retrived from: [Unsplash](https://unsplash.com/s/photos/kyoto) 
- Favicon taken from: [123RF](https://www.123rf.com/photo_65360684_stock-vector-japanese-temple-icon-illustration-isolated-sign-symbol.html)
- Custom font "Japanese Brush Master" taken from: [Online Web Fonts](https://www.onlinewebfonts.com/download/fc87c87c07938e0484418e4c0a773b02)

#### Content 

- About section content was partly based on: 
    - [Culture Trip: 10 Historical Landmarks to see in Kyoto](https://theculturetrip.com/asia/japan/articles/10-historical-landmarks-to-see-in-kyoto/)
    - [Culture Trip: The most beautiful parks in Kyoto](https://theculturetrip.com/asia/japan/articles/the-most-beautiful-parks-in-kyoto/)
- Information about specific locations was based on:
    - [Google](https://www.google.com/)
    
#### Code 

- Main sources (Specific credits are provided in the respective files, above each piece of code):
    - [W3Scgools](https://www.w3schools.com/)
    - [Stack Overflow](https://stackoverflow.com/)
    - [YouTube](https://www.youtube.com/)
    - [CSS-Tricks](https://css-tricks.com/)
    - [CI-MS2-Safari-Africa](https://github.com/JimLynx/CI-MS2-Safari-Africa)
    - Code Institute tutorial: Rosie - Resume Project.

#### Acknowledgement

- Thanks to my mentor : Oluwafemi Medale, for his support and feedback.
- Thanks to the Slack community for providing essential knowledge.