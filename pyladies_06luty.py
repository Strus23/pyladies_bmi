import json

class BMI:
    def dane(self):
        self.imie=raw_input("Podaj imie:")
        print ("Hello {}".format(self.imie))
        self.waga=float(raw_input("podaj wage:"))
        self.wzrost=float(raw_input("podaj wzrost"))
    def oblicz(self):
        self.bmi=self.waga/self.wzrost**2
        print ("Twoje bmi to {}".format(self.bmi))
    def podzial(self):
        if self.bmi<20:
            klasyfikacja = 'niedowaga'
        elif self.bmi <=25:
            klasyfikacja = 'norma'
        else:
            klasyfikacja = 'nadwaga'
        print ("Masz {}".format( klasyfikacja))
    def ogarnij(self):
        self.dane()
        self.oblicz()
        self.podzial()
    def zapisz_Json(self):
        self.path=r"C:\Users\Katarzyna\Dropbox\Dracena\python_nauka\pyladies\zadanie3bmi.txt"
        results = self.wczytaj_liste()
        results.append({
            "imie":self.imie,
            "wzrost":self.wzrost,
            "waga":self.waga,
            "bmi": self.bmi
        })

        with open(self.path,"w" ) as file:
            json.dump(results,file)
    def wczytaj_liste(self):
        with open (self.path) as file:
            data=json.load(file)
            if type(data) is not list:
                data = []
            return data

    def odczyt(self):
        with open (self.path) as file:
            self.data=json.load(file)


aa=BMI()
aa.ogarnij()
aa.zapisz_Json()
aa.odczyt()


#a2+b2=c2

##class Pitagoras:
##    def przyprostokatne(self):
##        self.a=float(raw_input("Podaj dlugosc przyprostokatnej a:"))
##        self.b=float(raw_input("Podaj dlugosc przyprostokatnej b:"))
##    def dzialanie (self):
##        self.c=(self.a**2+self.b**2)**0.5
##        print ("Wynik to {}".format(self.c))
##kwadrat=Pitagoras()
##kwadrat.przyprostokatne()
##kwadrat.dzialanie()






