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