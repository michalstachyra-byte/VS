def function (lista1, lista2):
  lista_merge = lista1 + lista2

  lista_uniq = list(set(lista_merge))
  potega = [liczba ** 3 for liczba in lista_uniq]
  return potega

lista1 = [1, 2, 5, 4, 2, 7]
lista2 = [3, 4, 6, 8, 1, 9]

wynik = function(lista1,lista2)

print(wynik)