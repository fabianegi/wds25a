class Depot:
    def __init__(self, name: str, stock: int, capacity: int):
        self.name = name
        self.stock = stock        # in Paletten
        self.capacity = capacity  # in Paletten

    def provide_goods(self, amount:int) -> int:
        # Anpassung: Depot darf nicht mehr ausgeben als vorhanden
        if amount > self.stock:
            print(f"{self.name}: Nur {self.stock} Paletten verfügbar – Menge wird angepasst.")
            provided = self.stock
            self.stock = 0
            return provided
        else:
            self.stock -= amount
            return amount

    def store_goods(self, amount:int) -> None:
        if self.stock + amount > self.capacity:
            raise ValueError("Depot-Kapazität überschritten.")
        self.stock += amount

distances_km = {
    ("Zentrallager", "Stuttgart"): 200.0,
    ("Stuttgart", "Berlin"): 220.0,
    ("Berlin", "Hamburg"): 780.0,
    ("Hamburg", "Zentrallager"): 290.0,
}

class Truck:
    def __init__(self, name: str, current_location: str, capacity: int, load: int, mileage_km: float, depot: Depot):
        self.name = name
        self.current_location = current_location
        self.capacity = capacity
        self.load = load
        self.mileage_km = mileage_km
        self.depot = depot

    def get_status(self) -> str:
        print(f"\n{self.name}\n- Ort: {self.current_location},\n- Ladung: {self.load}/{self.capacity} Paletten,\n- Kilometerstand: {self.mileage_km} km")

    def drive_to(self, destination: str) -> None:
        distance = get_distance_km(self.current_location, destination)
        if distance < 0:
            print(f"Fahrt abgebrochen: Distanz von {self.current_location} nach {destination} nicht definiert.")
            return
        print(f"{self.name} fährt von {self.current_location} nach {destination} ({distance} km)")
        self.current_location = destination
        self.mileage_km += distance

    def load_from_depot(self, depot: Depot, amount: int) -> None:
        # Anpassung: Truck darf nicht mehr laden als Kapazität frei
        free_capacity = self.capacity - self.load
        if amount > free_capacity:
            print(f"{self.name}: Kann nicht {amount} Paletten laden – nur {free_capacity} frei.")
            amount = free_capacity

        provided = depot.provide_goods(amount)
        self.load += provided
        print(f"{self.name} lädt {provided} Paletten aus dem {depot.name}.")

    def unload_to_depot(self, depot: Depot, amount: int) -> None:
        if amount > self.load:
            print(f"{self.name}: Hat nur {self.load} Paletten geladen.")
            amount = self.load
        if depot.stock + amount > depot.capacity:
            allowed = depot.capacity - depot.stock
            print(f"{depot.name}: Kann nur {allowed} Paletten aufnehmen.")
            amount = allowed
        self.load -= amount
        depot.stock += amount
        print(f"{self.name} entlädt {amount} Paletten in {depot.name}.")

def get_distance_km(start: str, destination: str) -> float:
    for (loc1, loc2), dist in distances_km.items():
        if (loc1 == start and loc2 == destination) or (loc1 == destination and loc2 == start):
            return dist
    return -1.0

def run_simulation():
    # Objekte anlegen
    depotA = Depot("Zentrallager", 100, 200)
    depotB = Depot("Stuttgart", 50, 150)
    depotC = Depot("Berlin", 80, 180)

    truckA = Truck("Truck 1", "Zentrallager", 20, 0, 101000.0, depot=None)
    truckB = Truck("Truck 2", "Stuttgart", 15, 5, 85000.0, depot=None)
    truckC = Truck("Truck 3", "Berlin", 25, 10, 125000.0, depot=None)
    truckD = Truck("Truck 4", "Hamburg", 30, 0, 90000.0, depot=None)

    trucks = {1: truckA, 2: truckB, 3: truckC, 4: truckD}
    depots = {"Zentrallager": depotA, "Stuttgart": depotB, "Berlin": depotC}

    while True:
        print(f"\n1) Status aller Trucks anzeigen\n2) Truck zu einem Depot fahren lassen\n3) Ladung im Depot aufnehmen\n4) Ladung in Depot abgeben\n5) Programm beenden")
        try:
            choice = int(input("Eingabe: ").strip())
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        if choice == 1:
            for t in trucks.values():
                t.get_status()
        elif choice == 2:
            try:
                tn = int(input("Welcher Truck soll fahren? (1-4): ").strip())
                truck = trucks[tn]
            except (ValueError, KeyError):
                print("Ungültiger Truck-Name.")
                continue
            destination = input("Zielort (Zentrallager, Stuttgart, Berlin, Hamburg): ").strip()
            truck.drive_to(destination)
        elif choice == 3:
            try:
                tn = int(input("Welcher Truck soll laden? (1-4): ").strip())
                truck = trucks[tn]
            except (ValueError, KeyError):
                print("Ungültiger Truck-Name.")
                continue
            depot_name = input("Von welchem Depot laden? (Zentrallager, Stuttgart, Berlin): ").strip()
            if depot_name not in depots:
                print("Ungültiges Depot.")
                continue
            depot = depots[depot_name]
            if truck.current_location != depot_name:
                print(f"{truck.name} ist nicht im {depot_name}. Muss zuerst dorthin fahren.")
                continue
            try:
                amount = int(input("Anzahl Paletten zum Laden: ").strip())
            except ValueError:
                print("Ungültige Menge.")
                continue
            truck.load_from_depot(depot, amount)
        elif choice == 4:
            try:
                tn = int(input("Welcher Truck soll entladen? (1-4): ").strip())
                truck = trucks[tn]
            except (ValueError, KeyError):
                print("Ungültiger Truck-Name.")
                continue
            depot_name = truck.current_location
            if depot_name not in depots:
                print(f"{truck.name} kein Depot in {depot_name}.")
                continue
            depot = depots[depot_name]
            amount = int(input("Anzahl Paletten zum Entladen: ").strip())
            if amount <= truck.load:
                truck.unload_to_depot(depot, amount)
            else:
                print("Ungültige Menge, so viel hat der Truck nicht.")
        elif choice == 5:
            print("\n--- Simulation beendet ---")
            print("\n=== TRUCK-STATUS ===")
            for t in trucks.values():
                print(f"{t.name}: Ladung {t.load}/{t.capacity}, Kilometer: {t.mileage_km}")
            print("\n=== DEPOT-BESTÄNDE ===")
            for d in depots.values():
                print(f"{d.name}: Bestand {d.stock}/{d.capacity}")
            break
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

# Test der Klassen
#
#depot1 = Depot("Depot A", 100, 200)
#depot2 = Depot("Depot B", 50, 150)
#
#print(f"\n{depot1.name} hat {depot1.stock} Paletten auf Lager.")
#print(f"{depot2.name} hat {depot2.stock} Paletten auf Lager.")
#truck1 = Truck("Truck 1", "Berlin", 20, 0, 120000.0, depot = None)
#truck1.get_status()
#truck1.load_from_depot(depot1, 10)
#truck1.get_status()
#depot1.store_goods(truck1.load)
#print(f"Nach Lagerung hat {depot1.name} {depot1.stock} Paletten auf Lager.")
#truck1.drive_to("Leipzig")
#truck1.unload_to_depot(depot2, 5)
#truck1.get_status()
#print(f"\n{depot1.name} hat jetzt {depot1.stock} Paletten auf Lager.")
#print(f"{depot2.name} hat jetzt {depot2.stock} Paletten auf Lager.")

# Simulation starten
run_simulation()
