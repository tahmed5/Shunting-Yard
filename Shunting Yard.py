data = '( x + y ) + z' .split()
print(data)
output_queue = []
operator_stack = []
# b = n/a i = 5 d = 4 m = 3 a = 2 s = 1
op_data = {'^': [5 ,'right'] , '/': [4 , 'left'] ,'*': [3, 'left'] ,'+': [2 , 'left'] , '-': [1, 'left']}

## https://en.wikipedia.org/wiki/Shunting-yard_algorithm

#while there are tokens to be read:
#    read a token.
#    if the token is a number, then:
#        push it to the output queue.
#    if the token is a function then:
#        push it onto the operator stack 
#    if the token is an operator, then:
#        while ((there is a function at the top of the operator stack)
#               or (there is an operator at the top of the operator stack with greater precedence)
#               or (the operator at the top of the operator stack has equal precedence and is left associative))
#              and (the operator at the top of the operator stack is not a left bracket):
#            pop operators from the operator stack onto the output queue.
#        push it onto the operator stack.
#    if the token is a left bracket (i.e. "("), then:
#        push it onto the operator stack.
#    if the token is a right bracket (i.e. ")"), then:
#        while the operator at the top of the operator stack is not a left bracket:
#            pop the operator from the operator stack onto the output queue.
#        pop the left bracket from the stack.
#        /* if the stack runs out without finding a left bracket, then there are mismatched parentheses. */
#if there are no more tokens to read:
#    while there are still operator tokens on the stack:
#        /* if the operator token on the top of the stack is a bracket, then there are mismatched parentheses. */
#        pop the operator from the operator stack onto the output queue.
        
def precedence(operator):
    try:
        return op_data[operator][0]
    except:
        return 0

def assoc(operator):
    try:
        return op_data[operator][1]
    except:
        return 0

def peek(stack):
    try:
        top = stack[-1]
    except:
        top = 0

    return top 


    


while data:
    for token in data:
        try:
            if int(token):
                output_queue.append(token)
        except:
            while (precedence(peek(operator_stack)) > precedence(token)) or (precedence(peek(operator_stack)) == precedence(token) and assoc(token) == 'left') and (peek(operator_stack) != '('):

                for x in range(len(operator_stack)):
                    output_queue.append(operator_stack.pop())
            print('De Token' , token)
            operator_stack.append(token)

        if token == '(':
            operator_stack.append(token)
        print('CHECK')

        print(operator_stack)
        print(output_queue)

        if token == ')':
            try:                  
                while peek(operator_stack) != '(':
                    output_queue.append(operator_stack.pop())
            except:
                print(' mismatched parentheses ' )
                print(operator_stack)
                print(output_queue)
                quit()
            operator_stack.pop()
while len(operator_stack) != 0:
    if peek(operator_stack) == '(' or peek(operator_stack) == ')':
        print(' mismathced parentheses ' )
        print(operator_stack)
        print(output_queue)
        quit()
    output_queue.appened(operator_stack.pop())


            



            
        



