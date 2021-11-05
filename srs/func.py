import requests 
import json

response = requests.get('https://create.poluchpoker.repl.co/book')
DB = response.json()['DB']

def addAuthor():
    print('имя автора:')
    name = input()
    for author in DB:
      if name == author['name']:
        print('Такое имя уже занято!')
        return
    DB.append({'name': name, 'books': []})
    
        
def addBook():
    print('имя автора:')
    name_author = input()
    print('название книги:')
    name_book = input()
    for author in DB:
      if name_author == author['name']:
        author['books'].append(name_book)
    
    
def read():
    print('имя автора для чтения:')
    name = input()
    for author in DB:
      if name == author['name']:
        print(author['books'])
    
def deleteAuthor():
  print('имя автора для удаления пользователя:')
  name = input()
  for author in DB:
      if name == author['name']:
        DB.remove(author)

def deleteBook():
    print('имя автора для удаления книги:')
    name_author = input()
    print('название книги для удаления:')
    name_book = input()
    for author in DB:
      if name_author == author['name']:
        author['books'].remove(name_book)
        
def changebook():
    print('имя автора:')
    name_author = input()
    print('название книги:')
    name_book = input()
    print('на какое название хотите поменять текущее:')
    new_name_book = input()
    for author in DB:
      if name_author == author['name']:
        author['books'].remove(name_book)
        author['books'].append(new_name_book)

def start():     
  while True:
      print('addAuthor, addBook, read, changebook, deleteAuthor, deleteBook, exit')
      comand = input()
      if comand == 'addAuthor':
          addAuthor()
      if comand == 'addBook':
          addBook()
      if comand == 'read':
          read()
      if comand == 'deleteAuthor':
          deleteAuthor()
      if comand == 'deleteBook':
          deleteBook()
      if comand == 'changebook':
          changebook()
      if comand == 'exit':
          break

print(DB)

start()

print(DB)

for author in DB:
  requests.post('https://create.poluchpoker.repl.co/book', data ={
    'name': author['name'],
    'books': author['books']
  })
