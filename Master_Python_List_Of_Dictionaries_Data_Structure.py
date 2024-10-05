# List of product dictionaries
products = [
    {"name": "Laptop", "category": "Electronics", "id": 1, "price": 750, "stock": 50, "supplier email": "supplier1@gmail.com"},
    {"name": "Desk Chair", "category": "Furniture", "id": 2, "price": 100, "stock": 200, "supplier email": "supplier2@gmail.com"},
    {"name": "Smartwatch", "category": "Electronics", "id": 3, "price": 200, "stock": 150, "supplier email": "supplier3@gmail.com"},
    {"name": "Notebook", "category": "Stationery", "id": 4, "price": 5, "stock": 500, "supplier email": "supplier4@gmail.com"},
    {"name": "Running Shoes", "category": "Apparel", "id": 5, "price": 80, "stock": 100, "supplier email": "supplier5@gmail.com"}
]

# Print product data
for product in products:
    print(f"Name: {product['name']}, Category: {product['category']}, price: {product['price']}, stock: {product['stock']}, supplier email: {product['supplier email']}")

# List of employee dictionaries
employees = [
    {"name": "John Doe", "department": "Sales", "id": 1, "age": 30, "email": "john.doe@company.com"},
    {"name": "Jane Smith", "department": "Human Resources", "id": 2, "age": 25, "email": "jane.smith@company.com"},
    {"name": "Mark Johnson", "department": "IT", "id": 3, "age": 40, "email": "mark.johnson@company.com"},
    {"name": "Lisa Wong", "department": "Marketing", "id": 4, "age": 28, "email": "lisa.wong@company.com"},
    {"name": "Paul Mcdonald", "department": "Finance", "id": 5, "age": 35, "email": "paul.mcdonald@company.com"}
]

# Print employee data
for employee in employees:
    print(f"Name: {employee['name']}, Department: {employee['department']}, Email: {employee['email']}, Age: {employee['age']}")

# List of books dictionaries
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "published year": 1925, "id": 1, "isbn": "978-0743273565", "stock": 20, "price": 15.99},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "published year": 1960, "id": 2, "isbn": "978-0060935467", "stock": 35, "price": 10.99},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "published year": 1949, "id": 3, "isbn": "978-0451524935", "stock": 40, "price": 9.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "published year": 1951, "id": 4, "isbn": "978-0316769488", "stock": 25, "price": 8.99},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Non-Fiction", "published year": 1988, "id": 5, "isbn": "978-0553380163", "stock": 10, "price": "18.99"}
]

# Print books data
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, {book['published year']}, Published Year: {book['published year']}, ISBN: {book['isbn']}, Stock: {book['stock']}, Price: {book['price']}")

# List of univerities data
universities = [
    {"name": "University of the Philippines", "location": "Quezon City", "established year": 1908, "id": 1, "type": "Public", "website": "www.up.edu.ph"},
    {"name": "Ateneo de Manila University", "location": "Quezon City", "established year": 1859, "id": 2, "type": "Private", "website": "www.ateneo.edu"},
    {"name": "De La Salle University", "location": "Manila", "established year": 1911, "id": 3, "type": "Private", "website": "www.dlsu.edu.ph"},
    {"name": "University of Santo Tomas", "location": "Manila", "established year": 1611, "id": 4, "type": "Private", "website": "www.ust.edu.ph"},
    {"name": "Polytechnic University of the Philippines", "location": "Manila", "established year": 1904, "id": 5, "type": "Public", "website": "www.pup.edu.ph"}
]
# Print universities data
for university in universities:
    print(f"Name: {university['name']}, Location: {university['location']}")

# List of restaurants data
restaurants = [
    {"name": "Vikings Luxury Buffet", "location": "Pasay City", "cuisine type": "Buffet", "established year": 2011, "id": 1, "website or contact": "www.vikings.ph"},
    {"name": "Antonio's Restaurant", "location": "Tagaytay", "cuisine type": "Fine Dining", "established year": 2002, "id": 2, "website or contact": "www.antoniosrestaurant.ph"},
    {"name": "Mesa Filipino Moderne", "location": "Makati City", "cuisine type": "Filipino", "established year": 2009, "id": 3, "website or contact": "www.mesa.ph"},
    {"name": "Manam Comfort Filipino", "location": "Quezon City", "cuisine type": "Filipino", "established year": 2013, "id": 4, "website or contact": "www.manam.ph"},
    {"name": "Ramen Nagi", "location": "Various Locations", "cuisine type": "Japanese", "established year": 2013, "id": 5, "website or contact": "www.ramennagi.com.ph"}
]

# Print restaurants data
for restaurant in restaurants:
    print(f"Name: {restaurant['name']}, Location: {restaurant['location']}, Cuisine Type: {restaurant['cuisine type']}, Established Year: {restaurant['established year']}, Website or Contact: {restaurant['website or contact']}")