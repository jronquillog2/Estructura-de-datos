"""uso de while infinito"""

C = 1
while True:
    print(C)

# while validacion
vocal= input("ingrese vocal:")
while vocal not in("a","e","i","o","u"):
    if vocal ==".":
        break
    vocal = input("vocal:")
print("su vocal o punto es:{}".format(vocal))


