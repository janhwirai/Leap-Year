def is_leap(year):
    leap = False
    if (year % 100 == 0) and (year %400 != 0):
        leap = False
    elif (year % 4 == 0):
        leap = True
    return leap
year = int(input("Enter year: "))
if(is_leap(year)):
    print("\nIt's a Leap Year!")
else:
    print("\nIt's not a Leap Year!")