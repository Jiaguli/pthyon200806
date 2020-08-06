file=open('2020.jpg','rb')
nice=file.read()
file.close()

file=open('複製.jpg','wb')
file.write(nice)
file.close()