from Graph import *
from Hash import *
import numpy as np
from quicksort import *
from Heap import *

class PathNode:
    def __init__(self, path=None, distance=0):
        self.path = path
        self.distance = distance
        self.next = None

class PathLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_path(self, path, distance):
        new_path = PathNode(path.copy(), distance)
        if self.head is None:
            self.head = new_path
            self.count += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_path
            self.count += 1
    def print_paths(self):
        current = self.head
        while current:
            current.path.printPathList()
            print("Distance: ", current.distance)
            current = current.next

class Graph():
    def __init__(self):
        self.graph = DSAGraph()
        self.graph1 = DSADEDLList()
        self.vertices = DSADEDLList()
        # self.vistied = False
    # def hasRoad(self, location):
    #     return self.graph.has_vertex(location)
    def addLocation(self, location):
        self.graph.addVertex(location)
    def addRoad(self, location1, location2, distance):
        self.graph.addEdge(location1, location2, distance)
    def retrieve_neighbors(self, location):
        return self.graph.getAdjacent(location)
    def displayGraphL(self):
        self.graph.displayAsList()
    def displayGraphM(self):
        self.graph.displayAsMatrix()
    def is_path(self, source, destination):
        return self.graph.breadthFirstSearch(source, destination)
    def find_all_paths(self, source, destination):
        self.all_paths = PathLinkedList()
        visited = DSADEDLList()
        path = DSADEDLList()
        self.dfs_find_path(source, destination, visited, path, 0)
        return self.all_paths
    def dfs_find_path(self, current, destination, visited, path, distance):
        visited.insertLast(current)
        path.insertLast(current)
        if current == destination:
            self.all_paths.add_path(path, distance)
        else:
            for neighbor in self.graph.getAdjacent(current):
                if neighbor.getLabel() not in visited:
                    edge_weight = neighbor.getEdge(current).getWeight()
                    self.dfs_find_path(neighbor.getLabel(), destination, visited, path, distance + edge_weight)
        path.removeLast()
        visited.removeLast()

    def get_best_path(self, vehicle):
        all_paths = self.find_all_paths(vehicle.getLocation(), vehicle.getDestination())

        heap = DSAHeap(all_paths.count)
        current = self.all_paths.head
        while current:
            heap.add(current.distance, current.path)
            current = current.next
        
        heap.heapSort(all_paths.count)
        vehicle.setDistancetoDestination(heap.heapArr[0].getPriority())
        return heap.heapArr[0]

    def find_nearest_vehicle(self, vehicles):
        heap = DSAHeap(vehicles.hash.count)
        for vehicle_hash_entry in vehicles.hash.hashArray:
            if vehicle_hash_entry.value != None:
                self.get_best_path(vehicle_hash_entry.value)
                heap.add(vehicle_hash_entry.value.getDistancetoDestination(), vehicle_hash_entry.value)
        
        heap.heapSort(vehicles.hash.count)
        print(heap.heapArr[0].value)

    def find_vehicle_with_highest_battery(self, vehicles):
        vehicle_arr = np.empty(vehicles.hash.count, dtype= object)
        index = 0
        for vehicle_hash_entry in vehicles.hash.hashArray:
            if vehicle_hash_entry.value != None:
                vehicle_arr[index] = vehicle_hash_entry.value
                index += 1
        QuickSort(vehicle_arr, 0, (len(vehicle_arr) - 1))
        return vehicle_arr[0]
             

# graph = Graph()
# graph.addLocation('A')
# graph.addLocation('B')
# graph.addLocation('C')
# graph.addLocation('D')
# graph.addRoad("A", "B", 1)
# graph.addRoad("B", "C", 2)
# graph.addRoad("A", "C", 5)
# graph.addRoad("B", "D", 4)
# graph.addRoad("C", "D", 1)

# print(graph.graph.getVertex("A"))

# all_paths = graph.find_all_paths("A", "D")
# print("All paths from A to D with their distances:")
# all_paths.print_paths()

# distance = graph.calculate_total_distance('A','D')
# print(distance)

class VehicleHashTable():
    def __init__(self):
        self.hash = DSAHashTable(10)
    def putVe(self, ID, value):
        self.hash.put(ID, value)
    def deleteVe(self, ID):
        self.hash.remove(ID)
    def search(self, ID):
        return self.hash.get(ID)
    def displayVe(self):
        self.hash.printTable()
    
class Vehicle():
    vehicle_count = 0
    battery_level = [] #check again
    
    def __init__(self, current_location, current_destination, battery_level):
        Vehicle.vehicle_count += 1
        self.vehicle_id = f"VHE0{Vehicle.vehicle_count}"
        self.current_location = current_location
        self.current_destination = current_destination
        self.battery_level = battery_level
        Vehicle.battery_level.append(self.battery_level)
     
    def __repr__(self):
        return f"Vehicle(current location: '{self.current_location}', current destination: '{self.current_destination}', battery_level={self.battery_level})"
    
    def setLocation(self, location):
        self.current_location = location
    
    def setDestination(self, destination):
        self.current_destination = destination
    
    def setDistancetoDestination(self, distance): 
        self.distance = distance

    def setBatteryLevel(self, level):
        self.battery_level = level
    
    def getLocation(self):
        return self.current_location
    
    def getDestination(self):
        return self.current_destination
    
    def getDistancetoDestination(self): #need revising - hasn't printed values
        return self.distance
    
    def getBatteryLevel(self):
        return self.battery_level
    
    # def find_vehicle_with_highest_battery():
    #     array = QuickSort(Vehicle.battery_level, 0, (len(Vehicle.battery_level) - 1))
    #     return array[0]
                   
a = Graph()
a.addLocation('A')
a.addLocation('B')
a.addLocation('C')
a.addLocation('D')
a.addRoad('A','B', 30)
a.addRoad('B', 'C', 40)
a.addRoad('A','C', 90)
a.addRoad('C', 'D', 50)
a.retrieve_neighbors('A').printVertexList()
b = VehicleHashTable()
vehicle1 = Vehicle('A','B',20)
vehicle2 = Vehicle('A','B',100)
vehicle3 = Vehicle('A','B',50)
print(vehicle1)
b.putVe(vehicle1.vehicle_id, vehicle1)
b.putVe(vehicle2.vehicle_id, vehicle2)
b.putVe(vehicle3.vehicle_id, vehicle3)
b.displayVe()
a.find_nearest_vehicle(b)
print(a.find_vehicle_with_highest_battery(b))


# vehicle1 = Vehicle('A', 'C', 200)
# vehicle2 = Vehicle('C', 'D', 200)





# print(a.is_path('A', 'A'))

# vehicle2 = Vehicle('B','C', 300)
# vehicle3 = Vehicle('C', 'D', 150)
# vehicle4 = Vehicle('C', 'D', 100)
# vehicle5 = Vehicle('C', 'E', 400)

# vehicles = [vehicle2, vehicle3, vehicle4, vehicle5]

# highest_vehicle = Vehicle.find_vehicle_with_highest_battery(vehicles) # have to be included in the menu
# print("the highest battery level is:", highest_vehicle)


# print(vehicle1.vehicle_id)
# print(vehicle2.vehicle_id)
# print(vehicle3.vehicle_id)
# print(vehicle4.vehicle_id)

# c = VehicleHashTable()
# c.putVe(vehicle1.vehicle_id, vehicle1)
# c.putVe(vehicle2.vehicle_id, vehicle2)
# c.putVe(vehicle3.vehicle_id, vehicle3)
# c.putVe(vehicle4.vehicle_id, vehicle4)
# # c.putVe(vehicle5.vehicle_id, vehicle5)
# c.displayVe()
# print(vehicle1.vehicle_id)
# # c.deleteVe(vehicle1.vehicle_id)
# c.displayVe()
# print(c.search(vehicle1.vehicle_id))

# a.find_nearest_vehicle(c)
# print(a.find_vehicle_with_highest_battery(c))

# vehicle1 = Vehicle((4,2),(5,7),200)
# print(vehicle1.distace_calc())
# print(vehicle1.getLocation())
# vehicle1.setLocation((7,3))
# print(vehicle1.getLocation())
# print(vehicle1.distace_calc())
# print(vehicle1.getBatteryLevel())
# vehicle1.setBatteryLevel(100)
# print(vehicle1.getBatteryLevel())
# print(vehicle1.getDistancetoDestination())
