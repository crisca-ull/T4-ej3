#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

def ordeninverso():
    i=100
    while i>0:
        yield i
        i-=1

for i in ordeninverso():
    print(i)