#Create a dictionary whose key are moyh name and value is no. of day in  corresponding months.
# *ask user to enter a month  and dictionary to tell them how many days in month
# *print out all key in alphabetically order
# *print out all month have 31 day 
#* print out the key value pair sorted by no of day in month
def no_of_day(d1):
    month =input("Enter a month name to check no of days:")
    if month in d1: print(f"the no of day in {month} is {d1[month]}")
    else:           print("You enter a wrong month")

def print_key(d1):
    sort_month = sorted(d1.keys())
    print("\nPrinting month in alphabetical order:")
    for i in sort_month:
        print(i)

def month_of31(d1):
    print("\nMonth of 31 day:")
    for k,v in d1.items():
        if  v== 31:
            print(k)

        

def order_by_value(d1):
    print("\nMonth sorted by number of day:")
    sorted_mon = sorted(d1.items())
    for mon, day in sorted_mon:
        print(f"{mon}:{day} days")
    
    


dict1 = {"january":31,"february":28, "march":31,"april":30,"may":31,"june":30,"july":31,
        "august":31,"september":30,"october":31,"november":30,"december":31 }

no_of_day(dict1)
print_key(dict1)
month_of31(dict1)
order_by_value(dict1)


       