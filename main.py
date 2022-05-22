class pracownik:
    def __init__(self, imie, dochod):
        self.imie = imie
        self.dochod = dochod
       
    
    def kalkuluj(self):
        A = self.dochod 
        B = self.dochod
        C = round(round(0.0976*self.dochod,2) + round(0.015*self.dochod,2) + round(0.0245*self.dochod,2),2)
        D = round(B - C,2)
        E = round(0.09*D,2)
        F = round(0.0775*D,2)
        G = 111.25
        H = round(A - G - C, 0)
        I = round(round((0.18*H),2) - 46.33,2)
        J = round(I - F,0)
        K = round(A - C - E - J,2)
        L = round(round(0.0976*self.dochod,2) + round(0.065*self.dochod,2) + round(0.0193*self.dochod,2) + round(0.0245*self.dochod,2) + round(0.001*self.dochod,2),2)
        Ł = round(A + L,2)
        return f"{self.imie} {K} {L} {Ł}"
        #return f"{self.imie} {A} {B} {C} {D} {E} {F} {G} {H} {I} {J} {K} {L} {Ł}"


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
