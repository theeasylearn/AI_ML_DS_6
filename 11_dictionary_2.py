#nesting 
book = {}
print(book)
book['name'] = "the secret"
book['price'] = 400
book['chapters'] = (1,2,3,4)
book['topics'] = ['introduction','index','what is secret','summery']
print(book)
book['topics'][0] = 'about author'
print(book['topics'][0])
# book['chapters'][0] = 100 #error because topics is immutable
print(book)