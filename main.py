import os
import csv

def main():
    month = ""
    day = 0
    date = 0
    size = 0

    CSV_PATH = os.path.join('budget_data(1).csv')

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open(CSV_PATH) as csvfile:
        file = csvfile.readlines()

    print("Which month (number) would you like to search for?")
    month = int(input(" >"))
    month = monthValidation(month)
    
    if month == "Jan" or month == "Feb":
        print("""Pick an available day:
              
1. 10th
2. 11th
3. 12th
4. 13th
5. 14th
6. 15th
7. 16th
8. 17th""")
        day = int(input(" >"))
        day = dayValidationSpecial(day)
    else:
        print("""Pick an available day:
              
1. 10th
2. 11th
3. 12th
4. 13th
5. 14th
6. 15th
7. 16th""")
        day = int(input(" >"))
        day = dayValidation(day)
    
    date = month+"-"+day
    size = len(file)

    serialSearch(file, size, date)

def monthValidation(m):
    while m < 1 or m > 12:
        print("Invalid number for month. Please try again.")
        m = int(input(" >"))
    if m == 1:
        m = "Jan"
    elif m == 2:
        m = "Feb"
    elif m == 3:
        m = "Mar"
    elif m == 4:
        m = "Apr"
    elif m == 5:
        m = "May"
    elif m == 6:
        m = "Jun"
    elif m == 7:
        m = "Jul"
    elif m == 8:
        m = "Aug"
    elif m == 9:
        m = "Sep"
    elif m == 10:
        m = "Oct"
    elif m == 11:
        m = "Nov"
    elif m == 12:
        m = "Dec"
    
    return m

def dayValidationSpecial(d):
    while d < 1 or d > 8:
        print("Invalid number for day. Please try again.")
        d = int(input(" >"))
    if d == 1:
        d = 10
    elif d == 2:
        d = 11
    elif d == 3:
        d = 12
    elif d == 4:
        d = 13
    elif d == 5:
        d = 14
    elif d == 6:
        d = 15
    elif d == 7:
        d = 16
    elif d == 8:
        d = 17

    return str(d)

def dayValidation(d):
    while d < 1 or d > 7:
        print("Invalid number for day. Please try again.")
        d = int(input(" >"))
    if d == 1:
        d = 10
    elif d == 2:
        d = 11
    elif d == 3:
        d = 12
    elif d == 4:
        d = 13
    elif d == 5:
        d = 14
    elif d == 6:
        d = 15
    elif d == 7:
        d = 16

    return str(d)

def serialSearch(file, size, date):
    first = 0
    result = ""

    while first < size + 1:
        if date in file[first]:
            result = file[first][7:]
            print(f"The profit/loss for the {date} is: ${result.rstrip("\n")}")
            break
        else:
            first += 1
        
    if result == "":
        print("Data not found.")

main()