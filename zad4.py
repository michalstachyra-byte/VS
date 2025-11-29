lista_liczb = list(range(1,11))

def co_drugi(liczby):
  co_drugi = liczby[::2]
  for element in co_drugi:
    print(element)

co_drugi(lista_liczb)