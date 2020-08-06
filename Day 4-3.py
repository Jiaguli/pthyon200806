d={}

import os.path

def menu ():
    print('1.輸入成績')
    print('2.列出所有成績')
    print('3.成績查詢')
    print('4.離開')
    n=input("Your ans:")
    return n
print('welcome')

if os.path.isfile('score.txt'):
    print('old file')
    file=open('score.txt','r')
else:
    print('new file') 
    file=open('score.txt','w')

#for row in score.readline():
    

print('##################')
n=menu()

print('##################')
n=int(n)
while n!=4:
    while n == 1:
        name=input('請輸入你的名字')
        s=input('請輸入你的分數')
        file=open('score.txt','a')
        file.write(name)
        file.write(':')
        file.write(s)
        file.write('\n')
        file.close()
        d[name]=(s)
        YN=input('是否要繼續，要請按1，不要請按0:')
        if YN=='0':
            n=menu()
            break    
    while n==2:
        for w in d.keys():            
            print(w)
        n = menu()
        break
    while n==3:
        a=input('請輸入你的名字:')
        a=str(a)
        if a in d:
            ans = d[a]
            print(ans)
        else:
            print('沒有這項成績')
        n=menu()
        break
print('謝謝')
   
    

      