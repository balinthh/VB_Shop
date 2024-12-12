tart = True

while tart:

    termekek = input("Add meg a bevásárlólistát (szóközökkel elválasztva): ")


    helyes = True
    for termek in termekek:
        if not (('A' <= termek <= 'Z') or ('a' <= termek <= 'z') or ('0' <= termek <= '9') or termek == ' '):
            helyes = False

    if not helyes:
        print("Hiba: A lista csak angol betűket, számokat és szóközöket tartalmazhat.")
    else:
        lista = termekek.lower().split()


        lista.sort()
        print(f"Rendezett lista: {lista}")

        elista = []
        for elem in lista:
            if elem not in elista:
                elista.append(elem)
        print(f"Lista ismétlődés nélkül: {elista}")


        print(f"A lista hossza: {len(elista)}")


        if "kenyer" in elista:
            print("A lista tartalmazza a 'kenyér' szót. Program vége.")
            tart = False
        else:
            print("A lista nem tartalmazza a 'kenyér' szót. Próbáld újra!")
