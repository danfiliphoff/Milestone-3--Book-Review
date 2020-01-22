import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'books'
#förösk spara danhoff:UrSEzkJwRg0yELxb i environmental variabel så att lösenord ej syns på gith
app.config["MONGO_URI"] = 'mongodb+srv://danhoff:UrSEzkJwRg0yELxb@bookscluster-pabzd.mongodb.net/books?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())


#nedan kod binder databasen till genra så att det i addbook.py går att gå igenom
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
def book_task(book_id):
    the_book =  mongo.db.books.find_one({"_id": ObjectId(books_id)})
    all_genre =  mongo.db.genre.find()
    return render_template('editbook.html', book=the_book,
                           genre=all_genre)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)