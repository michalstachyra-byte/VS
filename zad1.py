
x=['Natalia', 'Michał', 'Joanna', 'Mirosław', 'Laura']

def wyswietl_imie(imiona):
  for imie in imiona:
    print(F"{imie}")

    if len(imiona) != 5:
      print("Lista nie zawiera 5 imion")

wyswietl_imie(x)



