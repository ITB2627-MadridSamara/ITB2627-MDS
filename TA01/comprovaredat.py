edat = int(input("Quina edat tens? "))

if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")
    if edat < 26:
    print("Tens descompte jove")
else:
    print("No tens descompte jove")