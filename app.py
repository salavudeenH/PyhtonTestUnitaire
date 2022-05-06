from flask import Flask, make_response,request,jsonify
from flask_mongoengine import MongoEngine
import unittest
app = Flask(__name__)
database_name = "Python"
DB_URI = "mongodb+srv://Jeeves123:Jeeves123@cluster0.q76xt.mongodb.net/Python?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)


class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def to_json(self):
        #convert le document en JSON
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author
        }
    
@app.route('/api/db_populate',methods=['POST'])
def db_populate():
    book1 = Book(book_id= 1, name= "Salut sala",author= "HADJI")
    book2 = Book(book_id= 2, name= "GTA 5",author= "ROCKSATR")
    book1.save()
    book2.save()
    return make_response("",201)

@app.route('/api/books',methods=['GET','POST'])
def api_books():
    if request.method == "GET": 
        books = []
        for book in Book.objects:
            books.append(book)
        return make_response(jsonify(books),200)
    elif request.method == "POST": 
        content = request.json
        book = Book(book_id=content['book_id'],
        name=content['name'],
        author=content['author'])
        book.save()
        return make_response("bien enregistré",201)

@app.route('/api/books/<book_id>',methods=['GET','PUT','DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        book_obj = Book.objects(book_id=book_id).first()
        if book_obj:
            return make_response(jsonify(book_obj.to_json()),200)
        else:
            return make_response("",404)
    elif request.method == "PUT":
        content = request.json
        book_obj = Book.objects(book_id=book_id).first()
        book_obj.update(author=content['author'],name=content['name'])
        return make_response("Il a bien ete mis a jour",200)

    elif request.method == "DELETE":
        book_obj = Book.objects(book_id=book_id).first()
        book_obj.delete()
        return make_response("Ton livre est supprimé",200)
        else:
            return make_response("",404)
if __name__ == '__main__':
    app.run()
    

# requests.get("http://localhost")


# requests.get('http://localhost:5000/api/books').json()