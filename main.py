print("hello world")
x = 5
print(x)
y = 10
print(x + y)
value_1 = -3.30
print(type(value_1), value_1)
value_3, value_4 = 3, 3.3
this_type = type(value_4)
print(this_type)
print(value_3 + value_4)
b = 7/4
print(int(b))
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
print(numbers[0:3])
my_list = ["hallo", 23, [4.56, 3], True]
print(my_list[0][1:5])
print(my_list[2][1])
my_list.append("ratte")
print(my_list)
my_list.remove("ratte")
if True in my_list:
    print("True ist in der Liste")
k = 19
p = k
k = 20
print(k, p)
c = [1, 2]
s = c
c.append(3)
print(c, s)


customer_list = ["Herr", "Bob", "2025-31-10", "TechCorp", ["item1", "item2"], "25", "Wirtschaftsinformatik", "2025-01-10", "2028-31-09", "Sportinformatik"]
customer_dict = {"company_name": "TechCorp", "title": "Herr", "name": "Bob", "reg_date": "2025-31-10", "items": ["item1", "item2"], "age": 25, "Studiengang": "Wirtschaftsinformatik", "Start": "2025-01-10", "Ende": "2028-31-09", "Lieblingsfach": "Sportinformatik"}
print(customer_dict["title"])
print(customer_dict["Studiengang"])
print(customer_dict["age"])

speed = [120, 130, 125, 140, 135, 150, 160]
for s in speed:
    if s > 140:
        print(f"Das Fahrzeug ist {s - 140}km/h zu schnell.")
    elif s <= 140:
        print(f"Das Fahrzeug ist {max(0, 140 - s)}km/h zu langsam.")
    else:
        print(f"{s}km/h — Geschwindigkeit in Ordnung.")

print()
my_var = (1, 2, 3)
x, y, z = my_var
print(x, y, z)

print()
def calculate_distance(speedy, time):
    distance = speedy * time
    print(f"Distance: {distance}")

calculate_distance(speedy = 90, time = 2)
calculate_distance(speedy = 120, time = 1.5)

print()
def double_speed(speed):
    speed = speed * 2
    print(f"Inside: {speed}")

def add_measurement(measurements, new_value):
    measurements.append(new_value)
    print(f"Inside: {measurements}")

data = [10, 20, 30]
add_measurement(data, 40)
print(f"Outside: {data}")

print()
value = 100
double_speed(value)
print(f"Outside: {value}")

#Veränderliche und unveränderliche Datentypen (siehe Code)
print()
def calculate_efficiency (distance_km , energy_kwh):
    efficiency = (energy_kwh / distance_km) * 100
    return efficiency
result = calculate_efficiency (350 , 72)
print (f"Energy efficiency: {result:.2f} kWh/100 km")

print()
def trip_summary (distance_km , time_h , energy_kwh):
    avg_speed = distance_km / time_h
    efficiency = (energy_kwh / distance_km) * 100
    return avg_speed , efficiency
geschwindigkeit, effi = trip_summary (400 , 5, 80)
print (f"Average speed: {geschwindigkeit:.1f} km/h")
print (f"Efficiency: {effi:.1f} kWh/100 km")

print()
def analyze_trip (distance_km , time_h , energy_kwh):
    avg_speed = distance_km / time_h
    efficiency = (energy_kwh / distance_km) * 100
    return [avg_speed , efficiency]
result = analyze_trip (300 , 4, 60)
print (result)

print()
def analyze_trip_dict (distance_km , time_h , energy_kwh):
    avg_speed = distance_km / time_h
    efficiency = (energy_kwh / distance_km) * 100
    return {
        "avg_speed_kmh": avg_speed ,
        "efficiency_kWh_100km": efficiency
    }
summary = analyze_trip_dict(300 , 4, 60)
print (summary)
