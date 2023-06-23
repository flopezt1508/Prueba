product = {
    "name" : "book",
    "quantity" : 3,
    "price" : 4.99
}

person = {
   "first_name" : "Francisco",
   "last_name" : "López"
}

print(type(product))
print(person.keys())
print(person.items())

person.clear()

print(person) 

products = [
    {"name" : 'book', "price" : 10.99},
    {"name" : 'laptop', "price" : 1000}
]
print(products)