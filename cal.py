first= input('enter the first number')
second= input('enter the seccond number')
first=int(first)
second= int(second)
print('choose the operator +,-./,* ...')
operator=input("enter the operator")
if operator=='+':
    print('sum=',first+second)
elif operator=='-':
    print('difference=',first-second)
elif operator=='/':
    print('division=',first/second)
elif operator=='*':
    print('multiplication=',first*second)
else:
    print('invalid operation')
