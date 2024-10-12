a_mile = 1609.344   #meters
a_gallon = 3.785411784 #liters

def liters_100km_to_miles_gallon(liters):
    gallon=liters/a_gallon
    miles = 100000/a_mile
    return miles/gallon



def miles_gallon_to_liters_100km(miles):
    hundred_km= (miles*a_mile)/100000
    liters = a_gallon
    return (liters/hundred_km)

print(liters_100km_to_miles_gallon(3.9))    #60.31143162393162
print(liters_100km_to_miles_gallon(7.5))    #31.36194444444444
print(liters_100km_to_miles_gallon(10.))    #23.52145833333333
print(miles_gallon_to_liters_100km(60.3))   #3.9007393587617467
print(miles_gallon_to_liters_100km(31.4))   #7.490910297239916
print(miles_gallon_to_liters_100km(23.5))   #10.009131205673757