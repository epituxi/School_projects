def get_input():
    nimi = list(input("Enter your name.\n"))[::-1]
    nimi = [kirjain.lower() for kirjain in nimi]
    return nimi

def lists(nimi):
    vokaalit = ['a', 'e', 'i', 'o', 'u', 'y']
    konsonantit = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    vokaali_lst = [kirjain for kirjain in nimi if kirjain in vokaalit]
    konsonantti_lst = [kirjain for kirjain in nimi if kirjain in konsonantit]

    nimimerkki = []

    a = min([len(vokaali_lst), len(konsonantti_lst)])
    if a < 2:
        return "Not able to generate a nickname."
    elif a < 3:
        n = 2
    else:
        n = 3

    for i in range(n):
        if i == 0:
            nimimerkki.append(konsonantti_lst[i].upper())
        else:
            nimimerkki.append(konsonantti_lst[i])
        nimimerkki.append(vokaali_lst[i])

    if str(nimimerkki).lower() == str(nimi[::-1]).lower():
        return "Not able to generate a nickname."

    x = "".join(nimimerkki)

    return f"Your nickname: {x}"

def main():
    nimi = get_input()
    nimimerkki = lists(nimi)
    print('')
    print(nimimerkki)

main()