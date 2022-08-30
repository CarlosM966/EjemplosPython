listaEst = []
resp = "Si"
while(resp.upper() != "No"):
    tam = len(listaEst)
    print("Elemetos guardados: ", tam)
    nombres = input("Escriba el nombre desl estudiante: ")
    listaEst.append(nombres)
    resp = input("Desea agregar otro? SI - NO ")
    
for est in listaEst:
    print(est)