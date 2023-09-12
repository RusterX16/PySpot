import heapq

import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self, nodes=None, edges=None):
        self.graph = {}

        if nodes is not None:
            self.add_nodes(nodes)

        if edges is not None:
            self.add_edges(edges)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, length=1):
        if length <= 0:
            raise ValueError("Edge length must be a positive integer")

        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def add_nodes(self, nodes):
        for node in nodes:
            if node not in self.graph:
                self.graph[node] = []

    def add_edges(self, edges, length=1):
        if length <= 0:
            raise ValueError("Edge length must be a positive integer")

        for node1, node2, edge_length in edges:
            if node1 in self.graph and node2 in self.graph:
                self.graph[node1].append((node2, edge_length))
                self.graph[node2].append((node1, edge_length))

    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                if (node, neighbor) not in edges and (neighbor, node) not in edges:
                    edges.append((node, neighbor))
        return edges

    def is_null(self):
        return len(self.graph) == 0

    def is_trivial(self):
        return len(self.graph) == 1 and len(list(self.graph.values())[0]) == 0

    def is_regular(self):
        degrees = [len(neighbors) for neighbors in self.graph.values()]
        return all(deg == degrees[0] for deg in degrees)

    def is_complete(self):
        num_nodes = len(self.get_nodes())
        return len(self.get_edges()) == (num_nodes * (num_nodes - 1)) / 2

    def degree(self, node):
        if node in self.graph:
            return len(self.graph[node])
        else:
            return 0

    def has_cycle(self):
        def is_cyclic_util(node, visited, parent):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if is_cyclic_util(neighbor, visited, node):
                        return True
                elif parent != neighbor:
                    return True
            return False

        visited = {node: False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if is_cyclic_util(node, visited, None):
                    return True
        return False

    def get_subgraph(self, selected_nodes):
        subgraph = Graph()

        # Add selected nodes to the subgraph
        for node in selected_nodes:
            if node in self.graph:
                subgraph.add_node(node)

        # Add edges between selected nodes in the subgraph
        for node1 in selected_nodes:
            if node1 in self.graph:
                for node2 in self.graph[node1]:
                    if node2 in selected_nodes:
                        subgraph.add_edge(node1, node2)

        return subgraph

    def to_matrix(self):
        nodes = self.get_nodes()
        matrix = [["0"] * (len(nodes) + 1) for _ in range(len(nodes) + 1)]

        # Set a special character in cell [0][0]
        matrix[0][0] = " "  # Replace "X" with your special character

        # Fill the header row and column with node names
        for i, node in enumerate(nodes, start=1):
            matrix[0][i] = matrix[i][0] = node

        # Fill in the matrix based on edges
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if node2 in self.graph[node1]:
                    matrix[i + 1][j + 1] = "1"

        return matrix

    def to_list(self):
        adjacency_list = {}
        for node, neighbors in self.graph.items():
            adjacency_list[node] = neighbors

        return adjacency_list

    def visualize(self, node_color='skyblue'):
        G = nx.Graph()
        G.add_nodes_from(self.graph.keys())

        edge_labels = {}  # Dictionary to store edge labels

        for node, neighbors in self.graph.items():
            for neighbor, length in neighbors:
                G.add_edge(node, neighbor)
                edge_labels[(node, neighbor)] = length  # Edge length as label

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_color, font_size=10, font_color='black', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
        plt.show()

    def dijkstra(self, start_node, end_node):
        if start_node not in self.graph or end_node not in self.graph:
            return None

        distances = {node: float('inf') for node in self.graph}
        predecessors = {node: None for node in self.graph}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, edge_length in self.graph[current_node]:
                distance = distances[current_node] + edge_length

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        while end_node:
            path.insert(0, end_node)
            end_node = predecessors[end_node]

        return path if path[0] == start_node else None

    def __str__(self):
        graph_str = ""
        for node, neighbors in self.graph.items():
            if neighbors:
                neighbors_str = " -> ".join(neighbors)
                graph_str += f"{node} -> {neighbors_str}\n"
            else:
                graph_str += f"{node}\n"
        return graph_str
