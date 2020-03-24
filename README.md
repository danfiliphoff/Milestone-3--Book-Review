# Book Review
A simple website where users can submit books with a brief coment and vote on the books submitted by others.

## UX
The site allows users to add, eddit and browse book reviews. Users can chose to browse books by cathegory to help  the user find the type of book 
he/she is looking for. Users can add links to each book so that the book can easily be found and purchased on the webb. To help the users find the best books, a simple 
voting system ranks the books. The users goal is to find good book reviews and get ideas on what books are worth reading.

![Image of Wireframe](https://raw.githubusercontent.com/danfiliphoff/Milestone-3--Book-Review/master/static/readme_pictures/wireframe%20milestone3.PNG)


## Features

### Existing Features
The main page shows all submitted books ranked after number of votes. The genre page allows a user to browse after books based on varoius cathegories. Both the genre and main page
pressents the books on cards. Each card have an edit, vote, and link button for that particular book. The number of votes a review have recived is also displayed. Users can add books thrue a form accesed 
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
    2. Try to submit form with all fields fild in. book should apper on books.html page. 
2. base.html- Go to each .html page and check that the home, add a book and genre buttons in the navbar all directs towards the correct page.
Clicking on the "book review" should link to books.html.
3. books.html
4. editbook.html
5. genre.html

## Deployment

## Credits
# Content
# Acknowlegements


