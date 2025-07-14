# Sample directed graph represented as an adjacency list.
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# DFS = Depth-First Search (uses stack - LIFO)
def dfsPrint(graph, source):
    # Initialize a stack with the source node
    stack = [source]

    # Keep going until the stack is empty
    while len(stack) > 0:
        current = stack.pop()  # Pop the last element
        print(current)  # Visit the node

        # Push neighbors to the stack (in reverse for correct order)
        for neighbor in reversed(graph[current]):
            stack.append(neighbor)

dfsPrint(graph, "a")

# BFS = Breadth-First Search (uses queue - FIFO)
from collections import deque

def bfsPrint(graph, source):
    # Initialize a queue with the source node
    queue = deque([source])

    # Keep going until the queue is empty
    while queue:
        current = queue.popleft()  # Remove from the front of the queue
        print(current)  # Visit the node

        # Add all neighbors to the end of the queue
        for neighbor in graph[current]:
            queue.append(neighbor)
