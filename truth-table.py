# A program that generates a truth table for valid logical statements, with up to 3 parameters

def truth_table():
    logic_statement = input("Insert a valid statement, in parameters A, B and C: ")
    # For example 'A is true if B is false'


    try:
        answer = eval(logic_statement)  # if the statement has no parameters, it will be evaluated
        print(answer)
        return answer
    except:
        print('Logic statement contains parameters')

    split_logic = str(logic_statement).split()  # scrubs the input for parameters
    parameters = []
    for i in split_logic:
        if len(i) == 1:
            parameters.append(i)
    print(parameters)

    times = len(parameters)
    total = 0

    while times <= total:
        total += 1

    for parameter in parameters:
        print(parameter)
        parameter = True
        print(parameter)
        for parameter in parameter
            print(eval(logic_statement))  # does not work




   # def true_loop():
   #     for parameter in parameters:
   #         print(parameter)
   #
   # for parameter in parameters:
   #     i = 0
   #     while i < len(parameters):  # continues until the end of the list
   #         true_loop()
   #         i += 1





#        bool_pool  = (True, False)
#        text = "| A = {} | B = {} | C = {}  | \"{}\" = {} |"
#        for truth in bool_pool:
#            A = truth
#            for truth in bool_pool:
#                B = truth
#                for truth in bool_pool:
#                    C = truth
#                    answer = eval(logic_statement)
#                    parameters = (A, B, C)
#                    output = text.format(A, B, C, logic_statement, answer)
#                    print(output)
   
   # Notice there is spurious output if B and C aren't used

truth_table()
