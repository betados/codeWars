def calc(expr):
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
        print(chain, i)
        if chain[i] not in operators:
            continue
        if i==1:
            chain.pop(i)
            chain.pop(i-1)
            i = -1
            continue
        last = operatorsDict[ chain[i] ](int(chain[i-2]), int(chain[i-1]))
        chain[i-1] = last
        chain.pop(i-2)
        i = -1
        print('pop:' ,chain)
    return last
            
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
        
        
