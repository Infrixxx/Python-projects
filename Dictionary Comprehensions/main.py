# dictionary comprehension =    create a dictionary using an expression
#                               can replace for loops and certain lambda functions
#
#dictionary = {key: expression for (key, value) in iterable}

#cities_in_F= {'New York' : 32, "Boston ":75, 'Los Angeles':100, 'Chicago':50}

#This will create a new dicitionary in degrees celcius
#cities_in_c ={key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_c)


#_________________________________________________________________________
#dictionary={key: expression for (key, value) in iterable if conditional}

#weather= {'New York' : "snowing", "Boston ":"sunny", 'Los Angeles':"sunny", 'Chicago':"cloud"}
#sunny_weather= {key: value for (key,value) in weather.items() if value=="sunny"}
#print(sunny_weather)

#_________________________________________________________________________
#dictionary = {key: (if/else) for (key, value) in iterable}
#cities_in_F= {'New York' : 32, "Boston ":75, 'Los Angeles':100, 'Chicago':50}
#desc_cities={key: ("WARM" if value>=40 else "COLD") for (key, value) in cities_in_F.items()}
#print(desc_cities)

#_________________________________________________________________________
#dictionary = {key: function(value) for (key,value) in iterable}

#def check_temp(value):
#    if value>=70:
#        return "HOT"
#    elif 69>=value >=40:
#        return "WARM"
#    else:
#        return "COLD"

#cities_in_F= {'New York' : 32, "Boston ":75, 'Los Angeles':100, 'Chicago':50}
#desc_cities={key: check_temp(value) for (key, value) in cities_in_F.items()}

#print(desc_cities)