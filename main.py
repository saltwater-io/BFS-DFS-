from _collections import deque


class Stack:
    def __init__(self):  # initial constructor
        self.items = []

    def isEmpty(self):  # is stack empty?
        return self.items == []

    def push(self, item):  # Pushes item onto stack
        self.items.append(item)

    def pop(self):  # Pops item off stack
        return self.items.pop()

    def peek(self):  # Peeks at the last value added to stack
        return self.items[len(self.items) - 1]

    def size(self):  # Returns size of stack
        return len(self.items)


def BFS(graph):
    # Traveled is a list that stores already visited nodes
    traveled = []
    connected_nodes = []
    queue = deque()
    queue.append(1)
    traveled.append(1)
    bfs = []
    while queue:  #
        # for i in range(1,7):
        i = queue.popleft()
        bfs.append(i)
        # traveled.append(i)
        for m in graph[i]:
            if m not in traveled:
                connected_nodes.append(m)
        for n in connected_nodes:
            queue.append(n)
            traveled.append(n)
        connected_nodes.clear()
    print("BFS: ")
    print(bfs)


def DFS(graph):
    # Traveled is a list that stores already visited nodes
    traveled = []
    connected_nodes = []
    stack = Stack()
    stack.push(1)
    traveled.append(1)
    dfs = []
    while not stack.isEmpty():  #
        # for i in range(1,7):
        i = stack.pop()
        dfs.append(i)
        # traveled.append(i)
        for m in graph[i]:
            if m not in traveled:
                connected_nodes.append(m)
        for n in connected_nodes:
            stack.push(n)
            traveled.append(n)
        connected_nodes.clear()
    print("DFS: ")
    print(dfs)


def main():
    queue = deque()
    stack = Stack()

    # Non-weighted undirected graph
    # V: [List of U's]
    # V connected to U

    graph = {
        1: [2, 3],
        2: [1, 5, 4],
        3: [1, 5],
        4: [2, 5, 6],
        5: [6, 4, 2, 3],
        6: [4, 5]
    }

    BFS(graph)
    DFS(graph)


if __name__ == "__main__":
    main()
