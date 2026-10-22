from math import isqrt

<<<<<<< HEAD

=======
>>>>>>> 49ea1e6f86162c54c8f9042f91e1b37231201340
def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for delitel in range(2, isqrt(cislo) + 1):
        if cislo % delitel == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    return [
        cislo
        for cislo in range(2, maximum + 1)
        if je_prvocislo(cislo)
    ]


def my_range_while(start, stop, step=1):
    cislo = start
    while cislo < stop:
        yield cislo
        cislo += step


if __name__ == "__main__":
    for cislo in (1, 2, 3, 100, 101):
        print(f"{cislo} -> {je_prvocislo(cislo)}")

    for maximum in (1, 2, 3, 10):
        print(f"{maximum} -> {vrat_prvocisla(maximum)}")
