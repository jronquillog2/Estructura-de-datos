class Sintaxis:
    def _init_(self, dato="instancia de la clase"):
        self.frase = dato

    def usoVariables(self):
        edad, _peso = 23, 71
        nombres = "Juan Ronquillo"
        #           0953797560
        Sexo = "Masculino"
        civil = True
        # print("civil={} y su tipo es:{}".format(civil,type(civil)))
         # tuplas=()son colecciones de datos de cualquier tipo inmutables
        usuario = ()
        usuario = ("taeyong", 200806, "juanca07@hotmail.com", True)
        #               0       1           2              3
        # usuario[4]="Guayaquil"
        x = usuario[0]
        # listas[] colecciones mutables
        materias = ["Investigación", "Base de datos", "Programación en python"]
        #                 0                1                  2
        materias[1] = "Python with PyCharm"
        materias.append("Go")
        # diccionario={} colecciones de objetos claves: valor tipo json
        docente = {}
        docente = { "nombre": "Juan", "edad": 23 }
        docente = [edad]= 20
        docente = [cargo] = "Docente"
        y=docente = ["cargo"]
        # print(nombres,nombres[0],nombres[0:2],nombres[-1])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(materias,materias[2:],materias[:2],materias[:-1],materias[-2:])
        print(x, y)
        print(docente, docente["nombre"])
    def mostrar(self):
        print("mostrar")
        print(self.frase)


ejer1 = Sintaxis()  # instancia la clase y se crea el objeto1 con todos los atributos y metodos de la clase Sintasis
ejer1.usoVariables()
print(ejer1.frase)








