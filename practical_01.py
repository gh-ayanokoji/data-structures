cricket = set()
badminton = set()
football = set()

cric_st = int(input("enter the no. of students playing cricket: "))
for i in range(cric_st):
    roll = int(input("Enter the roll no. of student: "))
    if roll not in cricket:
        cricket.add(roll)
    else:
        pass

bad_st = int(input("enter the no. of students playing badminton: "))
for i in range(bad_st):
    roll = int(input("Enter the roll no. of student: "))
    if roll not in badminton:
        badminton.add(roll)
    else:
        pass

foot_st = int(input("enter the no. of students playing football: "))
for i in range(foot_st):
    roll = int(input("Enter the roll no. of student: "))
    if roll not in football:
        football.add(roll)
    else:
        pass


def cricNBad(cricket, badminton):
    cnb = cricket.intersection(badminton)
    return cnb


def notBothCnb(cricket, badminton):
    ncnb = cricket.symmetric_difference(badminton)
    return ncnb


def neitherCNB(football, cricket, badminton):
    f1= football.difference(cricket)
    f2 = football.difference(badminton)
    return f1.intersection(f2)


def fNCnotBad(football, cricket, badminton):
    fnc = football.union(cricket)
    return fnc.difference(badminton)


print(f"Roll no. of students that play both cricket and badminton are: {cricNBad(cricket, badminton)}")
print(f"Roll no. of students that play either cricket and badminton but not both are: {notBothCnb(cricket, badminton)}")
print(f"Roll no. of students that play neither cricket nor badminton are: {neitherCNB(football, cricket, badminton)}")
print(f"Roll no. of students that play both cricket and football but no badminton are: {fNCnotBad(football, cricket, badminton)}")
