def calc(expr):
    print(expr)
    if len(expr) == 0:
        return 0
    
    operators = ['+', '-', '*', '/']
    names = [add, sub, mult, div]
    operatorsDict = dict((operators[i], names[i]) for i in range(4))
    
    chain = expr.split(' ')
    i = -1
    try:
        last = float(chain[-1])
    except:
        pass
    while i < len(chain)-1 and len(chain)>0:
        i += 1
        # print(chain, i)
        if chain[i] not in operators:
            continue
        if i==1:
            chain.pop(i)
            # chain.pop(i-1)
            i = -1
            continue
        # print(chain[i-2] , chain[i-1])
        print(chain)
        last = operatorsDict[ chain[i] ](float(chain[i-2]), float(chain[i-1]))
        chain[i-1] = last
        chain.pop(i)
        chain.pop(i-2)
        i = -1
        # print('pop:' ,chain)
    print(last)
    return last
            
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
        
        
