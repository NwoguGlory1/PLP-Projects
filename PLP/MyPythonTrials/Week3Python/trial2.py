#Create a function named large_power() that takes two parameters named base and exponent.

# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    #using inbuilt pow(base, exp, mod=None)
    result = pow(base, exponent)
    if result > 5000:
        return True
    else:
        return False
    
    #more efficient way:
    #def large_power(base, exponent):
    # return pow(base, exponent) > 5000