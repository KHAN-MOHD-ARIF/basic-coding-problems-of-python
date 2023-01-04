# write a programe to convert decimal to binary:
n=int(input('Enter any decimal\n'))
r=[]
def binary(n):
    c=0
    while n>0:
        k=n%2
        v=str(k)
        l=n//2
        n=l
        c += 1
        r.append(v)
    size=r[::-1]
    d=' '.join(size)
    return d
deci_to_binary=binary(n)
print('binary of given decimal is =',deci_to_binary)
