# Autonomous Vehicle Management System

This project implements an **Autonomous Vehicle Management System** that combines concepts of data structures and algorithms to manage road networks and vehicles effectively. It is designed as part of a final assignment for COMP5008 - Semester 2, 2024.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Implementation Details](#implementation-details)
  - [Graph Class](#graph-class-road-network)
  - [Vehicle Hash Table](#vehicle-hash-table)
  - [Vehicle Class](#vehicle-class)
- [Setup and Usage](#setup-and-usage)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview
The project integrates various data structures and algorithms to solve the problem of managing a fleet of autonomous vehicles within a defined road network. It focuses on the following:
1. **Road Network (Graph)**: Represent locations as vertices and roads as edges with distances as weights.
2. **Vehicle Management (Hash Table)**: Handle insertion, deletion, searching, and displaying vehicle information.
3. **Autonomous Vehicle Features**: Maintain details such as vehicle ID, location, destination, distance, and battery level.

---

## Features
- **Road Network Operations**:
  - Add locations and roads with distances.
  - Retrieve neighboring locations.
  - Display the road network as adjacency lists or matrices.
  - Check if a path exists between two locations.
  - Find all possible paths between two locations.
- **Vehicle Management**:
  - Insert, delete, and search for vehicles.
  - Manage vehicle details (location, battery level, etc.).
- **Algorithm Usage**:
  - Implement **Breadth-First Search (BFS)** to check path existence.
  - Use **Depth-First Search (DFS)** to find all possible paths.
  - Apply hash table techniques for efficient vehicle management.

---

## Implementation Details

### Graph Class: Road Network
The **Graph Class** represents the road network using vertices (locations) and edges (roads).
- **`addLocation(location)`**: Add a location (vertex) to the graph.
- **`addRoad(location1, location2, distance)`**: Add a road (edge) between two locations with a specified distance.
- **`retrieve_neighbors(location)`**: List all locations connected to a specific location.
- **`is_path(source, destination)`**: Check if a path exists between two locations using BFS.
- **`find_all_path(source, destination)`**: Find all possible paths between two locations using DFS.

### Vehicle Hash Table
The **Hash Table** manages vehicles with operations for insertion, deletion, and searching. It ensures quick access to vehicle information using hash functions and collision handling techniques.

### Vehicle Class
The **Vehicle Class** stores details such as:
- Vehicle ID
- Current location and destination
- Distance traveled
- Battery level

It also provides methods for setting and retrieving these attributes.

---

## Setup and Usage

