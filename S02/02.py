a=[]
i=int(input('Enter Number = '))
while i>0:
    a.append(int(input('{} Number = '.format(i))))
    i=i-1
a.sort()
print(a)


