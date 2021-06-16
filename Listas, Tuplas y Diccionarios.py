# Tuplas – Listas - Diccionarios
usuario = ("luron","1234","luron@gmail.com")
materias = ["Python","PHP","POO","Go"]
docente = {"nombre":"luis","edad":29,"fac":"faci"}
print(usuario[0],materias[1],docente["nombre"])
print(usuario[0:2],docente.keys(),docente.values())
materias.append("Programacion Movil")
docente["sexo"], docente["edad"]="M", 29
print(materias,docente)
tupla,lista,diccionario=(),[],{}

# Recorridos tuplas y listas con in
for valor in usuario: print(valor)

# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,":",c)

# Recorridos diccionario con items
for c, v in docente.items(): print(c,":",v)
