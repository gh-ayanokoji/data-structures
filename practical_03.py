total = int(input("Enter the no. of books: "))
books = {}
for i in range(total):
    book = input("Enter the name of book: ")
    cost = int(input("Enter the cost of book: "))
    books[book] = cost

print(books)

def delDup(books):
    noDup = {}
    for item in books:
        if item not in noDup:
            noDup[item] = books[item]
    return noDup

def ascending(books):
    asc = {}
    for item in books:
        for i in books.values():
            for j in books.values():
                if i < j:
                    if i not in books.values():
                        asc[item] = books[item]

    return asc

    
def costly(books):
    pass

print(f"Books without duplicate entries is {delDup(books)}")
print(f"Books in ascending order is {ascending(books)}")

