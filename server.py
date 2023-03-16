from flask import Flask, render_template
import pymongo


app = Flask(__name__)

# Setup MongoDB
client = pymongo.MongoClient("mongodb+srv://indianspeedster:iLhGAcO21DRHTyt1@cluster0.ikmbwgh.mongodb.net/?retryWrites=true&w=majority")
db = client.mydatabase

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<name>", methods=['GET'])
def author(name):

    # Reference to Books Collection in the DB
    books = db.author_books

    bookList = []
    bio = ""
    links = []
    for book in books.find():
        if (name in book['authors']):
            bookList.append(book['title'])
            bio = book['bio']
            links = book['book_link']

    return render_template("author.html", name=name, books=bookList, bio= bio, links= links)

if __name__ == "__main__":
    app.run()