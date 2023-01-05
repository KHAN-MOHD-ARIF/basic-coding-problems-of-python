# Write a program in Python to find sum of digits of a number using recursion?
n=int(input('enter the number \n'))
def sum_of_digit(n):
    global sum
    k=n%10
    n=n//10
    sum+=k
    if n==0:
        return sum
    return sum_of_digit(n)
sum=0
digits=sum_of_digit(n)
print(f'sum of the digits of {n} is ',digits)
