num=input('請輸入一個數字')
x=2
if int(num)<2:
    print('他不是質數也不是合數')
else:
    while int(num)%int(x)!=0:
        x=int(x)+1
    if int(x)==int(num):
        print('他是質數')
    else:
        print('他是合數')