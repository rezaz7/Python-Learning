a=float(input('First Number = '))
b=float(input('Second Number = '))
c=str(input('Operator = '))

if c=='+':
    print(a+b)
elif c=='-':
        print(a-b)
elif c=='*':
        print(a*b)
elif c=='/':
    if (a!=0) or (b!=0):
        print('Problem = 00')
    else:
        print(a/b)
elif c=='^':
        print(a**b)    
else:
    print('Invalid')
    