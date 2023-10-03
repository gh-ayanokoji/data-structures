bankAc = 0

def deposit(bankAc, depo):
    bankAc = bankAc + depo

def withdraw(bankAc, wd):
    if bankAc - wd < 0:
        print(f"Your account does not have enough balance to withdraw Rs.{wd}")