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
    bad_tokens = 0

    for i in range(len(tokens[1:])):
        try:
            tokens[i+1] = int(tokens[i+1])
        except:
            bad_tokens += 1
            print "%s is a bad input!" % tokens[i+1]
            
    if bad_tokens > 0:
        return False
    else:
        return True


def convert_to_ints(tokens):
    for i in range(len(tokens[1:])):
        tokens[i+1] = int(tokens[i+1])
    return tokens


def validate_input(tokens):
    operator = tokens[0]
    token_len = len(tokens)

    if operator:
        if operator in ["+", "-", "*","/", "pow", "mod","square", "cube"]:
            if len(tokens) >= 2:

                # returns two outputs, a boolean stating whether a new list has valid
                # operators and a new list of tokens that have integers now
                if validate_operands(tokens):
                    integer_tokens = convert_to_ints(tokens)

                    if operator in ["square", "cube"]:
                        if token_len  == 2: 
                            operation1(integer_tokens)
                        else: 
                            print "Too many operands, only use one. [EX: cube 5]"
                    elif operator in ["/", "pow", "mod"]:
                        if token_len  == 3: 
                            operation2(integer_tokens)
                        elif token_len > 3: 
                            print "Too many operands, only use two. [EX: pow 3 6]"
                        elif token_len < 3:
                            print "Not enough operands, only use two. [EX: pow 3 6]"
                    elif operator in ["+", "-", "*"]:
                        if token_len  >= 3: 
                            operation3(integer_tokens)
                        else: 
                            print "Not enough operands, use two or more. [EX: add 3 6]"
                            
                    else:
                        print "You really screwed this up. >_>"
                else: 
                    print "Use integers only for arithmetic."

            else: 
                print "No operands. Needs integer(s) to calculate."
        else:
            print "Invalid operator used. Only use: '+', '-', '*','/', 'pow', 'mod', 'square', 'cube'"
    else:
        print "No operator and operation exists."



def main():
    # continually allow the user to enter input(s) until they want to quit (q)
    user_input = raw_input("> ")

    while user_input is not "q":
        tokens = user_input.split()
        validate_input(tokens)
        user_input = raw_input("> ")

main()