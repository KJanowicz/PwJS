#!/usr/bin/env python
# coding: utf-8

# In[4]:


def testy():
    #Zadanie 1:
    p1 = Student("Karol","Janowicz",19366,"IIS")
    print("Zadanie 1")
    print(p1.imie)
    print(p1.nazwisko)
    #print(p1.__nr_indeksu)
    print(p1.kierunek)
    print(p1)
    print("")
    
    #Zadanie 2:
    print("Zadanie 2")
    p2 = Student("Jan","Kowalski",12345,"IIS")
    print(p1.__lt__(p2))
    print(p1.__eq__(p2))
    print("")
    
    #Zadanie 3:
    print("Zadanie 3")
    p3 = Student("Adam","Nowak",14212,"IP")
    print("Licznik: %s"%(p3.getLicznik()))
    print("")
    
    #Zadanie 4:
    print("Zadanie 4")
    p4 = StudentInformatyki("Tytus","Szyluk",17654,"IIS","Grafika")
    print(p4)
    print(p4.specjalnosc)
    pass
    print("")

class Student():
    __licznik = 0

    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek

    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s\nNazwisko: %s\nnr indeksu: %s\nkierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc

if __name__ == "__main__":
    testy()


# In[ ]:




