#Introducción al usuario
print("Ingrese 3 numeros para obtener su promedio.")
#Se crea lista con 3 elementos vacíos
lista = ["","",""]
# Bucle que pide 3 numeros
for i in range(0,3): 
    # Se ingresa numero y se guarda en determinada posición de la lista
    lista[i] = int(input(f"Ingrese numero {i+1}: "))
# Calculo del promedio guardada en la variable prom
prom = (lista[0] + lista[1] + lista[2])/3
# Se imprime resultado
print(f"El promedio de los 3 numeros es {round(prom,2)}")