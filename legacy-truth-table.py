# A program that generates a truth table for valid logical statements, with up to 3 parameters

def truth_table():
    logic_statement = input("Insert a valid statement, in parameters A, B and C: ")
    
    # If the statement has no parameters, it will be evaluated
    try:
        answer = eval(logic_statement)
        print(answer)
        return answer
    except:
        print('Logic statement contains parameters')
    
    try:
        bool_pool  = (True, False)
        
        text = "| A = {} | B = {} | C = {}  | \"{}\" = {} |"
        
        for truth in bool_pool:
            A = truth
            for truth in bool_pool:
                B = truth
                for truth in bool_pool:
                    C = truth
                    answer = eval(logic_statement)
                    parameters = (A, B, C)
                    T = "True " # True padded
                    if A == True:
                         A = T
                    if B == True:
                        B = T
                    if C == True:
                        C = T
                    if answer == True:
                        answer = T
                    output = text.format(A, B, C, logic_statement, answer)
                    print(output)
        return answer
   
   # Notice there is spurious output if B and C aren't used

    except:
        print("Please only use A, B and C as paramters.")
        return None

truth_table()
