n=int(input('enter a number to reverse\n'))
num=0
def rever(n):
        global num
        res=n%10
        res1 = n // 10
        n=res1
        num=num*10 + res
        if n==0:
            return num
        return rever(n)
xcv=rever(n)
print('reverse of entered number is =',xcv)
