def calculate_fare(distance):
    base_fare = 50
    per_km_rate = 10
    return base_fare + (distance * per_km_rate)

def total_fare(trips):
    total = 0
    for i, distance in enumerate(trips, start=1):
        fare = calculate_fare(distance)
        total += fare
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total}")

# Example input
trips = [5, 10, 3]

# Output
total_fare(trips)
