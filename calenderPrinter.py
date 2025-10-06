
    #take user input: number of days in month
days_in_month = int(input("How many days are in the month? "))

    #take user input: day the month starts on
first_day = int(input("What day of the week does the month start on? (Sun=1, Monday=2, ... Sat= 7) "))

 # function to print calendar
def calender_printer(days_in_month, first_day):

    calender_title = ["S", "M" , "T", "W", "T", "F", "S"]
    print("  ".join(calender_title)) 

         #makes spaces based on first day of month
    for i in range(first_day-1):
        print("   ", end="") # end = "" ensure it prints on same line

        #takes number of days in the month
    for i in range(1, days_in_month+1): 
        print(f"{i:2}", end=" ") 

             #new line after every 7th day (including spaces)
        if (i + first_day - 1) % 7 == 0:
            print()  # newline

#calls function
calender_printer(days_in_month, first_day)