books = [
  {
    "title": "Englisha",
    "authors":["akash", "Ashik"],
    "isbn": "1xc4",
    "Publishing_year": 2013,
    "price": 500.36,
    "quantity": 5
  },
  {
    "title": "Ab",
    "authors":["a", "b", "c"],
    "isbn": "a23",
    "Publishing_year": 2015,
    "price": 325.6,
    "quantity": 2
  },
  {
    "title": "Axu",
    "authors":["ax", "byk", "cz"],
    "isbn": "a234",
    "Publishing_year": 2015,
    "price": 325.6,
    "quantity": 2
  },
]

users = [
  {
    "name": "Akash",
    "phone": "01760864356",
    "pin": "1234"
  },
  {
    "name": "Ashik",
    "phone": "01760113265",
    "pin": "5678"
  },
]

lend_books = []

def add_book():
  title = input("Enter book title: ")
  isbn = input("Enter book's ISBN number: ")
  Publishing_year = int(input("Enter book's publishing year: "))
  price = float(input("Enter book's price: "))
  quantity = int(input("Enter book's quantity: "))
  number_of_author = int(input("Enter how many authors: "))
  authors = []
  if type(number_of_author) is int:
    for x in range(number_of_author):
      author = input(f"Enter author {x+1}: ")
      authors.append(author)
  else:
    print("Enter an integer number")
  book = {
    "title": title,
    "authors": authors,
    "isbn": isbn,
    "Publishing_year": Publishing_year,
    "price": price,
    "quantity": quantity
  }
  books.append(book)
  print("Books Added.")

def show_books():
  print("BOOKS")
  print("--------")
  count = 0
  for book in books:
    count = count+1
    print(f"\nBook: {count}\n")
    number_of_author = len(book["authors"])
    
    print(f"Title: {book["title"]}\nISBN: {book["isbn"]}\nPublished: {book["Publishing_year"]}\nPrice: {book["price"]}\nQuantity: {book["quantity"]}")
    
    for x in range(number_of_author):
      print("Author ", x+1, ":", book["authors"][x])

def search_books():
  search_tearm = input("Enter text to search books: ")
  search_tearm_lower = search_tearm.lower()
  book_found = []
  index_found = []
  
  for index, book in enumerate(books):
    title_lower = book["title"].lower()
    isbn_lower = book["isbn"].lower()
    
    if search_tearm_lower in title_lower or search_tearm_lower in isbn_lower:
      number_of_author = len(book["authors"])
    
      print(f"\nId: {index+1}\nTitle: {book["title"]}\nISBN: {book["isbn"]}\nPublished: {book["Publishing_year"]}\nPrice: {book["price"]}\nQuantity: {book["quantity"]}")
      
      for x in range(number_of_author):
        print("Author ", x+1, ":", book["authors"][x])
      book_found.append(book)
      index_found.append(index+1)
  
  if len(book_found) == 0:
    print("No book found!")
    return 0, 0
  else:
    return book_found, index_found

def search_by_authors():
  search_term = input("Enter text to search books: ")
  search_term_lower = search_term.lower()
  book_found = []
  index_found = []
  
  for index, book in enumerate(books):
    for author in book["authors"]:
      if search_term_lower in author.lower():
        print(f"\nId: {index+1}\nTitle: {book["title"]}\nISBN: {book["isbn"]}\nPublished: {book["Publishing_year"]}\nPrice: {book["price"]}\nQuantity: {book["quantity"]}\nAuthor: {author}")
        book_found.append(book)
        index_found.append(index+1)
  if len(book_found) == 0:
    print("No book found!")
    return 0, 0
  else:
    return book_found, index_found
    
def remove_book(book_found, index_found):
  if book_found != 0:
    selected_index = int(input("Select an id to remove: "))
    if selected_index in index_found:
      books.pop(selected_index - 1)
      print("Contact Removed.")
    else:
      print("Wrong id selected!")

def create_user():
  name = input("Enter your name: ")
  phone = input("Enter your phone: ")
  pin = input("Enter your pin: ")
  
  user = {
    "name": name,
    "Phone": phone,
    "pin": pin
  }
  
  users.append(user)
  print("User created sucessfully.")

def book_lend():
  user_name = input("Enter your user name: ")
  user_pin = input("Enter your pin: ")
  user_name_lower = user_name.lower()
  user_pin_lower = user_pin.lower()
  
  for user in users:
    if user_name_lower == user["name"].lower() and user_pin_lower == user["pin"].lower():
      book_found, index_found = search_books()
      if book_found != 0 and index_found != 0:
        selected_index = int(input("Enter an book id to lend: "))
        if selected_index in index_found and books[selected_index - 1]["quantity"] > 0:
          new_quantity = books[selected_index - 1]["quantity"] - 1
          books[selected_index - 1].update(
            {
              "quantity": new_quantity,
            }
          )
          lend_book = {
            "user_name": user_name,
            "book_title": books[selected_index - 1]["title"],
            "book_author": books[selected_index - 1]["authors"][0],
            "book_isbn": books[selected_index - 1]["isbn"],
          }
          lend_books.append(lend_book)
          print(f"Book lended by {user_name} successfully.")
        else:
          print("Book quantity is 0")
      break
    else:
      print("Wrong userName or pin!")
      break

def show_lend_book():
  if len(lend_books) != 0:
    for book_lend in lend_books:
      print(
        book_lend["user_name"],
        book_lend["book_title"],
        book_lend["book_author"],
        book_lend["book_isbn"],
        sep="|"
      )
  else:
    print("No Lend book here.")

def return_book():
  user_name = input("Enter your user name: ")
  user_pin = input("Enter your pin: ")
  user_name_lower = user_name.lower()
  user_pin_lower = user_pin.lower()
  
  for user in users:
    if user_name_lower == user["name"].lower() and user_pin_lower == user["pin"].lower():
      book_isbn = input("Enter return's book isbn: ")
      for index, lend_book in enumerate(lend_books):
        if lend_book["book_isbn"] == book_isbn:
          lend_books.pop(index)
          print("Book return successfully.")
          for index, book in enumerate(books):
            if book["isbn"] == book_isbn:
              new_quantity = book["quantity"] + 1
              books[index].update(
                {
                  "quantity": new_quantity
                }
              )
              break
          print(new_quantity)
        else:
          print("ISBN dosen't match!")
      break
    else:
      print("Wrong userName or pin.....!")
      break
          

#Menu
menu = """
Menu options:-
1. Add Books
2. Show Books
3. Search Books
4. Search by author
5. Remove book
6. Create new user
7. Lend book
8. Show lends books
9. Return book
0. Exit
"""

search_option = """
Search options:-
1. Title
2. ISBN
3. Author
"""
print("Welcome")

while True:
  print(menu)
  choice = input("Choice an option: ")
  if choice == "0":
    break
  elif choice == "1":
    add_book()
  elif choice == "2":
    show_books()
  elif choice == "3":
    search_books()
  elif choice == "4":
    book_found, index_found = search_by_authors()
  elif choice == "5":
    print(search_option)
    option = input("Select an option: ")
    if option == "1" or option == "2":
      book_found, index_found = search_books()
      remove_book(book_found, index_found)
    elif option == "3":
      book_found, index_found = search_by_authors()
      remove_book(book_found, index_found)
    else:
      print("Wrong option selected!")
  elif choice == "6":
    create_user()
  elif choice == "7":
    book_lend()
  elif choice == "8":
    show_lend_book()
  elif choice == "9":
    return_book()
  else:
    print("Wrong option chosed!")