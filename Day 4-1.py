import os.path

if os.path.isfile('myfile.txt'):
    print('存在')
else:
    print('不存在')

#file=open('myfile.txt','w')
#file.write('hi')

file=open('myfile.txt','r')
nnn = file.read()
print(nnn)

file=open('myfile.txt','a')
file.write(',Jiaguli.')

file.close()