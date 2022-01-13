# -*- coding: utf-8 -*-
# Nimi: Viljami Riihimäki
# Opiskelijanumero: 910048
#​​‌‌‌‌‌‌​​‌‌​​‌ CS-A1130 Tietotekniikka sovelluksissa

#​​‌‌‌‌‌‌​​‌‌​​‌ Tarkistin testaa tätä funktiota
def palindromi(sana):
    #​​‌‌‌‌‌‌​​‌‌​​‌ Toteuta ratkaisusi tänne
    print()
    #​​‌‌‌‌‌‌​​‌‌​​‌ Palautettava arvo:
    return False


#​​‌‌‌‌‌‌​​‌‌​​‌ Tätä funktiota ei testata
#​​‌‌‌‌‌‌​​‌‌​​‌ eli voit muokata tätä funktiota vapaasti.
#​​‌‌‌‌‌‌​​‌‌​​‌ Voit testata main()-funktion avulla palindromi()-funktion toimintaa
def main():
    print("Testataan palindromilla:")
    print("Funktio palautti:", palindromi("saippuakauppias"))

    print()

    print("Testataan sanalla joka ei ole palindromi:")
    print("Funktio palautti:", palindromi("palindromi"))


#​​‌‌‌‌‌‌​​‌‌​​‌ Älä muuta tätä
if __name__ == "__main__":
    main()

