# Book Review
A simple website where users can submit books with a review and vote on the reviews submitted by others.

## UX
The site allows users to add, eddit and browse book reviews. Users can chose to browse books by cathegory to help  the user find the type of book 
he/she is looking for. Users can add links to each book so that the book can easily be found and on the webb. To help the users find the best books, a simple 
voting system ranks the books. The users goal is to find good book reviews and get ideas on what books are worth reading.

In the early stages of development the below wireframe was made as a general concept of how the site would look:
![Image of Wireframe](https://raw.githubusercontent.com/danfiliphoff/Milestone-3--Book-Review/master/static/readme_pictures/wireframe%20milestone3.PNG)


## Features

### Existing Features
The main page shows all submitted books ranked after number of votes. This allows the user to browse all books sorted after most votes.

The genre page allows a user to browse after books based on varoius cathegories. Both the genre and main page
pressents the books on cards. Each card have an edit, vote, and link button for that particular book. These buttons allows the user to vote, update the details for a book and find the book on the webb.
The number of votes a review have recived is also displayed on the card. Users can add books thrue a form accesed 
by the "add book" button in the nav bar. 

### Features left to implement
A search field in the nav bar would greatly help users find what they are looking for as the database expands. Also a feutre where a new review can be added to an already existing book could be
implemented. 

## Technologies Used
- Pymongo to ease the database intergration.
- Jquery to run Materilize scripts
- HTML as markup languge.
- Flask to easly manage my templates

## Testing
All pages have been manualy tested as specified below:

1. addbook.html 
    1. Try to submit form with one or several empty fields, should be unsucessful and give feedback on what field is missing.
    2. Try to submit form with all fields fild in and go to books.html, book should apper on this page. 
2. base.html- Go to each .html page and check that the home, add a book and genre buttons in the navbar all directs towards the correct page.
Clicking on the "book review" should link to books.html.
3. books.html
    1. Press the buy this book button and make sure that it links to an external page.
    2. Test up and downvote buttons, the displayed total should change in accordance with what buttonis pressed. 
    3. Pressing eddit button should redirect to eddit page. 
    4. Delete button should delete the book. 
4. editbook.html
    1. Check so that all info for each field is correctly retrived from the database.
    2. Make a change and submit to make sure it uppdates correctly.
    3. Delete one or more fields, the form should not be allowed to submit with empty fields.
5. genre.html
    1. Press the buy this book button and make sure that it links to an external page.
    2. Test up and downvote buttons, the displayed total should change in accordance with what buttonis pressed. 
    3. Pressing eddit button should redirect to eddit page. 
    4. Delete button should delete the book.
    5. Test the genre select by clicking it. If it works only books to the selected genre should display.

## Deployment
This project have been deplyed using Heroku. An app was created in Heroku. The projects github repository was then conected to Heroku 
so that all commits to the github master branch automaticaly updates the aplication in heroku. To allow heroku to run the application sucessfully
an requirements file and a procfile have been included in the project. 

Environmental variables containing the log in information to the database have been set. 


## Credits
The example book reviews included in the site have been copied from wikipedia articals. 

# Acknowlegements
This project was made possible thrue the suport of the tutors at code institute.


