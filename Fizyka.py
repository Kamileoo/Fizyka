import math
import random

class Vector:
    """ Wektor prędkości """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

class Particle:
    """ Atom """

    def __init__(self, x: float, y: float, v: Vector, special: bool = False):
        self.x = x
        self.y = y
        self.v = v

        # Atom czerwony
        self.special = special

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}, V: {self.v}'

    def move(self, t: float):
        """ Przesunięcie atomu o wektor prędkości w danym kwancie czasu """
        self.x += self.v.x * t
        self.y += self.v.y * t

    def distance(self, other: "Particle"):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def collision(self, other: "Particle"): # Do zrobienia
        """ Obliczanie nowych wektorów prędkości po kolizji """

class Base:
    """ Program podstawowy """

    def __init__(self, nh: float, nl: float, n: int, radius: float, maxv: float, d: float, m: float):
        # Ilość atomów
        self.n = n

        # Promień atomu
        self.radius = radius

        # Ograniczenie V
        self.maxv = maxv

        # Wartości nh i nl
        self.nh = nh
        self.nl = nl

        # Wymiary zbiornika
        self.height = self.nh * self.radius
        self.length = self.nl * self.radius

        # Tolerancja
        self.d = d

        # Kwant czasu
        self.t = 1/(min(nl,nh) * maxv)

        # Wartość M
        self.m = m

        # Delta t
        self.deltat = self.m * self.t

        # Delta n - ilość zderzeń
        self.deltan = 0

    def spawn(self):
        """ Tworzenie atomów """

        # Lista atomów
        self.particles = []

        # Atom czerwony
        self.particles.append(Particle(0.0,0.0,Vector(random.uniform(0.0,self.maxv),random.uniform(0.0,self.maxv)),True))

        # Atomy niebieskie
        for i in range(0,self.n):
            v = Vector(random.uniform(-self.maxv,self.maxv), random.uniform(-self.maxv,self.maxv))
            p = Particle(random.random() * self.length, random.random() * self.height, v)
            self.particles.append(p)

        # Sortowanie względem X
        self.particles.sort(key=lambda particle: particle.x)

    def wall_detect(self):
        """" Wykrywanie zdeżeń ze ścianą """ # Trzeba dodać właściwości kiedy jest specjalna (czerwona)

        for i in self.particles:

            if i.x <= self.radius * self.d and i.v.x < 0:
                i.v.x *= -1

            if i.x >= (self.length - self.radius * self.d) and i.v.x > 0:
                i.v.x *= -1

            if i.y <= self.radius * self.d and i.v.y < 0:
                i.v.y *= -1

            if i.y >= (self.height - self.radius * self.d) and i.v.y > 0:
                i.v.y *= -1

    def other_detect(self): # Do zrobienia
        """ Wykrywanie zdeżeń z innym atomem """

    def average_distance(self): # Do zrobienia
        """ Obliczanie średniej drogi swobodnej atomu czerwonego """

    def frequency(self): # Do zrobienia
        """ Obliczanie częstości zderzeń """

    def sim(self):
        """ Symulacja 1 kwantu czasu cząsteczki """

        # Ruch cząsteczki
        for i in self.particles:
            i.move(self.t)

        # Wykrywanie zderzeń ze ścianą
        self.wall_detect()

        # Wykrywanie zderzeń z innym atomem
        self.other_detect()

        # Sortowanie względem X
        self.particles.sort(key=lambda particle: particle.x)

    def print(self):
        """ Wypisywanie wszystkich atomów na konsole """

        for i in range(0,self.n+1):
            print(self.particles[i])

    def run(self):
        """ Program główny """

        # Generowanie atomów
        self.spawn()

        # Wykonywanie M symulacji
        for i in range(int(self.m)):
            self.sim()

class Trials: # Do zrobienia i przerobienia
    """ Klasa do wykonywania pewnej ilości prób """


# {
# Nie wiem, czy wartości poniżej spełniają pana normy, podczas obliczeń będzie się zmieniala tylko wartość m (M)
test = Base(nh=300.0, nl=300.0, n=100, radius=1.0, maxv=2.0, d=1.0, m=10.0)

# Uruchamianie programu głównego
test.run()

# Wypisywanie atomów na terminal (dla testów)
test.print()

# Usuwanie
del test

# }

""" Nie wiem w jakiej postaći mamy to wszystko przedstawiać. Chyba mamy narysować wykres za pomocą Pythona. 
Wszystko w klamrze powyżej trzeba zamknąć w klasie Trials, ona ma odpowiadać za wykonywanie wszystkich prób dla różnych N i M"""
