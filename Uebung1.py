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
# Wert von power ändern und Ausgabe wiederholen
car_dict["power"] = 340
print(f"Nach Update - Leistung: {car_dict['power']} PS")

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

print()
print("Aufgabe 2.6.1: Boolesche Ausdrücke")
speed = 90
limit = 100
too_fast = speed > limit
print(too_fast)

print()
print("Aufgabe 2.6.2: Kombination zweier Vergleiche")
speed = 85
rpm = 2200
cond_and = (speed > 80) and (rpm < 3000)
print(f"a) speed > 80 und rpm < 3000 -> {cond_and}")
cond_or = (speed > 80) or (rpm < 3000)
print(f"c) speed > 80 oder rpm < 3000 -> {cond_or}")

print()
print("Aufgabe 2.6.3: Bereichsprüfung mit logischen Operatoren")
temperature = 95
in_range_and = (temperature >= 80) and (temperature <= 100)
print(f"a/b) 80 <= temperature <= 100 (via and) -> {in_range_and}")
chained = 80 <= temperature <= 100
print(f"c) 80 <= temperature <= 100 (verkettet) -> {chained}")

print()
print("Aufgabe 2.6.4: Kombination mehrerer Sensorbedingungen")
speed = 110
fuel_level = 8
engine_on = True
if speed > 100 and engine_on == True and fuel_level > 5:
    print("a) speed>100 and engine_on==True and fuel_level>5 -> True")
else:
    print("a) speed>100 and engine_on==True and fuel_level>5 -> False")
cases = [
    {"speed": 110, "fuel_level": 8, "engine_on": True},
    {"speed": 95,  "fuel_level": 8, "engine_on": True},
    {"speed": 110, "fuel_level": 4, "engine_on": True},
    {"speed": 110, "fuel_level": 8, "engine_on": False},
]
for case in cases:
    result = (case["speed"] > 100) and (case["engine_on"] == True) and (case["fuel_level"] > 5)
    print(f"Test {case} -> {result}")
expr_or = (speed > 100) or (engine_on == True) or (fuel_level > 5)
print(f"c) Mit or statt and -> {expr_or} (erfüllt, wenn mind. eine Bedingung wahr ist)")

print()
print("Aufgabe 2.6.5: Komplexer Ausdruck mit not, and, or")
temperature = 102
rpm = 3500
oil_pressure = 1.2
emergency_mode = False
if ((temperature > 100) and (rpm > 3000)) or (oil_pressure < 1.5) or (not emergency_mode):
    expr_ausdruck = True
else:
    expr_ausdruck = False
print(f"(temperature>100 and rpm>3000) oder (oil_pressure<1.5) oder (not emergency_mode) -> {expr_ausdruck}")

print()
print("Aufgabe 2.6.6: Datentypüberprüfung und Wahrheitswerte")
values = [0, 1, "", " Data ", [], [1, 2], None]
for v in values:
    print(v, bool(v))
# Folgende Werte gelten in Python als 'falsy' (werden zu False), wenn es eine "leere" oder "null"-artige Repräsentation ist

print()
print("Aufgabe Verzweigungen 1")
speed = 121
if speed > 120:
    print("Too fast! Slow down.")
else:
    print("Speed is ok.")

print()
print("Aufgabe Verzweigungen 2")
battery_level = 19
if battery_level < 20:
    print("Warning: Low battery!")
else:
    print("Battery level sufficient.")

print()
print("Aufgabe Verzweigungen 3")
temperature = 60
if temperature < 60:
    print("Freezing temperature!")
elif 60 <= temperature <= 100:
    print("Termperature normal.")
else:
    print("Warning Overheating!")

print()
print("Aufgabe Verzweigungen 4")
score = 67
if 100 >= score >= 90:
    grade = "Excellent"
elif 90 > score >= 75:
    grade = "Good"
elif 75 > score >= 60:
    grade = "Satisfactory"
elif 60 > score >= 40:
    grade = "Needs improvement"
else:
    grade = "Insufficient"
print(f"Ergebnis: {grade}")

print()
print("Aufgabe Verzweigungen 5")
mode = "sport"
speed = 130
if mode == "sport":
    if speed > 150:
        print("Sport mode: maximum speed reached!")
    else:
        print("Sport mode: accelerating.")
elif mode == "eco":
    if speed > 100:
        print("Eco mode: limit reached!")
    else:
        print("Eco mode: efficient driving.")
else:
    print("Unknown mode.")

print()
print("Aufgabe Verzweigungen 6")
temperature = 95
pressure = 1.8
system_active = True
if system_active:
    if temperature > 100:
        print("Warning: High temperature!")
    elif pressure < 1.5:
        print("Pressure below threshold!")
    else:
        print("System running normally.")
else:
    print("System offline.")

print()
print("Aufgabe Verzweigungen 7")
#a)
# rpm > 3000 und speed > 100 und temperature > 100
# speed > 100 und rpm <= 3000 fuel_level < 10
# speed <= 100 oder rpm <= 3000 und fuel_level >= 10 oder rpm > 3000 und temperature <= 100

#b), c)
speed = 110
rpm = 3200
temperature = 105
fuel_level = 8

if speed > 100 and rpm > 3000 and temperature > 100:
    print("Warning: High engine load!")
elif speed > 100 and rpm > 3000 and temperature <= 100:
    print("Engine warm, but temperature OK.")
elif speed > 100 and rpm <= 3000 and fuel_level < 10:
    print("Warning: Low fuel during high speed.")
elif speed > 100 and rpm <= 3000 and fuel_level >= 10:
    print("Normal operation.")
else:
    print("Speed below threshold.")

print()
print("Aufgabe for- und while-Schleifen 1")
speeds = [50, 70, 90, 110]
for s in speeds:
    print(f"Current speed: {s} km/h")
while speeds:
    current_speed = speeds.pop(0)
    print(f"Processing speed: {current_speed} km/h")

print()
print("Aufgabe for- und while-Schleifen 2")
text = "Data"
i = 0
b = 0
for char in text:
    print(char)
    i = i + 1
print (f"The word has {i} letters.")
while text:
    char = text[0]
    print(char)
    text = text[1:] #entfernt das erste Zeichen aus text (verkürzt die Zeichenkette).
    b = b + 1
print (f"The word has {b} letters.")

print()
print("Aufgabe for- und while-Schleifen 3")
car_data = {"speed" : 88, "rpm" : 3100, "fuel": 12.5}
for key in car_data:
    print(f"Keys: {key}")
print()
for value in car_data.values():
    print(f"Values: {value}")
print()
for key, value in car_data.items():
    print(f"{key} = {value}")

print()
print("Aufgabe Schleifensteuerung mit continue und break 4")
speeds = [40, 60, 0, 80, 120, -1, 100]
for s in speeds:
    if s == 0:
        print("Engine idle: skipping")
        continue
    if s < 0:
        print("Negative speed: stopping processing")
        break
    else:
        print(f"Speed OK: {s}")

print()
print("Kombination und pass und verschachtelte Schleifen 5")
vehicles = {"Car A": ["speed", "rpm", "fuel"], "Car B": ["speed", "fuel"], "Car C": []}
for vehicle, sensors in vehicles.items():
    if not sensors:
        pass
    for sensor in sensors:
        print(f"{vehicle}: {sensor}")