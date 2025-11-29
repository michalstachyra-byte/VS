x = [1,2,3,4,5]

def petla(liczby):
  mnozenie = []

  for liczba in liczby:
    mnozenie.append(liczba*2)

  return mnozenie

wynik_petla = petla(x)

def skladana(liczby_skladana):
  mnozenie_skladna = [liczba_skladana*2 for liczba_skladana in liczby_skladana]
  return mnozenie_skladna

wynik_skladana = skladana(x)

print(f"Liczby: {x}")
print(f"Mnożenie petla: {wynik_petla}")
print(f"Mnożenie skladana: {wynik_skladana}")