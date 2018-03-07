import random
zuffalszahl = random.randint(1,101)
versuche = 0

print("Zahlenraten - Errate mei Zoi zwischn 1 und 100")


gewonnen = False
while gewonnen == False:
  zahl = int(input("Wöche Zoi nimmstn? "))
  versuche = versuche + 1
  if (zahl == zuffalszahl):
    print("Supa gmocht du host gwungan. Jetzt griagst a Bier vo mia!")
    gewonnen = True
  elif (zahl < zuffalszahl):
    print("Haha! Die Zoi is gressa wia deine.")
  elif (zahl > zuffalszahl):
    print("Haha! Die Zoi is klana wia deine.")
    
print("Anzahl der restlichen versuche:" , versuche)