def leap_year(year):
        if year < 1582:
            return False
        if year % 4 !=0:
            return False
        if year % 100 !=0:
            return True
        if year % 400 !=0:
            return False
        return True
print("Leap Year =", leap_year(int(input("Enter a year: ",))))