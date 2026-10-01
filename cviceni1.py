def add(a, b):
    c = a + b
    return c 
#soucet

def mul(a, b, c):
   #nasobeni
   vysledek = a * b * c
   return vysledek

def div(a, b):
   if b == 0:
      #prvni cast: kdy b je nula
      vysledek = 0
   else:
      #druhaa cast- kdyx b je nenula
    vysledek = a / b
    return vysledek 
   #deleni / s des. carkou deleni // na cele cislo 

def je_delitelne_beze_zbytku(a):
   return je_delitelne_beze_zbytku(a, 3)



def je_delitelne_3(a):
    if a % 3 == 0:
        return "je delitelne beze zbytku"
    else:
        return "neni delitelne beze zbytku"


if __name__ == "__main__":
   # x = add(1, 2)
   x = mul(1, 2, 3)
   x= div(10, 1) 
   vysledek = je_delitelne_3(10)
   print(vysledek)
   
