# Write a program in Python to check if a number is binary?
n=int(input('Enter Any Number to check\n'))
if n<=1:
    print('binary value')
if n>1:
    while n>0:
        n=n%10
        if n!=0 and n!=1:
            print('not a binary value')
            break
        n=n//10
        if n==0:
            print('binary value')