print("Aufgabe 1: Deine ersten Variablen")
name = "Bobby Rizzler"
alter = 21
lieblingsmarke = "BMW"
print("Name:", name)
print("Alter:", alter)
print("Lieblingsmarke:", lieblingsmarke)
print()

print("Aufgabe 2: Datentyp erkennen")
a = 12
b = 3.14
c = " Audi "
d = True
print("a ->", a, "Typ:", type(a))
print("b ->", b, "Typ:", type(b))
print("c ->", c, "Typ:", type(c))
print("d ->", d, "Typ:", type(d))
print()

print("Aufgabe 3: Werte überschreiben")
value = 100
print("value vorher:", value, type(value))
value = "hundert"
print("value nachher:", value, type(value))
print("Python ist dynamisch, der Typ kann sich je nach zugewiesenem Wert ändern.")
print()

print("Aufgabe 4: Mehrfachzuweisung")
x = y = z = 0
x = x + 5
print("x, y, z:", x, y, z)
print("Nur x bekam eine neue Zuweisung (5), y und z bleiben 0.")
print()

print("Aufgabe 5: Zuweisung unterschiedlicher Werte")
auto_list = ["BMW", "i4", 340]
auto_dict = {"brand": "BMW", "model": "i4", "horsepower": 340}
print(auto_dict["brand"], auto_dict["model"], auto_dict["horsepower"])
print()

print("Aufgabe 6: Strings kombinieren")
brand = "Audi"
model = "A6"
vollstaendiger_name = brand + " " + model + " " + str(auto_dict["horsepower"])
print("Vollständiger Name:", vollstaendiger_name)

print()
print("Aufgabe 7: Zahlen und Text kombinieren")
speed = 120
print(f"Das Fahrzeug ist {speed}km/h schnell.")

print()
print("Aufgabe 8: Datentypumwandlung (Type Casting)")
engine_power = "300"
engine_power_int = int(engine_power)
ergebnis = engine_power_int + 50
print("engine_power als int + 50:", ergebnis)
print("Direkt '300' + 50 führt zu einem Fehler: TypeError - can only concatenate str (not int) to str")

print()
print("Aufgabe 9: Unterschiedliche Datentypen im Überblick")
marke = "Mercedes-Benz"
leistung_float = 250.5
year = 2026
flag = True
liste = [1, 2, 3]
tuple_wert = (1, 2, 3)
dict_wert = {"brand": "Audi", "power": 250}
print("marke:", type(marke))
print("leistung_float:", type(leistung_float))
print("year:", type(year))
print("flag:", type(flag))
print("liste:", type(liste))
print("tuple_wert:", type(tuple_wert))
print("dict_wert:", type(dict_wert))

print()
print("Aufgabe 10: Mutable vs. Immutable")
a = [1, 2, 3]
b = a
print("Vor append: a =", a, ", b =", b)
a.append(4)
print("Nach append: a: a =", a, ", b =", b)
print("Erläuterung: Listen sind mutable (veränderbar). a und b referenzieren dieselbe Liste, daher sieht b die Änderung.")
