from book import Book

books = {}

while True:
  print('Book Management system')
  
  print('1. Add Book')
  print('2. Delete Book by ID')
  print('3. Display All Books')
  print('4. Search Book by Id')
  print('5. Exit')
  
  choice = int(input('Enter your choice:'))
  
  if choice == 1:
    bid = int(input('Enter Book ID:'))
  
    if bid in books:
      print('Book ID already Exists.')
    
    else:
      name = input('Enter book name:')
      price = float(input('Enter Book price:'))
      author = input('Enter  Author name:')
    
      books[bid] = Book(bid,name,price,author)
      print('Book added Successfully')
    
    
  elif choice == 2:
    bid = int(input('Enter Book ID to delete:'))
    if bid in books:
        del books[bid]
        print('Book deleted')
    else:
      print('Book not found')
      
  elif choice ==3:
    if len(books) == 0:
      print('No books available')
    else:
      for book in books.values():
        book.display()
    
  elif choice == 4:
    bid = int(input('Enter book ID to search :'))
    
    if bid in books:
      books[bid].display()
    else:
      print('Book not found')
      
  elif choice == 5:
    print('Thank you ')
    break
  
  else:
    print('Invalid choice')

        
    
