from graph import *

if __name__ == "__main__":
    nodes_to_add = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    edges_to_add = [
        ("A", "B", 2),
        ("A", "C", 3),
        ("B", "C", 1),
        ("C", "D", 4),
        ("D", "E", 2),
        ("A", "F", 5),
        ("B", "G", 2),
        ("G", "H", 3),
        ("C", "I", 1),
        ("E", "F", 2),
        ("F", "H", 4),
        ("I", "D", 3),
        ("A", "D", 6),
        ("B", "E", 7),
        ("C", "F", 5),
        ("D", "G", 2),
        ("E", "H", 1),
        ("F", "I", 4),
        ("G", "J", 3),
        ("H", "K", 2),
        ("I", "L", 5),
        ("J", "M", 2),
        ("K", "N", 4),
        ("L", "O", 1),
        ("M", "P", 3),
        ("N", "Q", 7),
        ("O", "R", 2),
        ("P", "S", 3),
        ("Q", "T", 4),
        ("R", "U", 1),
        ("S", "V", 2),
        ("T", "W", 5),
        ("U", "X", 6),
        ("V", "Y", 3),
        ("W", "Z", 2),
        ("W", "M", 15),
        ("X", "Q", 23),
    ]

    my_graph = Graph(nodes=nodes_to_add, edges=edges_to_add)

    # Visualize the graph
    my_graph.visualize('red')

    # Find the shortest path from "A" to "G"
    start_node = "A"
    end_node = "Q"
    shortest_path = my_graph.dijkstra(start_node, end_node)

    if shortest_path:
        print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path from {start_node} to {end_node}")
