# -*- coding: utf-8 -*-

#model za nase kontakte
class Kontakt():
    ime = "ime"
    priimek = "priimek"
    email = "email"
    telefon = "tel"
    naslov = "naslov"

    def __init__(self, ime, priimek, email, telefon, naslov):
        self.ime = ime
        self.priimek = priimek
        self.email = email
        self.telefon = telefon
        self.naslov = naslov

    def polno_ime(self):
        return "%s %s" % (self.ime, self.priimek)

    def izpis_kontakta(self):
        return "Ime: %s, Priimek: %s, Email: %s, Telefon: %s, Naslov: %s" % (self.ime, self.priimek, self.email, self.telefon, self.naslov)

#------------------------------------------------------
#program za dodajanje noviih kontaktov oziroma objektov
seznam_kontaktov = []

while True:
    dodaj_kontakt = raw_input("Ali zelis dodati nov kontakt? (da/ne): ")
    if dodaj_kontakt == "da" or dodaj_kontakt == "ja":
        ime = raw_input("Vpisi ime: ")
        priimek = raw_input("Vpisi priimek: ")
        email = raw_input("Vnesi email: ")
        telefon = raw_input("Vpisi telefonsko stevilko: ")
        naslov = raw_input("Vpisi naslov (Ulica in hisna stevilka, postna stevilka in posta: ")

        #ustvarimo objekt oziroma nov kontakt in ga dodamo v seznam
        nov_kontakt = Kontakt(ime, priimek, email, telefon, naslov)
        seznam_kontaktov.append(nov_kontakt)
    elif dodaj_kontakt == "ne" and seznam_kontaktov.__len__() == 0:
        print "Vnesen ni bil noben kontakt!"
        break
    elif dodaj_kontakt == "ne":
        print "Dodani so naslednji kontakti: "
        for n in seznam_kontaktov:
            print "%s: %s" % (n.polno_ime(), n.izpis_kontakta())
        break
    else:
        print "Izbiras lahko samo med da in ne!"
