#Sumar los elementos de un areglo
arreglo = []
cant = int(input("Cuantos #:"))
cont = 0
while (cont < cant):
    num = int(input("DIME UN #: "))
    arreglo.append(num)
    cont+=1
    
suma = 0
for num in arreglo:
    suma += num
print("La suma es: ", suma)
print("lA SUMA CON LA FUNCION SUMA: ",suma(arreglo))