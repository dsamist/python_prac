#this is a simple program that converts celcius to fahrenheit

#formula for converting celcius to fahrenheit is (0°C × 9/5) + 32 = 32°F

#request user to input the temperature in celcius
#create a fuction that converts celcius to fahrenheit
def celcius_to_fah(input):
    celcius = (input * 9/5) + 32
    return celcius

user_input = float(input("Enter the temperature in celcius:"))

# print("The temperature in fahrenheit is " + str(celcius_to_fah(user_input)) + "°F")

print("The temperature in fahrenheit is " + str(celcius_to_fah(user_input)) + "°F")
