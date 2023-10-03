total = int(input("Enter the no. of books: "))
books = []

for i in range(total):
    title = input("Enter the name of book: ")
    cost = int(input("Enter the cost of book: "))
    temp = [title, cost]
    books.append(temp)

def delDup(books):
    noDup = []
    for book in books:
        if book not in noDup:
            noDup.append(book)
    print("\nBooks without duplicate entries are:\n")
    for book in noDup:
        print(f"Title: {book[0]}, Cost: {book[1]}")

def ascending(books):
    cost = []
    asc = []
    for i in range(len(books)):
        cost.append(books[i][1])
    cost.sort()
    for i in range(len(cost)):
        for book in books:
            if cost[i] == book[1]:
                if book not in asc:
                    asc.append(book)
    print("\nBooks in ascending order are:\n")
    for book in asc:
        print(f"Title: {book[0]}, Cost: {book[1]}")
         
def costly(books):
    count = 0
    for book in books:
        if book[1] > 500:
            count+=1
    return count

def lessCost(books):
    newList = []
    for book in books:
        if book[1] < 500:
            newList.append(book)
    print("\nBooks costing less than 500 are:\n")
    for book in newList:
        print(f"Title: {book[0]}, Cost: {book[1]}")

delDup(books)
ascending(books)
print(f"\n{costly(books)} books cost more than 500")
lessCost(books)

