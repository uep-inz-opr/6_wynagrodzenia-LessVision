class pracownik:
    def __init__(self, imie, dochod):
        self.imie = imie
        self.dochod = dochod
        
    
    def kalkuluj(self):
        A = self.dochod 
        B = self.dochod
        C = round(0.0976*self.dochod,2) + round(0.015*self.dochod,2) + round(0.0245*self.dochod, 2)
        D = round(B - C,2)
        E = round(0.09*D,2)
        F = round(0.0775*D,2)
        G = 111.25
        H = round(A - G - C, 2)
        I = round(round((0.18*H),2) - 46.33,2)
        J = round(I - F,2)
        K = round(A - C - E - J,2)
        L = round(0.0976*self.dochod,2) + round(0.065*self.dochod,2) + round(0.0193*self.dochod,2) + round(0.0245*self.dochod,2) + round(0.001*self.dochod,2)
        Ł = round(A + L,2)
        return f"{self.imie} {K} {I} {Ł}"


n = int(input())
parametry = []
pracownicy = []
suma = 0
for i in range (n):
    parametry = input().split(' ')
    worker = pracownik(str(parametry[0]), int(parametry[1]))
    pracownicy.append(worker)

for i in range(n):
    lancuch = str(pracownicy[i].kalkuluj())
    print(lancuch)
    tab_lancuch = lancuch.split(' ')
    suma += float(tab_lancuch[3])

print(suma)



#A -> brutto 
#B -> brutto
#C -> 0.0976*brutto + 0.015*brutto + 0.0245*brutto
#D -> B - C
#E -> 0.09*D
#F -> 0.075*D
#G -> 111.25
#H -> A - G - C
#I -> (0,18*H) - 46.33
#J -> I - F
#K -> A - C - E - J
#L -> 0.0976*brutto + 0.065*brutto + 0.0193*brutto + 0.0245*brutto + 0.001*brutto
#Ł -> A + I
#składki pracodawcy
#łączny koszt na pracownika
#