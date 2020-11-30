from No import No

class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
   
    def __len__(self):
        return self.size

    def add(self, value):
        if self.first: 
            aux = self.first
            ant = None
            while(aux.next):
                ant = aux
                aux = aux.next
            aux.next = No(value)
            aux.next.ant = aux
            aux.ant = ant
            if self.last:
                self.last = aux.next
        else:
            self.first = No(value)
            self.last = No(value)
        self.size += 1


    def printListOrdered(self):
        if self.first == None:
            print("Lista Vazia")

        aux = self.first
        while(aux):
            print(aux.report)
            aux = aux.next
        print("Total de Elementos na lista: " + str(self.size))
        print("\n -----------------\n")
    
    def printReverseOrder(self):
        aux = self.last
        print("Lista em ordem inversa da inserção: " + str(self.size))
        while(aux):
            print(aux.report)
            aux = aux.ant
        print("Total de Elementos na lista: " + str(self.size))
        print("\n -----------------\n")
