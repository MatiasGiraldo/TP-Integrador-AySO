#Codigo del programa
print("Ingrese 3 numeros para obtener su promedio.")
lista = ["","",""]
for i in range(0,3): 
    lista[i] = int(input(f"Ingrese numero {i+1}: "))

prom = (lista[0] + lista[1] + lista[2])/3
print(f"El promedio de los 3 numeros es {round(prom,2)}")