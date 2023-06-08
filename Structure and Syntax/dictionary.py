#key-value pairs
monthConversions ={
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConversions["Nov"]) #method 1
print(monthConversions.get("Sep")) #method 2
print(monthConversions.get("step","Not a valid key")) #default value