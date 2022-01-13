# -*- coding: utf-8 -*-
# Nimi: Viljami Riihimäki
# Opiskelijanumero: 910048
#​​‌‌‌‌‌‌​​‌‌​​‌ CS-A1130 Tietotekniikka sovelluksissa

#​​‌‌‌‌‌‌​​‌‌​​‌ Tarkistin testaa tätä funktiota
def rain():
    """
    Kysyy lukuja kunnes käyttäjä antaa -999 ja sen jälkeen laskee epänegatiivisten lukujen keskiarvon.
    """
    #​​‌‌‌‌‌‌​​‌‌​​‌ Palautettava arvo:
    return keskiarvo


#​​‌‌‌‌‌‌​​‌‌​​‌ Tätä funktiota ei testata, joten voit muokata sitä.
def main():
    print("Ohjelma laskee sademäärän keskiarvon.")

    vastaus = rain()
    print("Sademäärän keskiarvo on: {} millimetriä\n".format(vastaus))

    print("Ohjelman suoritus päättyy.")


#​​‌‌‌‌‌‌​​‌‌​​‌ Älä muuta tätä
if __name__ == "__main__":
    main()

