aaa=open('book.txt','w')
aaa.write(' ')
n=1

a=input('請輸入一個數字')
b=int(a)+1
for x in range(2,b,1):
    if int(a)%int(x)==0 and int(a)!=1:
        aaa=open('book.txt','a')
        aaa.write('*')
        w=str(x)
        aaa.write(w)
        a=int(a)/x
        aaa.close()
    else:
        x=int(x)
aaa=open('book.txt','r')
aaa.read()
print(aaa)
aaa.close()