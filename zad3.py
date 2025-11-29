liczby_10 = list(range(1,11))

def parzyste(liczby):
  for x in liczby:
    if (x%2 == 0):
      print(x)

print(f"Liczby to: {liczby_10}\n")
print("Parzyste z nich:")
parzyste(liczby_10)