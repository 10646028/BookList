from operator import truediv
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flasgger import Swagger
import uuid

app = Flask(__name__)
api = Api(app)

app.config['SWAGGER'] = {
    "title": "Test API",
    "description": "Test API",
    "version": "1.0.0",
    "termsOfService": "",
    "hide_top_bar": True
}

# enable CORS
CORS(app)

Swagger(app)

# Define parser and request args
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title', help='title is required', location=['json', 'args'], required=True)
parser.add_argument('author', help='author is required', location=['json', 'args'], required=True)
parser.add_argument('read', help='read is required', location=['json', 'args'], required=True)

parser_put = reqparse.RequestParser(bundle_errors=True)
parser_put.add_argument("id", help="id is required", location=["json", "args"], required=True)
parser_put.add_argument('title', help='title is required', location=['json', 'args'], required=True)
parser_put.add_argument('author', help='author is required', location=['json', 'args'], required=True)
parser_put.add_argument('read', help='read is required', location=['json', 'args'], required=True)

parser_del = reqparse.RequestParser(bundle_errors=True)
parser_del.add_argument("id", help="id is required", location=["json", "args"], required=True)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': 'true'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': 'false'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': 'true'
    }
]


class API_BOOK(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     self.reqparse.add_argument('title', type=str, required = True, help = u'No task title provided', location = 'json')
    #     self.reqparse.add_argument('description', type=str, default='', location='json')
    #     super(API_BOOK, self).__init__()
    
    def get(self):
        return jsonify({
            'status': 'success',
            'books': BOOKS 
        })

    def post(self):
        args = parser.parse_args(strict=True)
        for i in (0, len(BOOKS)-1):
            if args['title'] == BOOKS[i]['title']:
                response_object = {'message': "Title already exists.", 'status': "Failed"}
                return jsonify(response_object)

        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': args['title'],
            'author': args['author'],
            'read': args['read']
        })
        response_object = {"message": "Book added!", 'status': 'success'}
        return jsonify(response_object)

    def put(self):
        response_object = {'status': 'success'}
        args = parser_put.parse_args(strict=True)
        id = args["id"]
        flg = remove_book(id)
        if flg:
            BOOKS.append({
                'id': args["id"],
                'title': args['title'],
                'author': args['author'],
                'read': args['read']
            })
            response_object['message'] = 'Book updated!'
        else:
            response_object = {'message': "Can't find this book.", 'status': "Failed"}

        return jsonify(response_object)
        
    def delete(self):
        response_object = {'status': 'success'}
        args = parser_del.parse_args(strict=True)
        id = args["id"]
        flg = remove_book(id)
        if flg:
            response_object['message'] = 'Book deleted!'
        else:
            response_object = {'message': "Can't find this book.", 'status': "Failed"}
        
        return jsonify(response_object)

def remove_book(book_id):
    for i in range(0, len(BOOKS)):
        if(BOOKS[i]['id'] == book_id):
            BOOKS.pop(i)
            return True
    return False

api.add_resource(API_BOOK, '/v1/books/',  endpoint = 'api_book')

if __name__ == '__main__':
    app.run(debug=True)