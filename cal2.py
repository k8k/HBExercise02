import arithmetic

print "Hello and welcome to our calculator."



while True:
    user_calculation = raw_input("Enter calculation, type q to quit > ")
    tokens = user_calculation.split(" ")
    
    if tokens[0] == "q":
        break
    
    if tokens[0] == "pow":
        print arithmetic.power(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "mod":
        print arithmetic.mod(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "+":
        print arithmetic.add(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "-":
        print arithmetic.subtract(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "/":
        print arithmetic.divide(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "*":
        print arithmetic.multiply(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "square":
        print arithmetic.square(float(tokens[1]))
    elif tokens[0] == "cube":
        print arithmetic.cube(float(tokens[1]))
    else:
        print "Please enter a valid calculation."




