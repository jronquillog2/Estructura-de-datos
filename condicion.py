class condicion:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
        numero = self.numero1+self.numero2
        self.numero3=numero

    def condicion(self):
        if self.numero1==self.numero2:
            print("numero1:{} y numero2:{} son iguales".format(self.numero1,self.numero2))

        else:
            print("no son iguales")
        print("fin del metodo")

condi1 = condicion (4,7)
print(condi1.numero3)
print(condi1.condicion())










