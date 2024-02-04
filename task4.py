import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt

class MinHeapNode:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.key < other.key

def add_heap_edges(graph, heap, pos, x=0, y=0, parent_idx=0):
    if parent_idx < len(heap):
        node = heap[parent_idx]
        graph.add_node(node.id, color=node.color, label=node.key)

        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx < len(heap):
            left_child = heap[left_child_idx]
            graph.add_edge(node.id, left_child.id)
            l = x - 1 / 2 ** (y + 1)
            pos[left_child.id] = (l, y - 1)
            add_heap_edges(graph, heap, pos, x=l, y=y - 1, parent_idx=left_child_idx)

        if right_child_idx < len(heap):
            right_child = heap[right_child_idx]
            graph.add_edge(node.id, right_child.id)
            r = x + 1 / 2 ** (y + 1)
            pos[right_child.id] = (r, y - 1)
            add_heap_edges(graph, heap, pos, x=r, y=y - 1, parent_idx=right_child_idx)


def draw_heap(min_heap):
    heap_graph = nx.DiGraph()
    pos = {node.id: (0, 0) for node in min_heap}
    add_heap_edges(heap_graph, min_heap, pos)

    colors = [node[1].get('color', 'skyblue') for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1].get('label', '') for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення бінарної купи
min_heap = [MinHeapNode(8), MinHeapNode(5), MinHeapNode(7), MinHeapNode(3), MinHeapNode(1), MinHeapNode(6), MinHeapNode(4)]

# Відображення бінарної купи
draw_heap(min_heap)
