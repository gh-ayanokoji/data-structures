total = int(input("Enter the no. of books: "))
books = []
for i in range(total):
    cost = int(input("Enter the cost of book: "))
    books.append(cost)

print(books)

def delDup(books):
    noDup = []
    for item in books:
        if item not in noDup:
            noDup.append(item)
    return noDup

def ascending(books):
    books.sort()
    return books

    
def costly(books):
    count = 0
    for item in books:
        if item > 500:
            count+=1

    return count

def lessCost(books):
    newList = []
    for item in books:
        if item < 500:
            newList.append(item)

    return newList

print(f"Books without duplicate entries is {delDup(books)}")
print(f"Books in ascending order is {ascending(books)}")
print(f"{costly(books)} no. of books cost more than 500")
print(f"Books costing less than 500 are {lessCost(books)}")

