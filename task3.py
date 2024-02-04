import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.vertices[from_vertex][to_vertex] = weight

    def dijkstra(self, start_vertex):
        heap = [(0, start_vertex)]  # (distance, vertex)
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Приклад використання:
if __name__ == "__main__":
    # Створення графа
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)

    # Запуск алгоритму Дейкстри
    start_vertex = "A"
    shortest_paths = graph.dijkstra(start_vertex)

    # Виведення результатів
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"To {vertex}: {distance}")
