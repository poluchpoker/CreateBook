from flask import Flask, request
from db import DB
import json

app = Flask('my_server')

@app.route('/book', methods=['POST'])
def book():
  name = request.form['name']
  books = request.form['books']
  print({'name': name, 'books': books})
  DB.append({'name': name, 'books': books})
  return {'status': True, 'DB': DB}
  
@app.route('/book')
def get_book():
  return {'status': True, 'DB': DB}

app.run(host='0.0.0.0', port=6000)
