print ("Taschenrechner")
zahl1 = int(input("Bitte geben Sie die 1. Zahl ein!"))
zahl2 = int(input("Bitte geben Sie die 2. Zahl ein!"))
operation = input(" + ,- ,* oder / rechnen? ")

if (operation == "+"):
  summe = zahl1 + zahl2
  print("Summe = ",summe)
  
if (operation == "-"):
  differenz = zahl1 - zahl2
  print("Differenz = ", differenz)
  
if (operation == "*"):
  produkt = zahl1 * zahl2
  print("Produkt = ",produkt)
  
if (operation == "/"):
  if (zahl2 !=0):
	quotient = zahl1 / zahl2
  else:
	quotient = "nicht definiert!"
  print("Quotient = ",quotient)
  
  