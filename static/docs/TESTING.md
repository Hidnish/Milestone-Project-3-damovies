# DaMovies - Testing Documentation

<br>

## Contents Table

1. [**Testing 'User Stories'**](#testing-user-stories)
    - **First time visitor goals**
    - **Returning or frequent visitor goals**

2. [**Manual Testing**](#manual-testing)
      
3. [**Automated Testing**](#automated-testing)
    - **HTML**
    - **CSS**
    - **JavaScript**
    - **Python**

4. [**Responsiveness**](#responsiveness)

<br>

---

### Testing User Stories 

<br>

#### As a first time visitor

- I want to easily understand the main purpose of the site

    - Right below the home hero-image, the user will find a section that describes the website's purpose

- I want the site navigation to be intuitive and user friendly

    - On top of every page there is a fixed navbar (except the 'error' page) which links to the main pages of the website. 

- I want to create an account to become part of the website community 

    - By clicking on the 'sign-in' button the user is redirected the respective page. Here the user can find a link below the sing-in form that will bring him/her to the registration form.

- I want to see information about movies in the catalogue (i.e. director, year of release)

    - After accessing the catalogue by clicking on the respective link in the navbar, the user is provided with the list of movies that have been added to the website. At the bottom of each movie 'card' there is an icon that can be clicked to reveal the movie's information. 

- I want to see the audience rating of movies in the catalogue

    - In the same section where the user can find the movie information, there is a section that shows the average rating by the users (on a scale from 1 to 5).

- I want to add my rating

    - Below the average rating, there is a radio button form where the user can submit his/her own rating.

- I want to see other users comments on movies in the catalogue

    - Below the ratings the user can see the list of comment on the movie left by the users.

- I want to add my own comment

    - By comment list, there is a text area where the user can leave his/her own comment.

- I want to add movies that I like to the catalogue

    - After registering, the user can access the 'Add movie' page by clicking on the respective link in the navbar. The page provides the user with a form to fill out with the movie's info (i.e. title, director, etc.) and a submit button. 

- I want to be able to edit information of the movies I have uploaded in the catalogue

    - The user can find the movie he/she uploaded by scolling through the catalogue or by using the search bar. Once he/she finds the movie, there is an 'Edit' button on the bottom of the movie 'card' that will redirect him/her to the 'Edit movie' page.

- I want to be able to delete movies I have uploaded

    - Next to the 'Edit' button mentioned in the last point, the user will find a 'Delete' button. 

<br>

#### As a returning and/or frequent visitor

<br>

- I want to easily log-in in to the website

    - By clicking on the 'sign-in' button the user is redirected the respective page. Here he/she can sign-in by filling the form with username and password and clicking the submit button.

- When I have questions about the website, I want to find information about the website creator/administrator  

    - The user can find a link to the GitHub account of the website creator on the right side of the footer. 

<br>

---

### Manual Testing 

<br>

#### Navbar

- All links work correctly and redirect the user to the right url.
- When clicked the hamburger icon triggers dropdown nav menu, which links work correctly.
- Logo works as link to home page.

#### Footer

- Copyright message brings the user back to the home page when clicked.
- Github link brings the user to my repository opening a new tab.

<br>

--- Links accessible through the navbar ---

<br>

#### Home Page 

- Links in the website description bring the user to the correct page (either: 'Catalogue' or 'Sign-in' for NOT signed-in users or 'Catalogues' or 'Add movies' for signed-in users).

#### Catalogue Page 

- Search bar filters the movies correctly based on movie 'title' or 'director' after typing the name and clicking the Search button.
- Search bar's Reset button refereshes the page correctly 
- Movie's Edit button (when visible)* works correcly and redirects the user to the 'Edit movie' page 
- Movie's Delete button (when visible)* works correctly. First it triggers a pop dialog to confirm the user's choice. If the user presses 'Ok' the movie gets deleted. 
- Info icon (3 dots vertically aligned) opens the movie's 'Info card' correctly, displaying movie's information, rating and comments
- The rating form (when visible)* uploads the user's rating correctly when he/she presses the submit button, and adds it to the average rating
- The comment text arena (when visible)* adds the user's comment to the list of comments.
- The comment's delete button (when visible)* deletes the comment from the list as expected.
- Flash messages arena gives feedback regarding:
    - Movie has been uploaded
    - Movie has been edited
    - Movie has been deleted
    - Rating has been added
    - Comment has been added
    - Comment has been deleted

#### Sign-in Page (Only for NOT signed-in users)

- Form inputs works. 
- Form validations work as expected.
- Sign-In button works as expected and submits data successfully, and redirects user to Profile page.
- Flash messages area gives feedback regarding:        
    - Unmatched format 
    - Incorrect username 
    - Incorrect password 
    - If user doesn't exist in the database.
    - If user has just sign-out

#### Register Page (Only for NOT signed-in users)

- Form inputs works. 
- Form validations work as expected.
- Register button works as expected and redirects user to Profile page.
- Flash messages area gives feedback regarding:   
    - Username already exists in the database
    - Password does not match Password confirmation

#### Add Movies Page (Only for signed-in users)

- All the fields in the form (except the movie cover image URL) require correct input by the user.
- With the submit button, the new movie is uploaded correctly to the database for display in the catalogue.

#### Manage Genres Page (Only for administrator)

- The 'Add genre' button redirects to the respective page without issues.
- The 'Edit' button, for each movie genre, redirects to the respective 'Edit genre' page.
- The 'Delete' button, for each movie genre, deletes the movie correctly (As long as all movies linked to that genre are first removed from the list)

#### Profile Page (Only for signed-in users)

- The page displays the user's username, email address, and list of movies uploaded to the catalogue correctly.
- Flash messages area:
    - Welcomes user after sign-in 
    - Informs user when registration was successful 

#### Sign Out Button (Only for signed-in users)

- Signs out user and redirects him/her to the Sign-In page and removes session cookie 


<br>

--- Links NOT accessible through the navbar ---

<br>

#### Edit Movie Page (Only for signed-in users)

- All the fields in the form are occupied by the original movie infos. When edited require correct input by the user.
- With the submit button, the  movie is edited correctly, updated in the database and displayed in the catalogue.
- The Cancel button redirects the user to the movie catalogue as expected.

#### Add Genre Page (Only for administrator)

- The field in the form requires input by the user
-  With the submit button, the new genre is uploaded correctly to the database for display in the Manage Genres page.

#### Edit Genre Page (Only for administrator)

- The field in the form is occupied by the original genre name. When edited requires correct input by the user.
- With the submit button, the  movie is edited correctly, updated in the database and displayed in the Manage Genres page.
- Changes applied to a genre's name are also reflected in the Movie's info 'cards' in the catalogue (for movies of that genre).
- The Cancel button redirects the user to the Manage Genres page as expected.

#### Error Page 

- The error page's link brings back to the website's Home page as expected

<br>

---

### Automated Testing 

<br>

#### HTML

HTML code was passed through [HTML Validator](https://validator.w3.org/).
- No errors found or warnings shown

<br>

#### CSS

CSS code was passed through [CSS Validator](https://jigsaw.w3.org/css-validator/)
- No errors found or warnings shown

<br>

#### JavaScript

Javascript code was passed through [JSHINT](https://jshint.com/)
- No errors found. Warnings for the "$" sign from Jquery which was not recognised by the code validator 

<br>

#### Python

Python code was passed trhough [PEP8 Online Check](http://pep8online.com/)
- No erros found or warning shown 

<br>

---

### Responsiveness 

<br>


- The Website was tested on the following browsers:
    - Google Chrome
    - Safari
    - Opera
    - Firefox
    - Microsoft Edge
- The Website was tested on a variety of screen sizes using Google Developer Tools: 
    - iPhone 5 
    - iPhone 6/7/8 
    - iPhone X 
    - Samsung Galaxy S III
    - Motorola Nexus 6
    - iPad
    - iPad Pro 
    - Microsoft Surface Duo 
    - 19-inch screen (1280px)
    - 20-inch screen (1600px)
    - Widescreen (1920px)
- The Website was tested on physical devices:   
    - iPhone 6s
    - iPhone 8
    - MacBook Air
- [Google mobile-friendly test](https://search.google.com/test/mobile-friendly?id=5Pz7BqGGcZdRd5o9rkxA9A): All pages in the website (except the profile page which was not accessible through the validator) passed the test as mobile friendly






