  
x=2
num=input('請輸入一個數字')
print('他的因數有：')
print('1')
while int(x)!=int(num):
    if int(num)%int(x)==0:
        print(x)
        x=int(x)+1
    else:
        x=int(x)+1
print(x)
