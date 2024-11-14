# outputs the current temperature of the given citys name (url)
# Made by Kerem Ceylan
# Dev Note: 
# Maybe I'll add a loop which will update the values after for example every 10 mins.
# And also make an input for choosing the location by only entering the name of the city.

import requests
from datetime import datetime

# Get today's date
raw_today = str(datetime.today())
# formate the String
today = raw_today[8:10] +"."+ raw_today[5:7] +"."+ raw_today[0:4]

# Print today's date
print("Today's date:", today)

# Weather Website: https://at.wetter.com
# ONLY PUT IN THE LINK FROM THIS SITE OR ELSE IT WON'T WORK
# simply select a location and copy paste the link in the url variable between the quotation marks ""

# idea with cmd: start \\website.com 

try:
    #------------------------------------------------------------------#
    url = "https://at.wetter.com/oesterreich/st-poelten/ATAT10590.html" 
    #------------------------------------------------------------------#
    response = requests.get(url)
    # if the URL does not exist or something like that: error message
except:
    print("An Error occured, try again later.")
    exit()




numbers = []
counter = 0
for i in "1234567890":
    numbers.append(str(counter))
    counter += 1

if response.status_code == 200:
    html_content = str(response.content)
    # shows if delta rtw_temp is in the websites src code
    if "swg-text-large" not in html_content:
        print("'swg-text-large' could not be found!")
        exit()
    # position of the line
    weather_index = html_content.index("swg-text-large")
    

    
    b = ""
    if html_content[weather_index+16] in numbers and html_content[weather_index+17] in numbers:
        degree1 = html_content[weather_index+16]
        degree2 = html_content[weather_index+17]
        a = degree1
        b = degree2
    else:
        degree1 = html_content.index(html_content[weather_index+16])
        a = html_content[degree1]

    result = a+b

    # result is the temperature
    result = int(result)

    # outputs
    if result < 10:
        print("it's really cold!")
    elif result > 10 and result < 20:
        print("very refreshing!")
    elif result > 20 and result < 30:
        print("it's getting warmer!")
    else:
        print("it's really hot")
    print(f"current temperature: {result}°C")
else:
    # if some kind of error happenens while trying to access the website then this will be outputted 
    print("Failed to fetch the website.")