class Darbuotojas:
    def __init__(self, vardas: str, pavarde: str, asmens_kodas: int, telefono_numeris: str, elektroninis_pastas: str, alga: int, id: str):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.telefono_numeris = telefono_numeris
        self.elektroninis_pastas = elektroninis_pastas
        self.alga = alga
        self.id = id

    def __repr__(self):
        return f"Darbuotuojas ({self.vardas}, {self.pavarde}, {self.elektroninis_pastas}, {self.id}, {self.alga})"

    def gauti_informacija(self):
        print(f"Vardas: {self.vardas}\n"
            f"Pavarde: {self.pavarde}\n"
            f"Asmens_kodas: {self.asmens_kodas}\n"
            f"Telefono_numeris: {self.telefono_numeris}\n"
            f"Elektroninis_pastas: {self.elektroninis_pastas}\n"
            f"Alga: {self.alga}\n"
            f"ID: {self.id}\n")

    def keisti_informacija(self, vardas=None, pavarde=None, telefono_numeris=None, elektroninis_pastas=None, alga=None):
        if vardas:
            self.vardas = vardas
        if pavarde:
            self.pavarde = pavarde
        if telefono_numeris:
            self.telefono_numeris = telefono_numeris
        if elektroninis_pastas:
            self.elektroninis_pastas = elektroninis_pastas
        if alga:
            self.alga = alga


from darbuotuojas import Darbuotojas

class KomercijosVadybininkas(Darbuotojas):
    def __init__(self, vardas, pavarde, asmens_kodas, telefono_numeris, elektroninis_pastas, alga, id):
        super().__init__(vardas, pavarde, asmens_kodas, telefono_numeris, elektroninis_pastas, alga, id)
        self.aptarnaujami_klientai = []
        self.uzsakymai = []

    def __repr__(self):
        return f"Komercijos Vadybyninkas({self.vardas}, {self.pavarde}, {self.elektroninis_pastas}, {self.id})"

    def perziureti_klientus(self):
        print(f"Vadybininkas {self.vardas} {self.pavarde} aptarnauja {self.aptarnaujami_klientai} klientus")

    def priskirti_klienta(self, klientas):
        self.aptarnaujami_klientai.append(klientas)

    def atimti_klienta(self, klientas):
        self.aptarnaujami_klientai.remove(klientas)

    def perziureti_uzsakymus(self):
        print(f"Vadybininkas {self.vardas} {self.pavarde} priziuri {self.uzsakymai} uzsakymus")

    def prideti_uzsakyma_kv(self, uzsakymas):
        self.uzsakymai.append(uzsakymas)
        print(f"Užsakymas pridėtas komercijos vadybininkui {self.vardas}: {uzsakymas.uzsakymo_id}")


from test.transportovadybininkas import TransportoVadybininkas
from order import Uzsakymas

class Automobilis:
    def __init__(self, automobilio_numeris: str, automobilio_komplektacija: str, priekabos_numeris: str, priekabos_tipas: str, vairuotojo_kontaktinis_tel: str, vygdomas_uzsakymas: Uzsakymas, automobilio_busena: str, atsakingas_tv: TransportoVadybininkas):
        self.automobilio_numeris = automobilio_numeris
        self.automobilio_komplektacija = automobilio_komplektacija
        self.priekabos_numeris = priekabos_numeris
        self.priekabos_tipas = priekabos_tipas
        self.vairuotojo_kontaktinis_tel = vairuotojo_kontaktinis_tel
        self.vygdomas_uzsakymas = vygdomas_uzsakymas
        self.automobilio_busena = automobilio_busena
        self.atsakingas_tv = atsakingas_tv
        atsakingas_tv.priskirti_automobili(self)


    def __repr__(self):
        return f"Automobilis({self.automobilio_numeris}, {self.priekabos_numeris}, {self.priekabos_tipas}, {self.vairuotojo_kontaktinis_tel}, {self.atsakingas_tv})"

    def gauti_informacija_apie_automobili(self):
        print(f"Automobilio numeris: {self.automobilio_numeris}\n"
                f"Automobilio komplektacija: {self.automobilio_komplektacija}\n"
                f"Priekabos numeris: {self.priekabos_numeris}\n"
                f"Priekabos tipas: {self.priekabos_tipas}\n"
                f"Vairuotojo kontaktinis tel: {self.vairuotojo_kontaktinis_tel}\n"
                f"Vygdomas užsakymas: {self.vygdomas_uzsakymas}\n"
                f"Automobilio būsenа: {self.automobilio_busena}\n"
                f"Atsakingas TV: {self.atsakingas_tv}")

    def keisti_atsakinga_tv(self, naujas_tv):
        if self.atsakingas_tv:
            self.atsakingas_tv.atimti_automobili(self)
        self.atsakingas_tv = naujas_tv
        naujas_tv.priskirti_automobili(self)
        print(f"Automobilio {self.automobilio_numeris} atsakingas vadybininkas pakeistas į {naujas_tv.vardas}.")

    def keisti_automobilio_komplektacija(self, nauja_komplektacija: str):
        self.automobilio_komplektacija = nauja_komplektacija

    def keisti_priekabos_numeri(self, naujas_priekabos_numeris: str):
        self.priekabos_numeris = naujas_priekabos_numeris

    def keisti_priekabos_tipa(self, naujas_priekabos_tipas: str):
        self.priekabos_tipas = naujas_priekabos_tipas

    def priskirti_nauja_uzsakyma(self, naujas_uzsakymas: Uzsakymas):
        self.vygdomas_uzsakymas = naujas_uzsakymas


from test.komercijosvadybininkas import KomercijosVadybininkas
from client import Klientas

class Uzsakymas:
    uzsakymai = []
    def __init__(self, uzsakymo_id: int, pakrovimo_data: str, atstumas: float, iskrovimo_data: str, pervezimo_kaina: float, automobilio_komplektacija: str, priekabos_tipas: str, klientas: Klientas, komercijos_vadybininkas: KomercijosVadybininkas, uzsakymo_busena: str):
        self.uzsakymo_id = uzsakymo_id
        self.pakrovimo_data = pakrovimo_data
        self.atstumas = atstumas
        self.iskrovimo_data = iskrovimo_data
        self.pervezimo_kaina = pervezimo_kaina
        self.automobilio_komplektacija = automobilio_komplektacija
        self.priekabos_tipas = priekabos_tipas
        self.klientas = klientas
        self.komercijos_vadybininkas = komercijos_vadybininkas
        self.uzsakymo_busena = uzsakymo_busena
        klientas.prideti_uzsakyma(self)
        komercijos_vadybininkas.prideti_uzsakyma_kv(self)


    @classmethod
    def prideti_uzsakyma(cls, uzsakymo_id, pakrovimo_data, atstumas, iskrovimo_data, pervezimo_kaina, automobilio_komplektacija,
                      priekabos_tipas, klientas, komercijos_vadybininkas, uzsakymo_busena):
        new_order = cls(uzsakymo_id, pakrovimo_data, atstumas, iskrovimo_data, pervezimo_kaina, automobilio_komplektacija,
                        priekabos_tipas, klientas, komercijos_vadybininkas, uzsakymo_busena)
        cls.uzsakymai.append(new_order)
        klientas.prideti_uzsakyma(new_order)
        komercijos_vadybininkas.prideti_uzsakyma_kv(new_order)
        print(f"Naujas užsakymas pridėtas: {new_order.uzsakymo_id}")

    def __repr__(self):
        return f"Uzsakymas({self.uzsakymo_id}, {self.klientas}, {self.komercijos_vadybininkas}, {self.uzsakymo_busena})"

    def gauti_informacija_apie_uzsakyma(self):
        print(f"Užsakymo ID: {self.uzsakymo_id}\n"
                f"Pakrovimo data: {self.pakrovimo_data}\n"
                f"Atstumas nuo pakrovimo iki iškrovimo: {self.atstumas}\n"
                f"Iškrovimo data: {self.iskrovimo_data}\n"
                f"Pervežimo kaina: {self.pervezimo_kaina}\n"
                f"Automobilio komplektacija: {self.automobilio_komplektacija}\n"
                f"Priekabos tipas: {self.priekabos_tipas}\n"
                f"Klientas: {self.klientas.pavadinimas}\n"
                f"Komercijos vadybininkas: {self.komercijos_vadybininkas}\n"
                f"Užsakymo būsena: {self.uzsakymo_busena}")

    def redaguoti_uzsakymo_busena(self, nauja_busena: str):
        self.uzsakymo_busena = nauja_busena
        print(f"Užsakymo {self.uzsakymo_id} būsena pakeista į {nauja_busena}.")

    def keisti_komercijos_vadybininka(self, naujas_vadybininkas):
        self.komercijos_vadybininkas.uzsakymai.remove(self)
        self.komercijos_vadybininkas = naujas_vadybininkas
        naujas_vadybininkas.prideti_uzsakyma(self)
        print(f"Užsakymo {self.uzsakymo_id} komercijos vadybininkas pakeistas į {naujas_vadybininkas.vardas}.")


komercijos_vadybininkas = KomercijosVadybininkas(
    vardas="Jonas", pavarde="Jonaitis", asmens_kodas=12345678901,
    telefono_numeris="+37060012345", elektroninis_pastas="jonas@example.com", alga=1500, id= "KV1"
)

transporto_vadybininkas = TransportoVadybininkas(
    vardas="Petras", pavarde="Petraitis", asmens_kodas=10987654321,
    telefono_numeris="+37060054321", elektroninis_pastas="petras@example.com", alga=1700, id= "TV1"
)
transporto_vadybininkas2 = TransportoVadybininkas(
    vardas="Antanas", pavarde="Antanaitis", asmens_kodas=12121212121,
    telefono_numeris="+37067777777", elektroninis_pastas="antanas@example.com", alga=1600, id= "TV2"
)
klientas = Klientas(
    pavadinimas="ABC Įmonė", kontaktinis_numeris="+37061234567",
    elektroninis_pastas="info@abcimone.lt", klientas_id=1001,
    komercijos_vadybininkas=komercijos_vadybininkas
)

uzsakymas1 = Uzsakymas(uzsakymo_id=1,pakrovimo_data="2024.05.20",
                       atstumas=1234, iskrovimo_data="2024.05.23",
                       pervezimo_kaina= 1400,automobilio_komplektacija="Standartine",
                       priekabos_tipas="Tentas",klientas=klientas,
                       komercijos_vadybininkas=komercijos_vadybininkas,uzsakymo_busena="Sukurta"
                       )

# Priskiriam uzsakyma prie kliento

klientas.prideti_uzsakyma(uzsakymas1)

# Komercijos vadybininkas priskiria klientą
komercijos_vadybininkas.priskirti_klienta(klientas)

# Sukuriame automobilį ir priskiriame užsakymą ir pakeiciame uzsakymo busena
automobilis = Automobilis(
    automobilio_numeris="ABC123", automobilio_komplektacija="Standartinė",
    priekabos_numeris="PRK456", priekabos_tipas="Šaldytuvas",
    vairuotojo_kontaktinis_tel="+37065555555", vygdomas_uzsakymas=uzsakymas1,
    automobilio_busena="Parengtas", atsakingas_tv=transporto_vadybininkas
)

uzsakymas1.redaguoti_uzsakymo_busena("Suplanuota")
# Informacijos atvaizdavimas
print("Informacija apie komercijos vadybininką ir jo klientus:")
komercijos_vadybininkas.perziureti_klientus()

print("\nInformacija apie transporto vadybininką ir jo automobilius:")
automobilis.gauti_informacija_apie_automobili()


Uzsakymas.prideti_uzsakyma(
    uzsakymo_id=1,
    pakrovimo_data="2024-06-10",
    atstumas=100.0,
    iskrovimo_data="2024-06-11",
    pervezimo_kaina=500.0,
    automobilio_komplektacija="Standartine",
    priekabos_tipas="Saldytuvas",
    klientas=klientas,
    komercijos_vadybininkas=komercijos_vadybininkas,
    uzsakymo_busena="Pending"
)

print("\nInformacija apie klientą ir jo užsakymus:")
klientas.bendra_info()
klientas.uzsakymu_info()

# Pakeitimai
print("\nAtliekami pakeitimai:")
automobilis.keisti_automobilio_komplektacija("ADR")
automobilis.keisti_priekabos_numeri("PRK789")
automobilis.keisti_priekabos_tipa("Tentinis")
automobilis.keisti_atsakinga_tv(transporto_vadybininkas2)

print("\nAtnaujinta informacija apie automobilį:")
automobilis.gauti_informacija_apie_automobili()