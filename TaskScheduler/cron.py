# Algorithm: 
# Compare the time entered by user with current time and send the email, if in case it matches

currentDateAndTime = datetime.now()
# date = date.split('T')            ===> Key in cachedListOfEmail
# min = int(date[1].split(':')[1])  ===> minutes in cachedListOfEmail
# hrs = int(date[1].split(':')[0])  ===> hours in cachedListOfEmail
dateToday = str(currentDateAndTime).split(' ')[0]

dateToday, currentDateAndTime.hour, currentDateAndTime.minute # Date and time at this moment

# Compare the current data and time with cachedListOfEmail and call schedule API