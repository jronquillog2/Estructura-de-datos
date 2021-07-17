class ordenar:
    def __init__ (self,lista):
        self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                ence=True
                break
            if ence == True:return pos
            else: return -1

        def ordenarAsc(self):
            for pos in range(0, len(self.lista)):
                for sig in range(pos + 1, len(self.lista)):
                    if self.lista[pos] > self.lista[sig]:
                        aux = self.lista[pos]
                        self.lista[pos] = self.lista[sig]
                        self.lista[sig]=aux

        def ordenarDes(self):
            for pos,ele in enumerate(self.lista):
                for sig in range(pos+1,len(self.lista)):
                    if ele < self.lista[sig]:
                        aux = self.lista[pos]
                        self.lista[pos]=self.lista[sig]
                        self.lista[sig]=aux




        def primerEliminado(self):
            primer = self.lista[0]
            auxilista=[]
            for pos in range(1,len(self.lista)):
                auxilista.append(self.lista[pos])
            self.lista=auxilista
            return primer

        def primerEliminado2(self):
            primer = self.lista[0]
            self.lista=self.lista[1:]
            return primer

        def ultimo(self):
            return self.lista[-1]

        def ultimoEliminado(self):
            ultimo = self.lista[-1]
            auxlista =[]
            for pos in range(0,len(self.lista)-1):
                auxilista.append(self.lista[pos])
            self.lista=auxilista
            return ultimo

        def ultimoEliminado2(self):
            ultimo = self.lista[-1]
            self.lista=self.lista[0:-1]
            return ultimo

        def insertar(self,num):
            self.ordendarAsc()
            auxilista=[]
            for pos, ele in enumerate(self.lista):
                if num < ele:
                    auxilista.append(num)
                    break
            self.lista=self.lista[0:pos]+auxilista+self.lista[pos:]

        def insertar2(self,num):
            self.ordenarAsc()
            auxilista=[]
            for pos,ele in enumerate(self.lista):
                if num< ele:
                    break
            for i in range(pos):
                auxilista.append(self.lista[i])
            auxilista.append(num)
            for j in range(pos,len(self.lista)):
                auxilista.append(self.lista[j])
            self.lista=auxilista

        def insertarOrden(self,num):
            self.lista.append(num)
            self.ordenarAsc()

        def eliminar(self, num):
            enc=False
            for pos,ele in enumerate(slef.lista):
                if num==ele:
                    enc=True
                    break
            if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
            return enc

    lista = [2,3,8,10]
    #        0 1 2 3      0 1 2 3 4
    ord1 = ordenar(lista)
    # print(ord1.lista)
    #print(or1.ultimoeliminado())
    if ord1.eliminar(8): print("el numero se elimino de la lista",ord1.lista)
    else: print("el numero no se encuentra en la lista")








































