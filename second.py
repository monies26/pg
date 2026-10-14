def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    if isinstance(cislo, bool) or not isinstance(cislo, (int, str)):
        raise TypeError("cislo musi byt cele cislo nebo jeho textova reprezentace")

    try:
        cislo = int(cislo)
    except ValueError as error:
        raise ValueError("cislo musi byt cele cislo od 0 do 100") from error

    if not 0 <= cislo <= 100:
        raise ValueError("cislo musi byt v rozsahu od 0 do 100")

    jednotky = (
        "nula",
        "jedna",
        "dva",
        "tři",
        "čtyři",
        "pět",
        "šest",
        "sedm",
        "osm",
        "devět",
    )
    teens = (
        "deset",
        "jedenáct",
        "dvanáct",
        "třináct",
        "čtrnáct",
        "patnáct",
        "šestnáct",
        "sedmnáct",
        "osmnáct",
        "devatenáct",
    )
    desitky = {
        2: "dvacet",
        3: "třicet",
        4: "čtyřicet",
        5: "padesát",
        6: "šedesát",
        7: "sedmdesát",
        8: "osmdesát",
        9: "devadesát",
    }

    if cislo < 10:
        return jednotky[cislo]
    if cislo < 20:
        return teens[cislo - 10]
    if cislo == 100:
        return "sto"

    desitka, jednotka = divmod(cislo, 10)
    if jednotka == 0:
        return desitky[desitka]
    return f"{desitky[desitka]} {jednotky[jednotka]}"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
