monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"]) #print the value of the key "Nov"
print(monthConversions.get("Dec")) #print the value of the key "Dec"
print(monthConversions.get("Luv", "Not a valid key")) #print the value of the key "Luv", if the key does not exist, print "Not a valid key"