"""Funciones sin retorno"""
def vocales(frase):
     for car in frase:
         if car in("a","e","i","o","u"):
            print(car)

"""Llamada a funcion"""
oracion = input("Ingrese oracion: ")
vocales(oracion.lower())

"""Funcion con retorno de valor"""
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

# llamada a funcion
listanotas = [5, 7, 6, 9, 9]
prom = promedio(listanotas)
print("Promedio: {} = {}".format(listanotas, prom))



