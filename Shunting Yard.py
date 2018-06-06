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
    return op_data[operator][0]

def assoc(opertaor):
    return op_data[operator][1]
                                  
while data:
    for token in data:
        try:
            if int(token):
                output_queue.append(token)
        except:
            while (precedence(operator_stack.peek()) > precedence(token)) or (precedence(operator_stack.peek()) == precedence(token) and assoc(token) == 'left') and (operator_stack.peek() != '('):
                for x in len(operator_stack):
                    output_queue.append(operator_stack.pop(0))
            operator_stack.append(token)



            
            





