import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'books'
#förösk spara danhoff:UrSEzkJwRg0yELxb i environmental variabel så att lösenord ej syns på github
app.config["MONGO_URI"] = mongodb+srv://danhoff:UrSEzkJwRg0yELxb@bookscluster-pabzd.mongodb.net/books?retryWrites=true&w=majority


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)