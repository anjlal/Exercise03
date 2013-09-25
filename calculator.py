# Created by Angie Lal and Ingrid Avendano on 9/25/13.
import arithmetic

# operations taking in one input
def operation1(tokens):
    operator = tokens[0]
    num  = int(tokens[1])

    if operator == "square":
        result = arithmetic.square(num)
    else:
        result = arithmetic.cube(num)

    print result


# operations that take two inputs
def operation2(tokens):
    operator = tokens[0]
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if operator == "pow":
        result = arithmetic.power(num1, num2)
    elif operator == "mod":
        result = arithmetic.mod(num1, num2)
    else:
        result = arithmetic.divide(num1, num2)

    print result


# operations that take in three or more inputs
def operation3(tokens):
    operator = tokens[0]

    if operator == "+":
        result = arithmetic.add(tokens[1:])
    elif operator == "-":
        result = arithmetic.subtract(tokens[1:])
    else:
        result = arithmetic.multiply(tokens[1:])

    print result


# checks to make sure all the inputs are integers
def validate_operands(tokens):
    for i in range(len(tokens[1:])):
        try:
            tokens[i+1] = int(tokens[i+1])
        except:
            return False

    return True


def convert_to_ints(tokens):
    for i in range(len(tokens[1:])):
        tokens[i+1] = int(tokens[i+1])
    return tokens


def validate_input(tokens):
    operator = tokens[0]
    token_len = len(tokens)

    if operator and operator in ["+", "-", "*","/", "pow", "mod","square", "cube"] and len(tokens) >= 2:

        # returns two outputs, a boolean stating whether a new list has valid
        # operators and a new list of tokens that have integers now
        if validate_operands(tokens):
            integer_tokens = convert_to_ints(tokens)

            # check number of tokens
            if token_len == 2 and operator in ["square", "cube"]:  
                operation1(integer_tokens)
            elif token_len == 3 and operator in ["/", "pow", "mod"]:
                operation2(integer_tokens)
            elif token_len >= 3 and operator in ["+", "-", "*"]:
                operation3(integer_tokens)
            else:
                print "Invalid number of arguments provided."
                
        else: 
            print "Invalid operands."

    else:
        print "Invalid operation."



def main():

    # continually allow the user to enter input(s) until they want to quit (q)
    input = raw_input("> ")

    while input is not "q":
        tokens = input.split(" ")
        validate_input(tokens)
        input = raw_input("> ")     

    # end of function
    exit()

main()