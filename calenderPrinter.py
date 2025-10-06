
import numpy as np
days_in_month = int(input("How many days are in the month? "))
first_day = int(input("What day of the week does the month start on? (Sun=0, Monday=1, ... Sat= 6) "))

def calender_printer(days_in_month, first_day):

    calender_title = np.array(["Sun", "Mon" , "Tue", "Wed", "Thur", "Fri", "Sat"])

    for i in range(first_day):
        print(" ", end = "") #ensure it prints on same line

    return calender_title
#print_gaps based on the day user selected

