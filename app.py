import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'books'
app.config["MONGO_URI"] = os.environ.get('mongodb_name') 
mongo = PyMongo(app)


#Renders books.html and sorts book cards in order of total votes.
@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find().sort("votes", -1))

#Renders addbook.html and retrives values for genre dropdown list.
@app.route('/add_book')
def add_book():
    return render_template("addbook.html",
        genre=mongo.db.genre.find().sort("genre_name"))

#Renders genre.html, gets genres for selection and sort books after number of votes.
@app.route('/genres')
def genres():
    books = mongo.db.books.find().sort("votes", -1)
    genre = mongo.db.genre.find().sort("genre_name")
    return render_template("genre.html", books= books, genre = genre)

#Allows the user to sort by genre on genre.html page.
@app.route('/selected_genre/<genre_name>')
def selected_genre(genre_name):
    books = mongo.db.books.find({"genre_name": genre_name}).sort("votes", -1)
    genre = mongo.db.genre.find().sort("genre_name")
    return render_template("genre.html", books= books, genre = genre)

#Allows submition of a new book to the database.
@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('add_book'))

#Renders editbook.html 
@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book =  mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_genre =  mongo.db.genre.find().sort("genre_name")
    return render_template('editbook.html', book=the_book,
                           genre=all_genre)

#Allows the user to eddit entries in teh database
@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    book = mongo.db.books
    book.update({'_id': ObjectId(book_id)},
    {
        'name':request.form.get('name'),
        'author':request.form.get('author'),
        'genre_name':request.form.get('genre_name'),
        'review':request.form.get('review'),
        'book_link':request.form.get('book_link')
    })
    return redirect(url_for('get_books'))

#Allows user to delete a book and be redirected to books.html
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_books'))

#Allows user to delete a book and be redirected to genre.html
@app.route('/delete_book_genre/<book_id>')
def delete_book_genre(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('genres'))


@app.route('/upvote_book/<book_id>')
def upvote_book(book_id):
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {'$inc': {'votes': 1}},
    upsert=False)
    return render_template("books.html", books=mongo.db.books.find().sort("votes", -1))   

@app.route('/downvote_book/<book_id>')
def downvote_book(book_id):
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {'$inc': {'votes': -1}},
    upsert=False)
    return render_template("books.html", books=mongo.db.books.find().sort("votes", -1))

@app.route('/upvote_book_genre/<book_id>')
def upvote_book_genre(book_id):
    books = mongo.db.books.find().sort("votes", -1)
    genre = mongo.db.genre.find().sort("genre_name")
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {'$inc': {'votes': 1}},
    upsert=False)
    return render_template("genre.html", books=books, genre = genre)   

@app.route('/downvote_book_genre/<book_id>')
def downvote_book_genre(book_id):
    books = mongo.db.books.find().sort("votes", -1)
    genre = mongo.db.genre.find().sort("genre_name")
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {'$inc': {'votes': -1}},
    upsert=False)
    return render_template("genre.html", books=books, genre = genre)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 3000)),
            debug=True)