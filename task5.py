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


def add_heap_edges(graph, heap, pos, x=0, y=0, parent_idx=0):
    if parent_idx < len(heap):
        node = heap[parent_idx]
        graph.add_node(node.id, color=node.color, label=node.key)

        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx < len(heap):
            left_child = heap[left_child_idx]
            node.left = left_child
            graph.add_edge(node.id, left_child.id)
            l = x - 1 / 2 ** (y + 1)
            pos[left_child.id] = (l, y - 1)
            add_heap_edges(graph, heap, pos, x=l, y=y - 1, parent_idx=left_child_idx)

        if right_child_idx < len(heap):
            right_child = heap[right_child_idx]
            node.right = right_child
            graph.add_edge(node.id, right_child.id)
            r = x + 1 / 2 ** (y + 1)
            pos[right_child.id] = (r, y - 1)
            add_heap_edges(graph, heap, pos, x=r, y=y - 1, parent_idx=right_child_idx)


def dfs_traversal(root, colors):
    visited = set()
    stack = [root]

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(len(visited))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs_traversal(root, colors):
    visited = set()
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(len(visited))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def generate_color(position):
    # Генерація кольору на основі позиції в обході
    hue = position % 16 / 16.0
    rgb_color = plt.cm.hsv(hue)[:3]
    hex_color = "#{:02X}{:02X}{:02X}".format(
        int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255)
    )
    return hex_color


def draw_tree_traversals(min_heap):
    heap_graph_dfs = nx.DiGraph()
    pos_dfs = {node.id: (0, 0) for node in min_heap}
    add_heap_edges(heap_graph_dfs, min_heap, pos_dfs)
    colors_dfs = {}
    dfs_traversal(min_heap[0], colors_dfs)
    draw_heap(heap_graph_dfs, pos_dfs, colors_dfs)

    heap_graph_bfs = nx.DiGraph()
    pos_bfs = {node.id: (0, 0) for node in min_heap}
    add_heap_edges(heap_graph_bfs, min_heap, pos_bfs)
    colors_bfs = {}
    bfs_traversal(min_heap[0], colors_bfs)
    draw_heap(heap_graph_bfs, pos_bfs, colors_bfs)


def draw_heap(heap_graph, pos, colors):
    labels = {node[0]: node[1].get("label", "") for node in heap_graph.nodes(data=True)}
    nodes_order = [
        node[0]
        for node in sorted(
            heap_graph.nodes(data=True), key=lambda x: x[1].get("label", "")
        )
    ]
    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=[colors[node] for node in nodes_order],
        nodelist=nodes_order,
    )
    plt.show()


# Створення бінарної купи
min_heap = [
    MinHeapNode(8),
    MinHeapNode(5),
    MinHeapNode(7),
    MinHeapNode(3),
    MinHeapNode(1),
    MinHeapNode(6),
    MinHeapNode(4),
]

# Відображення бінарної купи з обходами
draw_tree_traversals(min_heap)
