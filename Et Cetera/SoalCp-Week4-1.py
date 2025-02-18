class Vehicle:
    def __init__(self, vehicle_type, distance):
        self.vehicle_type = vehicle_type
        self.distance = distance

# Fungsi untuk menghitung total jarak
def calculate_total_distance(vehicles):
    total_distance = sum(vehicle.distance for vehicle in vehicles)
    return total_distance

# Input
n = int(input("Enter the number of vehicles: "))
vehicles = []

for _ in range(n):
    vehicle_type, distance = input().split()
    distance = int(distance)
    vehicles.append(Vehicle(vehicle_type, distance))

# Output
total_distance = calculate_total_distance(vehicles)
print(f"Total distance: {total_distance}")
