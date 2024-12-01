from Linkedlist import *
from Prac03act1Queue import *
from Prac03act1Stack import *
class DSAGraphEdge():
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def getWeight(self):
        return self.weight
    def __str__(self):
        return f'Source: {self.source}, Destination: {self.destination}, Weight: {self.weight}'

class DSAGraphVertex():
    def __init__(self, inlabel, invalue):
        self.label = inlabel
        self.value = invalue
        self.adjacencyList = DSADEDLList()
        self.addAdjacentEList = DSADEDLList()
    def getLabel(self):
        return self.label
    def getValue(self):
        return self.value
    def getAdjacent(self):
        return self.adjacencyList
    def getAdjacentE(self):
        return self.addAdjacentEList
    def addAdjacent(self, vertex):
        self.adjacencyList.insertLast(vertex)
    def addAdjacentE(self, edge, weight):
        edge = DSAGraphEdge(self, edge, weight)
        self.addAdjacentEList.insertLast(edge)
    def addEdge(self, edge):
        self.addAdjacentEList.insertLast(edge)
    def deleteEdge(self, edge):
        self.addAdjacentEList.removeLast(edge)
    def setVisited(self):
        self.visited = True
    def clearVisited(self):
        self.visited = False
    def getVisited(self):
        return self.visited
    def toString(self):
        return f"Vertex's label: {self.getLabel()} and value: {self.getValue}"
    def getEdge(self, label):
        current_edge_node = self.addAdjacentEList.head
        while current_edge_node is not None:
            adjacent_node = current_edge_node.getValue()
            # print("Node", self.getLabel())
            # print(f"Edge from", adjacent_node.getSource().getLabel(), "to", adjacent_node.getDestination().getLabel())
            if adjacent_node.getDestination().getLabel() == label:
                return adjacent_node
            current_edge_node = current_edge_node.getNext()
    def print_adjacent(self):
        current_vertex_node = self.adjacencyList.head
        if current_vertex_node is None:
            print("No adjacent vertices.")
            return
        while current_vertex_node.getNext() != None:
            print(f"{current_vertex_node.getValue().getLabel()}", end="\t")
            current_vertex_node = current_vertex_node.getNext()
        print(f"{current_vertex_node.getValue().getLabel()}")
    
    def get_sort_adjacent_list_unvisited(self):
        current_vertex_node = self.adjacencyList.head
        unvisited_list = []

        while current_vertex_node is not None:
            adjacent_vertex = current_vertex_node.getValue()
            if not adjacent_vertex.getVisited(): 
                unvisited_list.append(adjacent_vertex.getLabel())
            current_vertex_node = current_vertex_node.getNext()

        unvisited_list.sort()  
        return unvisited_list

class DSAGraph():
    def __init__(self):
        self.vertices = DSADEDLList()
        self.visited = False
    # def has_vertex(self, label):
    #     current_node = self.vertices.head
    #     is_contain_vertex = current_node.getValue().getLabel() == label
    #     while current_node.getNext() != None:
    #         current_node = current_node.getNext()
    #         if current_node.getValue().getLabel() == label:
    #             is_contain_vertex = True
    #     return is_contain_vertex
    def has_vertex(self, label):
        current_node = self.vertices.head
        while current_node is not None:
            if current_node.getValue().getLabel() == label:
                return True
            current_node = current_node.getNext()
        return False
    def addVertex(self, label, value = None):
        current_node = self.vertices.head
        if current_node == None or self.has_vertex(label) == False:
            graph_node = DSAGraphVertex(label, value)
            self.vertices.insertLast(graph_node)
        else:
            print("Vertex already exists!")
    
    def deleteNode(self, label):
        if not self.has_vertex(label):
            print(f"Vertex {label} does not exist!")
            return
        current_node = self.vertices.head
        prev_node = None
        while current_node is not None:
            if current_node.getValue().getLabel() == label:
                if prev_node is None:
                    self.vertices.head = current_node.getNext()  
                else:
                    prev_node.setNext(current_node.getNext())  
            prev_node = current_node
            current_node = current_node.getNext()

        current_node = self.vertices.head
        while current_node is not None:
            vertex = current_node.getValue()
            adjacency_list = vertex.getAdjacent()
            adjacent_node = adjacency_list.head
            prev_adjacent_node = None

            while adjacent_node is not None:
                adjacent_vertex = adjacent_node.getValue()
                if adjacent_vertex.getLabel() == label:
                    if prev_adjacent_node is None:
                        adjacency_list.head = adjacent_node.getNext()  
                    else:
                        prev_adjacent_node.setNext(adjacent_node.getNext())  

                prev_adjacent_node = adjacent_node
                adjacent_node = adjacent_node.getNext()

            current_node = current_node.getNext()

        print(f"Vertex {label} and all associated edges have been removed.")

        
    def deleteEdge(self,label1, label2):
        # Check if both vertices exist
        if self.has_vertex(label1) and self.has_vertex(label2):
            v1 = self.getVertex(label1)
            v2 = self.getVertex(label2)
            
            # Check if they are adjacent (i.e., there's an edge between them)
            if self.isAdjacent(label1, label2):
                # Remove vertex2 from vertex1's adjacency list
                adjacency_list_v1 = v1.getAdjacent()
                current_node = adjacency_list_v1.head
                prev_node = None

                while current_node is not None:
                    if current_node.getValue().getLabel() == label2:
                        if prev_node is None:
                            adjacency_list_v1.head = current_node.getNext()  # Remove head if it's the matching node
                        else:
                            prev_node.setNext(current_node.getNext())  # Bypass the current node to delete it
                    prev_node = current_node
                    current_node = current_node.getNext()

                # Remove vertex1 from vertex2's adjacency list
                adjacency_list_v2 = v2.getAdjacent()
                current_node = adjacency_list_v2.head
                prev_node = None

                while current_node is not None:
                    if current_node.getValue().getLabel() == label1:
                        if prev_node is None:
                            adjacency_list_v2.head = current_node.getNext()  # Remove head if it's the matching node
                        else:
                            prev_node.setNext(current_node.getNext())  # Bypass the current node to delete it
                    prev_node = current_node
                    current_node = current_node.getNext()

                print(f"Edge between {label1} and {label2} has been deleted.")
            else:
                print(f"No edge exists between {label1} and {label2}.")
        else:
            print(f"One or both vertices ({label1}, {label2}) not found!")
    # def addEdge(self, label1, label2):
    #     if self.has_vertex(label1) and self.has_vertex(label2):
    #         if not self.isAdjacent(label1, label2):
    #             self.getVertex(label1).addAdjacentE(
    #                 self.getVertex(label2))
    #             self.getVertex(label2).addAdjacentE(
    #                 self.getVertex(label1)) 
    #     else:
    #         print(f"One or both vertices ({label1}, {label2}) not found!")
    def addEdge(self, label1, label2, weight):
        if self.has_vertex(label1) and self.has_vertex(label2):
            if not self.isAdjacent(label1, label2):
                self.getVertex(label1).addAdjacentE(
                    self.getVertex(label2), weight)
                self.getVertex(label2).addAdjacentE(
                    self.getVertex(label1), weight) 
                self.getVertex(label1).addAdjacent(
                    self.getVertex(label2))
                self.getVertex(label2).addAdjacent(
                    self.getVertex(label1)) 
        else:
            print(f"One or both vertices ({label1}, {label2}) not found!")
    def getVertexCount(self):
        return len(self.vertices)
    def getVertex(self, label):
        current_node = self.vertices.head
        if current_node.getValue().getLabel() == label:
            return current_node.getValue()
        while current_node.getNext() != None:
            current_node = current_node.getNext()
            if current_node.getValue().getLabel() == label:
                return current_node.getValue()
        # else:
        #     print("Vertex isn't found!")

    def getAdjacent(self, label):
        if not self.has_vertex(label):
            print("Vertex isn't found!")
        current_node = self.vertices.head
        if current_node.getValue().getLabel() == label:
            return current_node.getValue().getAdjacent()
        while current_node.getNext() != None:
            current_node = current_node.getNext()
            if current_node.getValue().getLabel() == label:
                return current_node.getValue().getAdjacent()
                
    # def isAdjacent(self, label1, label2):
    #     if not self.has_vertex(label1) or not self.has_vertex(label2):
    #         print("Vertexes aren't found!")
    #     vertex_1_adjacent_list = self.getAdjacent(label1)
    #     current_node = vertex_1_adjacent_list.head
    #     if vertex_1_adjacent_list.isEmpty():
    #         return False
    #     if current_node.getValue().getLabel() == label2:
    #         return True
    #     while current_node.getNext() != None:
    #         current_node = current_node.getNext()
    #         if current_node.getValue().getLabel() == label2:
    #             return True
    #     return False
    def isAdjacent(self, label1, label2):
        if not self.has_vertex(label1) or not self.has_vertex(label2):
            print("Vertexes aren't found!")
        vertex_1_adjacent_list = self.getAdjacent(label1)
        current_node = vertex_1_adjacent_list.head
        if vertex_1_adjacent_list.isEmpty():
            return False
        if current_node == label2:
            return True
        while current_node.getNext() != None:
            current_node = current_node.getNext()
            if current_node == label2:
                return True
        return False

    def displayAsList(self):
        if self.vertices.isEmpty():
            print("No vertices!")
        else:
            current_node = self.vertices.head
            print("The adjacency list of the graph is:")
            while current_node.getNext() != None:
                print(f"{current_node.getValue().getLabel()}", end="\t")
                current_node.getValue().print_adjacent()
                current_node = current_node.getNext()

            print(f"{current_node.getValue().getLabel()}", end="\t")
            current_node.getValue().print_adjacent()

    def printmatrixnode(self, row_node, col_node):
        if self.isAdjacent(row_node.getValue().getLabel(), col_node.getValue().getLabel()):
            print("1".ljust(8), end="")
        else:
            print("0".ljust(8), end="")
    
    def print_matrix_line(self, row_node):
        print(f"{row_node.getValue().getLabel()}".ljust(8), end="")
        col_node = self.vertices.head
        while col_node.getNext() != None:
            self.printmatrixnode(row_node, col_node)
            col_node = col_node.getNext()

        self.printmatrixnode(row_node, col_node)
        
    def displayAsMatrix(self):
        if self.vertices.isEmpty():
            print("There is no vertices in the graph to display")
        else:
            print("The adjacency matrix representation of the graph is")
            current_node = self.vertices.head
            print(" " * 8, end="")
            while current_node.getNext() != None:
                print(f"{current_node.getValue().getLabel()}".ljust(8), end="")
                current_node = current_node.getNext()
            print(f"{current_node.getValue().getLabel()}".ljust(8), end="")
            print()

            row_node = self.vertices.head
            while row_node.getNext() != None:
                self.print_matrix_line(row_node)
                row_node = row_node.getNext()
                print()

            self.print_matrix_line(row_node)
            print()

    def print_traversal(self, t_queue):
        print("{", end="")
        i = 0
        while not t_queue.isEmpty():
            if i % 2 == 0:
                if i == 0:
                    print(f"({t_queue.dequeue().getLabel()},", end="")
                else:
                    print(f",({t_queue.dequeue().getLabel()},", end="")
            else:
                print(f"{t_queue.dequeue().getLabel()})", end="")
            i += 1
        print("}")
    
    # def print_traversal(self, t_queue):
    #     traverse = DSADEDLList()
    #     i = 0
    #     while not t_queue.isEmpty():
    #         if i % 2 == 0:
    #             if i == 0:
    #                 traverse.insertLast(t_queue.dequeue().getLabel())
    #                 # print(f"({t_queue.dequeue().getLabel()},", end="")
    #             else:
    #                 traverse.insertLast(t_queue.dequeue().getLabel())
    #                 # print(f",({t_queue.dequeue().getLabel()},", end="")
    #         else:
    #             print(f"{t_queue.dequeue().getLabel()}", end="")
    #         i += 1
    #     traverse.printList()

    # def breadthFirstSearch(self):
    #     t_queue = DSAQueue()
    #     q_queue = DSAQueue()

    #     current_vertex = self.vertices.head
    #     while current_vertex.getNext() != None:
    #         current_vertex.getValue().clearVisited()
    #         current_vertex = current_vertex.getNext()
    #     current_vertex.getValue().clearVisited()

    #     current_vertex = self.vertices.head
    #     current_vertex.getValue().setVisited()
    #     q_queue.enqueue(current_vertex.getValue())

    #     while not q_queue.isEmpty():
    #         vertex = q_queue.dequeue()
    #         vertex_adjacent_list_unvisited = vertex.get_sort_adjacent_list_unvisited()
    #         for w_label in vertex_adjacent_list_unvisited:
    #             w_vertex = self.getVertex(w_label)
    #             t_queue.enqueue(vertex)
    #             t_queue.enqueue(w_vertex)
    #             w_vertex.setVisited()
    #             q_queue.enqueue(w_vertex)

    #     # print the breadth_first_search
    #     self.print_traversal(t_queue)
  

    def breadthFirstSearch(self,source, destination):
        t_queue = DSAQueue()
        q_queue = DSAQueue()
        if self.getVertex(source) is None or self.getVertex(destination) is None:
            return ("Source/Destination not found!")
        if source == destination:
            return("That's the same place!")
        current_vertex = self.getVertex(source)
        current_vertex = self.vertices.head
        while current_vertex.getNext() != None:
            current_vertex.getValue().clearVisited()
            current_vertex = current_vertex.getNext()
        current_vertex.getValue().clearVisited()

        current_vertex = self.vertices.head
        current_vertex.getValue().setVisited()
        q_queue.enqueue(current_vertex.getValue())

        while not q_queue.isEmpty():
            vertex = q_queue.dequeue()
            if vertex.getLabel() == destination:
                return True
            vertex_adjacent_list_unvisited = vertex.get_sort_adjacent_list_unvisited()
            for w_label in vertex_adjacent_list_unvisited:
                w_vertex = self.getVertex(w_label)
                t_queue.enqueue(vertex)
                t_queue.enqueue(w_vertex)
                w_vertex.setVisited()
                q_queue.enqueue(w_vertex)

        # print the breadth_first_search
        # self.print_traversal(t_queue)
        return False
    
    # def depth_first_search(self):
    #     t_queue = DSAQueue()  
    #     s_stack = DSAStack()  

    #     current_vertex = self.vertices.head
    #     while current_vertex.getNext() is not None:
    #         current_vertex.getValue().clearVisited()
    #         current_vertex = current_vertex.getNext()
    #     current_vertex.getValue().clearVisited()

    #     current_vertex = self.vertices.head.getValue()
    #     current_vertex.setVisited()
    #     s_stack.push(current_vertex)

    #     while not s_stack.isEmpty():
    #         current_vertex = s_stack.top()  
    #         vertex_adjacent_list_unvisited = current_vertex.get_sort_adjacent_list_unvisited()

    #         if vertex_adjacent_list_unvisited: 
    #             next_vertex_label = vertex_adjacent_list_unvisited[0]
    #             next_vertex = self.getVertex(next_vertex_label)
                
    #             t_queue.enqueue(current_vertex)  
    #             t_queue.enqueue(next_vertex)
                
    #             next_vertex.setVisited()
    #             s_stack.push(next_vertex) 
    #         else:
    #             s_stack.pop()  

    #     self.print_traversal(t_queue)

    def depth_first_search(self, source, destination):
        self.shortest_path = None
        self.shortest_distance = float('inf')

    
   
    
 


    
    