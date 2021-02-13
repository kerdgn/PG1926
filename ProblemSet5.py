class Okul():
    tip = "okulturu"

    def __init__(self, adı, türü, öğretmen, öğrenci, sınıf):
        self.adı = adı
        self.türü = türü
        self.öğretmen = öğretmen
        self.öğrenci = öğrenci
        self.sınıf = sınıf

O1 = Okul("Fevzi Atlıoğlu", "İlköğretim Okulu", 15, 300, 30)
O2 = Okul("Kalaba", "Anadolu Lisesi", 40, 800, 50)
O3 = Okul("Gazi", "Üniversitesi", 100, 6000, 500)

Okullar = [O1, O2, O3]

for okul in Okullar:
    print(okul.adı, okul.türü, okul.öğretmen, okul.öğrenci, okul.sınıf)
