class Depot:
    def __init__(self, name: str, stock: int, capacity: int):
        self.name = name
        self.stock = stock        # in Paletten
        self.capacity = capacity  # in Paletten

    def provide_goods(self, amount:int) -> int:
        if amount > self.stock:
            provided = self.stock
            self.stock = 0
            return provided
        else:
            self.stock -= amount
            return amount
    def store_goods(self, amount:int) -> None:
        if self.stock + amount > self.capacity:
            raise ValueError("Depot Kapazität überschritten")
        self.stock += amount

class Truck:
    def __init__(self, name: str, current_location: str, capacity: int, load: int, mileage_km: float, depot: Depot):
        self.name = name
        self.current_location = current_location
        self.capacity = capacity  # in kg
        self.load = load          # in kg
        self.mileage_km = mileage_km
        self.depot = depot

    def get_status(self) -> str:
        print(f"\n{self.name}\n\\- Ort: {self.current_location},\n\\- Ladung: {self.load}/{self.capacity} Paletten,\n\\- Kilometerstand: {self.mileage_km} km")

    def drive_to(self, destination: str, distance_km: float) -> None:
        print(f"{self.name} fährt von {self.current_location} nach {destination} ({distance_km}km)")
        self.current_location = destination
        self.mileage_km += distance_km

    def load_from_depot(self, depot: Depot, amount: int) -> None:
        if amount > self.capacity - self.load:
            raise ValueError(f"{self.name} kann nur {self.capacity - self.load} Paletten laden (Kapazität erreicht).")
        self.load += amount
        print(f"{self.name} lädt {depot.provide_goods(amount)} Paletten aus dem {depot.name} auf.")

    def unload_to_depot(self, depot: Depot, amount: int) -> None:
        if amount > self.load:
            raise ValueError(f"Der {self.name} hat nur {self.load} Paletten geladen, kann aber nicht {amount} Paletten entladen.")
        self.load -= amount
        print(f"{self.name} entlädt {amount} Paletten im {depot.name}.")

# Test der Klassen
#
depot1 = Depot("Depot A", 100, 200)
depot2 = Depot("Depot B", 50, 150)
#
print(f"\n{depot1.name} hat {depot1.stock} Paletten auf Lager.")
print(f"{depot2.name} hat {depot2.stock} Paletten auf Lager.")
truck1 = Truck("Truck 1", "Berlin", 20, 0, 120000.0, depot = None)
truck1.get_status()
truck1.load_from_depot(depot1, 10)
truck1.get_status()
#depot1.store_goods(truck1.load)
#print(f"Nach Lagerung hat {depot1.name} {depot1.stock} Paletten auf Lager.")
truck1.drive_to("Leipzig", 910.0)
truck1.unload_to_depot(depot2, 5)
truck1.get_status()
print(f"\n{depot1.name} hat jetzt {depot1.stock} Paletten auf Lager.")
print(f"{depot2.name} hat jetzt {depot2.stock} Paletten auf Lager.")



