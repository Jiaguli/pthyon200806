n=0
ans=1


while int(n)!=10:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Please choose one service')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.平方')
    print('6.階乘')
    print('7.判斷質數')
    print('8.列出因數')
    print('9.因數分解')
    
    print('10.Finish')
    num=input("Your ans:")
    n=int(num)
    
    if n==1:
        a=input('輸入第一個數字')
        b=input('輸入第二個數字')
        ans=int(a)+int(b)
        print('The ans is',ans)
        
    elif n==2:
        a=input('輸入第一個數字')
        b=input('輸入第二個數字')
        ans = int(a)-int(b)
        print('The ans is',ans)
        
    elif n==3:
        a=input('輸入被乘數')
        b=input('輸入乘數')
        ans=int(a)*int(b)
        print('The ans is',ans)
        
    elif n==4:
        a=input('輸入被除數')
        b=input('輸入除數')
        ans=int(a)/int(b)
        print('The ans is',ans)
        
    elif n==5:
        a=input('輸入數字')
        b=input('輸入指數')
        b=int(b)+1
        for z in range(1,b,1):
            ans=int(ans)*int(a)
        print('The ans is',ans)
            
    elif n==6:
        a=input('輸入數字')
        a=int(a)+1
        for a in range(1,a,1):
            ans=int(ans)*int(a)
        print('The ans is',ans)
            
    elif n==7:
        a=input('請輸入一個數字')
        x=2
        if int(num)<2:
            print('他不是質數也不是合數')
        else:
            while int(a)%int(x)!=0:
                x=int(x)+1
            if int(x)==int(a):
                print('他是質數')
            else:
                print('他是合數')

    elif n==8:
        x=2
        a=input('請輸入一個數字')
        print('他的因數有：')
        print('1')
        while int(x)!=int(a):
            if int(a)%int(x)==0:
                print(x)
                x=int(x)+1
            else:
                x=int(x)+1
        print(x)

    elif n==9:
        





    else:
        print('謝謝使用')
        n=10