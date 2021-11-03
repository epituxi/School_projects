- Ohjelman kulku

    1. Ohjelma pyytää käyttäjältä ovien lukumäärän ja luo lukumäärää vastaavan määrän ovia.
      - Lukumäärää pyydetään uudestaan niin kauan, että se on välillä 3-999.
      - Ovet numeroidaan luvuin 1 - [ovien_lkm] tulostusta ja pelaamista varten.
    2. Ohjelma pyytää käyttäjää valitsemaan jonkin ovista.
      - Ohjelma pyytää käyttäjältä valintaa uudestaan, kunnes valinta on välillä 1 - [ovien lkm].
    3. Ohjelma avaa jäljelle jääneistä ovista [ovien lkm] - 2 varmasti väärää ovea, eli paljastaa mitä kyseisten ovien takana on (kaikkien takana on varmasti vuohi).
      - Jos käyttäjä on valinnut väärän oven, ohjelma avaa kaikki loput väärät ovet. Jäljelle jää siis tällöin käyttäjän valitsema ovi ja ovi, jonka takana on auto.
      - Jos käyttäjä on valinnut oikean oven, ohjelma jättää satunnaisen oven jäljelle.
      - Käyttäjä ei voi enää valita avattuja ovia.
    4. Ohjelma kysyy käyttäjältä haluaako hän vaihtaa ovea.
      - Käyttäjä voi valita pitävänsä alkuperäisen valitansa tai hän voi vaihtaa oven toiseen avaamattomaan oveen.
      - Käyttäjä valitsee alkuperäisen oven numeron, jos hän haluaa pitää alkuperäisen valintansa, ja toisen oven numeron, jos hän haluaa vaihtaa valintaansa.
      - Ohjelma kysyy valintaa uudelleen, kunnes käyttäjä syöttää jomman kumman avaamattoman oven numeron.
    5. Ohjelma paljastaa minkä oven takana auto on.
      - Jos auto on käyttäjän edellisessä vaiheessa valitseman oven takana, ohjelma tulostaa "Congratulations! The car was behind the door you chose!"
      - Jos auto on toisen oven takana (eli käyttäjän valitseman oven takana on vuohi), ohjelma tulostaa "A goat emerged from the door you chose! The car was behind the other door :("
    6. Ohjelman suoritus päättyy.
  
  
  Ohjelman rakenne
  
  import random

def initialize_doors(number_of_doors):
    # Implement your code here

def remove_wrong_doors(chosen_door, doors):
    # Implement your code here

def print_doors(doors, dont_open):
    # Implement your code here

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    
    # Implement your code here

main()


Täydennä ohjelmaan seuraavat funktiot:

- initialize_doors(number_of_doors)
  - Funktio saa parametrinaan ovien lukumäärän.
  - Funktio palauttaa listan, jossa on ovien lukumäärän verran totuusarvoja, joista jokainen kuvaa yhtä ovea.
    - Totuusarvo True kertoo, että oven takana on auto.
    - Totuusarvo False kertoo, että oven takana on vuohi.
  - Palautetun listan tulee siis sisältää parametrin number_of_doors verran totuusarvoja, joista tasan 1 on arvo True.
  - Satunnaisen indeksin arvolle True saa arvottua komennolla random.randint(), jolle annetaan parametreiksi ala- ja yläraja välille, josta numerot arvotaan.
    - Esimerkiksi komento random.randint(1,6) arpoo satunnaisen kokonaisluvun väliltä 1-6.
    - Arvotun satunnaisluvun tulee olla oven indeksi listassa (luku väliltä 0 - number_of_doors - 1), ei oven numero.
- remove_wrong_doors(chosen_door, doors)
  - Funktio saa parametrinaan käyttäjän valitseman oven numeron (kokonaisluku väliltä 1 - number_of_doors) ja totuusarvoja sisältävän listan, joka kuvaa ovia.
  - Funktio palauttaa varmasti väärien ovien avaamisen jälkeen jäljelle jääneen oven numeron (kokonaisluku väliltä 1 - number_of_doors).
    - Jos chosen_door on ovi, jonka takana on auto, funktio palauttaa satunnaisen oven jäljellä olevista ovista. Satunnainen ovi arvotaan randint-funktiolla vastaavalla tavalla kuin alunperin arvottiin se ovi, jonka takana on auto. Funktiota kutsutaan tarvittaessa niin monta kertaa, että tuloksena on eri ovi kuin chosen_door.
    - Jos oven chosen_door takana on vuohi, funktio palauttaa sen oven numeron, jonka takana on auto.
- print_doors(doors, dont_open)
  - Funktio saa parametrinaan listan totuusarvoja, jotka kuvaavat ovia, ja listan niiden ovien numeroista, joita ei vielä avata.
    - Lista dont_open sisältää siis ovien numerot, ei indeksejä.
  - Funktio tulostaa ovet konsoliin otsikon "Ohjelman tulostus" alla esiteltyjen ohjeiden mukaisesti.
  - Funktio ei palauta mitään.
