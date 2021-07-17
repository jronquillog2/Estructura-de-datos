class Ciclo:
    def __init__(self,num=10):
        self=numero=num

    def usowhile(self):
       #print("dento del la clase",self.numero)

       caracter=""
       while caracter not in ("a", "e", "i", "o", "u"):
           caracter = input("ingrese vocal: ").lower()

       print("felicidades el caracter:{} es una vocal".format(caracter))



ciclo1=Ciclo()
ciclo1.usowhile()











