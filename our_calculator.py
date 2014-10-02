import arithmetic


def validation_loop(operator, token_len):
    if len(tokens) == token_len:
        print operator(user_firstnumber, user_secondnumber)
    else:
        print "Please enter a valid calculation."


def validation_loop_for_square(operator, token_len):
    if len(tokens) == token_len:
        print operator(user_firstnumber)
    else:
        print "Please enter a valid calculation."

print "Hello and welcome to our calculator."



while True:
    user_calculation = raw_input("Enter calculation, type q to quit > ")
    tokens = user_calculation.split(" ")
    
    if tokens[0] == "q":
        break

    #if tokens[0] != ("+" or "-" or  "*" or "/" or "pow" or "square" or "cube" or "mod" or  "q"):
        #print "Please enter a valid operator."
        #continue

    #tokens[1].isdigit
    #tokens[2].isdigit



    user_firstnumber = float(tokens[1])
    if len(tokens) > 2:
        user_secondnumber = float(tokens[2])
    
    if tokens[0] == "pow":

       validation_loop(arithmetic.power, 3)

    elif tokens[0] == "mod":
     
        validation_loop(arithmetic.mod, 3)

    elif tokens[0] == "+":
        
        validation_loop(arithmetic.add, 3)

    elif tokens[0] == "-":
        
        validation_loop(arithmetic.subtract, 3)
    
    elif tokens[0] == "/":
        
        validation_loop(arithmetic.divide, 3)
    
    elif tokens[0] == "*":

        validation_loop(arithmetic.multiply, 3)

    elif tokens[0] == "square":
        
        validation_loop_for_square(arithmetic.square, 2)

    elif tokens[0] == "cube":
        
        validation_loop_for_square(arithmetic.cube, 2)
    else:
        print "Please enter a valid calculation."

