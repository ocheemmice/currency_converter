#Take user input
#input function to take user input
amount = input("Enter amount: ")

#convert the amount input data to float
amount_type_convert = float(amount)

#Conversion rate for Dollar to Naira
rate = 1400.0

def multiply():
    return amount_type_convert * rate
print (multiply())