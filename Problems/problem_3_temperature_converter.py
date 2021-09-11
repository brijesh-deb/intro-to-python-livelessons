"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_f=input("Enter temp in Fahrenheit: ")

# Calculate it in Celsius
temp_c= (int(temp_f)-32)*(5/9)

# Tell the user what it is
print("Calciuse temp: "+str(temp_c))