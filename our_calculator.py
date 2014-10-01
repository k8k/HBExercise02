import arithmetic

print "Hello and welcome to our calculator."



while True:
    user_calculation = raw_input("Enter calculation, type q to quit > ")
    tokens = user_calculation.split(" ")
    
    if tokens[0] == "q":
        break

    user_firstnumber = float(tokens[1])
    
    if len(tokens) > 2:
        user_secondnumber = float(tokens[2])
    
    if tokens[0] == "pow":
        print arithmetic.power(user_firstnumber, user_secondnumber)
    elif tokens[0] == "mod":
        print arithmetic.mod(user_firstnumber, user_secondnumber)
    elif tokens[0] == "+":
        print arithmetic.add(user_firstnumber, user_secondnumber)
    elif tokens[0] == "-":
        print arithmetic.subtract(user_firstnumber, user_secondnumber)
    elif tokens[0] == "/":
        print arithmetic.divide(user_firstnumber, user_secondnumber)
    elif tokens[0] == "*":
        print arithmetic.multiply(user_firstnumber, user_secondnumber)
    elif tokens[0] == "square":
        print arithmetic.square(user_firstnumber)
    elif tokens[0] == "cube":
        print arithmetic.cube(user_firstnumber)
    else:
        print "Please enter a valid calculation."




