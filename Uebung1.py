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

print()
print("Aufgabe 11: Fahrzeugdaten speichern")
car_brand = "Audi"
car_model = "A6"
car_year = 2020
car_price = 55000
print(f"Das Fahrzeug {car_brand} {car_model} aus dem Jahr {car_year} kostet {car_price} Euro.")

print()
print("Aufgabe 12: Durchschnittsgeschwindigkeit berechnen")
distance_km = 180
time_h = 2
avg_speed = distance_km / time_h
print(f"Durchschnittsgeschwindigkeit: {avg_speed} km/h")

print()
print("Aufgabe 13: Umrechnung von Einheiten")
speed_kmh = 100
speed_ms = speed_kmh * 0.27778
print(f"{speed_kmh} km/h sind {speed_ms:.2f} m/s")

print()
print("Aufgabe 14: Batteriekapazität bei E-Autos")
battery_kwh = 82
range_km = 600
consumption_kwh_100km = battery_kwh / range_km * 100
print(f"Energieverbrauch: {consumption_kwh_100km:.2f} kWh/100 km")

print()
print("Aufgabe 15: Fahrzeugbewertung")
price = 48000
power_hp = 200
price_per_hp = price / power_hp
print(f"Preis pro PS: {price_per_hp:.2f} Euro/PS")

print()
print("Aufgabe 16: Zeichenketten analysieren")
car_name = "Mercedes-Benz EQS"
int_test = 12
print("Länge:", len(car_name))
print("Großbuchstaben:", car_name.upper())
print("Kleinbuchstaben:", car_name.lower())

print()
print("Aufgabe 17: Zeichenketten konkatenieren")
brand = "Audi"
model = "Q4 e-tron"
year = 2026
print(f"Das Modell {brand} {model} wurde {year} vorgestellt.")

print()
print("Aufgabe 18: Mit mehreren Datentypen arbeiten")
car_dict = {"brand": "Tesla", "power": 325, "electric": True}
print(f"Fahrzeugmarke: {car_dict['brand']}, Leistung: {car_dict['power']} PS, Elektrofahrzeug: {car_dict['electric']}")
car_dict["electric"] = False
print(f"Nach Update - Elektrofahrzeug: {car_dict['electric']}")

print()
print("Aufgabe 19: Durchschnittsverbrauch berechnen")
fuel_used_l = 8.4
distance_km = 120
consumption_l_100km = fuel_used_l / distance_km * 100
print(f"Verbrauch: {consumption_l_100km:.2f} Liter/100 km")

print()
print("Aufgabe 20: Plausibilitätscheck mit Typen")
mileage = 45000
price = "32000"
print("mileage Typ:", type(mileage), "| price Typ:", type(price))
print("mileage + price führt zu einem Fehler: TypeError - unsupported operand type(s) for +: 'int' and 'str'")
price_int = int(price)
sum_values = mileage + price_int
print("Nach Typumwandlung (price -> int):", sum_values)

print()
print("Aufgabe ??: Positiv/Negativ prüfen")
unkown_value = int(input("Gib eine Zahl ein: "))
if unkown_value >= 0:
    print(f"{unkown_value} ist positiv (inkl. 0 als positiv gezählt).")
else:
    print(f"{unkown_value} ist negativ.")
