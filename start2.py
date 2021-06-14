import sqlite3

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

class Modello(): 

    def __init__(self,nome,descrizione,codDip) :
        self.nome=nome
        self.descrizione=descrizione
        self.codDip=codDip

    def inserimento(self,lista):
        lista.append(self)
        print("modello 3d  inserito \n   ")
        self.stampa()
        
    def stampa(self):
        
        print ("\nNome Modello:  %s \nDescrizione: %s \nDipartimento: %s \n"%(self.nome,self.descrizione,self.codDip))


    def modifica(self,lista,cosa,valore):
        vecchio_nome=self.nome
        if (cosa=='nome'):
            self.nome=valore
            print ("il nome del modello %s è stato cambiato in %s \n"%(vecchio_nome,self.nome))
        elif (cosa=='desc'):
            self.descrizione=valore
            print ("la descrizione del modello %s è stato cambiata in %s \n "%(vecchio_nome,self.descrizione))
        elif (cosa=='dip'):
            self.descrizione=valore
            print ("il dipartimento del modello %s è stato cambiato in %s \n "%(vecchio_nome,self.codDip))
        else:
            print ("nessun valore da modificare riconosciuto \n")

        self.stampa()

    def cancellazione(self,lista):
        nome=self.nome
        lista.remove(self)
        print("\n Modello %s Cancellato" %(nome))


    def inserimento_conDB(self,lista):
        lista.append(self)
        print("modello 3d  inserito \n")
        scelta=input("vuoi inserire questo modello anche nel database ?")
        if(scelta=='S'):
            self.inserisci_db()


    def inserisci_db(self):
        connessioneSQL.execute('insert into  modelli (nome, descrizione,cod_dip) values (?,?)', (self.nome,self.descrizione,self.codDip) )
        print("modello 3d  inserito %s inserito nel database \n"%(self.nome))



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

Lista=[]
print("lista_ vuota",Lista)

mod1=Modello("quadrato","un quadrato molto preciso con angoli super retti","1")
mod1.inserimento(Lista)

print("\n\n stampo primo modello inserito ",Lista)
for mod_sel in Lista:
    mod_sel.stampa()


print("\n\n inserisco un secndo modello")

mod2=Modello("rettangolo","modello di rettangolo incredibilmente con i lati uguali a coppie e gli angoli appuntiti.","2")
mod2.inserimento(Lista)

print("\n\n stampo la lista con 2 modelli ",Lista)
for mod_sel in Lista:
    mod_sel.stampa()


print("\n\n inserisco 3 modello")


mod3=Modello("triangolo","triangolo con ben 3 lati e tra angoli. ","1")
mod3.inserimento(Lista)

print("\n\n stampo la lista con 3 modelli ",Lista)
for mod_sel in Lista:
    mod_sel.stampa()



mod2.cancellazione(Lista)

print("\n\n stampo la lista con 2 modelli . ho acnellato il seocndo",Lista)
for mod_sel in Lista:
    mod_sel.stampa()


print("\n\n modifico il nome del primo elemento ",Lista)
mod1.modifica(Lista,'nome','cerchio')


print("\n\n modifico la descrizione del primo  elemento ",Lista)
mod1.modifica(Lista,'desc','incredibilmente senza angoli ')

print("\n\n modifico la descrizione del secondo  elemento ",Lista)
mod2.modifica(Lista,'dip','2 ')


print("\n\n imposto il database. se esiste mi connetto altrimenti prima lo creo e poi mi connetto \n")


try:
    f = open("db_modelli.db")
    f.close()
    connessioneSQL = sqlite3.connect('db_modelli.db')
    print("\n il DB eiste \n")


except IOError:
    connessioneSQL = sqlite3.connect('db_modelli.db')
    connessioneSQL.execute('CREATE TABLE modelli (id INTEGER PRIMARY KEY, nome, descrizione,cod_dip)')
    print("\n File db creato \n")

    


print("\n\n inserisco  un altro modello questa volta nel DB")

modsql=Modello("modello SQL"," questo modello viene salvato in SQL . ","3")
modsql.inserimento_conDB(Lista)


scelta=input("PREMERE \n N per cercare il nome di un modello   \n T per cercare la descrizone  \n D per cercare  il diaprtimento  \n ")
if(scelta=='N'):
    Ricerca = str(input("inserisci il nome del modello da ricercare? "))
    for mod_sel in Lista:
        if mod_sel.nome == Ricerca:
            mod_sel.stampa()
elif (scelta=='T'):
    Ricerca = str(input("Inserisci la descrizione da cercare"))
    for mod_sel in Lista:
        if mod_sel.descrizione == Ricerca:
            mod_sel.stampa()
elif (scelta=='D'):
    Ricerca = str(input("Inserisci il dipartimento "))
    for mod_sel in Lista:
        if mod_sel.codDip == Ricerca:
            mod_sel.stampa()
            
else:
    print("\n  SCELTA ERRATA \n")

