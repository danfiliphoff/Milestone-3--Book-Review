import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'books'
#
app.config["MONGO_URI"] = os.environ.get('mongodb_name') 
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())

@app.route('/add_book')
def add_book():
    return render_template("addbook.html",
        genre=mongo.db.genre.find())

@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('add_book'))

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book =  mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_genre =  mongo.db.genre.find()
    return render_template('editbook.html', book=the_book,
                           genre=all_genre)

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    book = mongo.db.books
    book.update( {'_id': ObjectId(book_id)},
    {
        'name':request.form.get('name'),
        'author':request.form.get('author'),
        'genre_name':request.form.get('genre_name'),
        'isbn':request.form.get('isbn'),
        'review':request.form.get('review'),
        'book_link':request.form.get('book_link')
    })
    return redirect(url_for('get_books'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_books'))

#below code to count votes
@app.route('/upvote_book/<book_id>')
def upvote_book(book_id):
    #add 1 to count value in mongodb. so add a number to the database
    # return current value for "votes" in mongodb. I have added votes to collection.
    book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
           # add one to "votes"
    votes = book['votes'] + 1 
        # submit new total value of "votes" to mongo db 
    book.update( {'_id': ObjectId(book_id)},
    {
        'votes':request.form.get(votes),
    })
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)