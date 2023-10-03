arr = []
r = int(input("Enter no. of rows and columns: "))


# for i in range(r):
#     a = []
#     for j in range(r):
#         item = int(input("Enter an element of array: "))
#         a.append(item)

#     arr.append(a)

for i in range(r):
    for j in range(r):
        print(arr[i][j], end=" ")
    print( )
