from Assignment import *

graph = Graph()
vehicle_hashtable = VehicleHashTable()
option = input("Choose one option: A: Add Location, B: Add Road, C: Display Road Network, D: Check path existence, E: Add Vehicle, F: Remove Vehicle, G: Display All Vehicles, H:Search for a Vehicle, I: Find nearest Vehicle, K: Find Vehicle with highest battery, X: Exit: ").upper()
while option != 'X':
    if option == 'A':
        location = input("Enter the Location: ").upper()
        graph.addLocation(location)
        print(f"{location} has successfully been added!")
    elif option == 'B':
        location1 = input("Enter Location 1: ").upper()
        location2 = input("Enter Location 2: ").upper()
        distance = int(input("Enter the distance: "))
        graph.addRoad(location1, location2, distance)
        print(f"Road between {location1} and {location2} with distance {distance} has successfully been added!")
    elif option == 'C':
        network = input("How would you like to display the network? A: As List, B: As Matrix: ").upper()
        if network == 'A':
            graph.displayGraphL()
        else:
            graph.displayGraphM()
    elif option == 'D':
        source = input("Enter the source: ").upper()
        destination = input("Enter the destination: ").upper()
        print(graph.is_path(source, destination))
    elif option == 'E':
        current_location = input("Enter Vehicle's current location: ").upper()
        current_destination = input("Enter Vehicle's current destination: ").upper()
        battery_level = int(input("Enter Vehicle's battery level: "))
        vehicle1 = Vehicle(current_location, current_destination, battery_level)
        print(f"Vehicle from {current_location} to {current_destination} with battery level {battery_level} has successfully been added!")
        vehicle_hashtable.putVe(vehicle1.vehicle_id, vehicle1)
    elif option == 'F':
        ID = input("Please input the vehicle ID: ")
        Vehicle.vehicle_hash_table.deleteVe(ID)
        print(f"Vehicle {ID} has been removed!")
    elif option == 'G':
        vehicle_hashtable.displayVe()
    elif option == 'H':
        ID = input("Please input the vehicle ID: ")
        print(Vehicle.vehicle_hash_table.search(ID))
    elif option == 'I':
        graph.find_nearest_vehicle(vehicle_hashtable)
    elif option == 'K':
        print(graph.find_vehicle_with_highest_battery(vehicle_hashtable))
            

    option = input("Choose one option: A: Add Location, B: Add Road, C: Display Road Network, D: Check path existence, E: Add Vehicle, F: Remove Vehicle, G: Display All Vehicles, H:Search for a Vehicle, I: Find nearest Vehicle, K: Find Vehicle with highest battery, X: Exit: ").upper()