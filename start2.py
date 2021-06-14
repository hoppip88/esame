class Dipartimento():

    def __init__(self,nome,codice) :
        self.nome=nome
        self.codice=codice

    def inserimento(self,lista):
        lista.append(self)
        print("dipartimento inserito \n   ")
        self.stampa()

    def stampa(self):
        print ("\nNome dipartimento:  %s \n Codice: %s \n"%(self.nome,self.codice))

    def cancellazione(self,lista):
        nome=self.nome
        lista.remove(self)
        print("\n dièartimento %s Cancellato"%(nome))
  
  
print("\n Buon giorno. esempio di uso continuo delle funzioni del programma \n")


ListaDipartimenti=[]
print("lista_ vuota dipartimenti",ListaDipartimenti)

dip1=Dipartimento("primo dipartimento","1")
dip1.inserimento(ListaDipartimenti)

dip2=Dipartimento("secondo dipartimento","2")
dip2.inserimento(ListaDipartimenti)

dip3=Dipartimento("terzo dipartimento","3")
dip3.inserimento(ListaDipartimenti)

print("\n stampo lista dipartimenti inseriti ")
for dip_sel in ListaDipartimenti:
    dip_sel.stampa()
