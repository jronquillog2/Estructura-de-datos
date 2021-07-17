class For:
    def __init__(self,lim=6):
        self.n=lim
        def usofor(self):
            nombre= "daniel"
            datos=["daniel",50,True]
            numeros = (2,5,6,4,1)
            docente={"nombre": "daniel", "edad": 50, "fac": "faci"}
            listaNotas=[(30,40),(20,40,50),(50,40)]
            listaAlumnos=[{"nombre":"erick","final":70},{"nombre": "Yadi","final":60}, {"nombre":"Danny", "final": 90}]

            #docente = {"nombre": "daniel", "edad": 50, "fac": "faci"}
            #for clave,valor in docente.items():
            #    print(clave,valor,end=" ")

           # listaAlumnos = [{"nombre": "erick", "final": 70}, {"nombre": "Yadi", "final": 60},{"nombre": "Danny", "final": 90}]
            #for alumnos in listaAlumnos:
                #for c,v in alumnos.items():
                   # print(c,v)
                   # if c=="final":
                     #   acu=acu+v
            #print(acu,acu/len(listaAlumnos))

        listaNotas = [(30, 40), (20, 40, 50), (50, 40, 20, 30), (10,20)]
        acu=0
        cont=0
        for notas in listaNotas:
            print(notas)
            acumParcial=0
            for nota in notas:
                acu+=nota
                acumParcial+=nota
                cont+=1
            print(acumParcial,acumParcial/len(notas))
        print(acu,acu/cont)

bucle1 = For()
bucle1.usoFor()








