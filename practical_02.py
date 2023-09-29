total = int(input("Enter total no. of students: "))
students = []
for i in range(total):
    marks = int(input("Enter the marks of student: "))
    students.append(marks)


def average(students):
    return sum(students) / len(students)


def highLow(students):
    print("Highest score of class is:", max(students))
    print("Lowest score of class is: ", min(students))


def absent(students):
    return students.count(0)


def maxFreq(students):
    maxFr = 0
    for item in students:
        temp = students.count(item)
        if temp > maxFr:
            maxFr = temp
            frMark = item
        else:
            pass

    print(f"The Marks with highest frequency is {frMark} and the frequency is {maxFr}")


print(f"Average marks of class is {average(students)}")
highLow(students)
print(f"No. of students who were absent are {absent(students)}")
maxFreq(students)
