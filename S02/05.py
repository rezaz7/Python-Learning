a=float(input('First Number = '))
b=float(input('Second Number = '))
c=str(input('Operator = '))

if (a!=0) and (b!=0):
    print('Problem')
    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)
    elif c=='~':
        print(a**b)    
else:
    print('Invalid')
    