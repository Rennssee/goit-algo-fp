import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class MinHeapNode:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key


def build_heap_tree(heap_array):
    min_heap = [MinHeapNode(key) for key in heap_array]
    for i in range(len(min_heap)):
        if i * 2 + 1 < len(min_heap):
            min_heap[i].left = min_heap[i * 2 + 1]
        if i * 2 + 2 < len(min_heap):
            min_heap[i].right = min_heap[i * 2 + 2]
    return min_heap[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.key)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_tree_root):
    heap_graph = nx.DiGraph()
    pos = {heap_tree_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_tree_root, pos)

    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


# Побудова бінарної купи з заданого масиву
heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
heapq.heapify(heap_array)
heap_tree_root = build_heap_tree(heap_array)

# Візуалізація бінарної купи
draw_heap(heap_tree_root)
