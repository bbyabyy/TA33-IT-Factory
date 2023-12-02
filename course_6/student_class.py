class Student:
    numar_studenti = 0 # atribut , apartine clasei Student =? variabilade clasa

    def __init__(self, nume, prenume, medie):
         self.nume = nume   # variabila care apartine obiectului => var de instanta/obiect
         self.prenume = prenume
         self.medie = medie


# Referirea la variabila de instanță nume se face cu notația self.nume în metodele acelui obiect
         print("Initializare studenti: ", self.nume, self.prenume)

# Referirea la variabila de clasă numar_studenti se face cu notaţia Student.numar_studenti şi nu cu self.numar_studenti

Student.numar_studenti += 1


#O variabila de obiect cu aceelasi nume ca o variabila de clasa, va ascunde o variabila de clasa fata de metodele clasei
#metoda nr_studenti este in fapt o metoda a clasei si nu a instantei. Asta inseamna ca trebuie sa definim cu declaratia
#static method.


def test_bursier(self):
    if self.medie >= 9.50:
        print("Bursa de merit")
    elif 8.50 <= self.media < 9.50:
        print("Bursa studiu")

def nr_studenti():
    print("exista", Student.numar_studenti, "instante.")

nr_studenti = staticmethod(nr_studenti)


student1 = Student('Bucur', 'Tudor', 10)
student1.test_bursier()
Student.nr_studenti()
student2 = Student('Enache', 'Stefan', 9)
student2.test_bursier()
Student.nr_studenti()