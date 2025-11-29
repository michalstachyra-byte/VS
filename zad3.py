def parzystosc(liczba):
  return liczba % 2 == 0

x = 54

wynik = parzystosc(x)

if wynik:
  print("Liczba parzysta")
else:
  print("Liczba nieparzysta")

x1=67
wynik1 = parzystosc(x1)

if wynik1:
  print("Liczba parzysta")
else:
  print("Liczba nieparzysta")