def divide(a, b):
    divisor = a
    dividend = b
    ans = 0
    while(divisor >= dividend):
        divisor -= dividend
        ans += 1
    return ans

def getCities():
    cities = []
    city = input("Enter the name of a city: ")
    while (city != ""):
        cities.append(city)
        city = input("Enter the name of a city: ")
    return cities

#break works as expected
#continue skips the rest of the iteration and continues the loop from there
