Var1 = input("Gib einen Wert für Var1 an: ")
print(f"Var1 = {Var1}")

Var2 = input("Gib einen Wert für Var2 an: ")
print(f"Var2 = {Var2}")

print("Jetzt wechseln wir die beiden!")
temp = Var1
Var1 = Var2
Var2 = temp

print(f"Jetzt ist Var1: {Var1} und Var2: {Var2}")