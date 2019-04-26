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

# Returns BFS of a undirected, non-weighted graph
def BFS(graph):
    # Traveled is a list that stores already visited nodes
    traveled = []
    # Queue
    queue = deque()
    # Starts at vertex 1
    queue.append(1)
    traveled.append(1)
    # Actual path
    bfs = []
    # While queue is not empty
    while queue:  #
        i = queue.popleft()  # Pops off queue
        bfs.append(i)  # Adds to bfs path
        for m in graph[i]:  # For each connected vertex
            if m not in traveled:  # If it has not been visited
                queue.append(m)  # Add to queue
                traveled.append(m)  # Add to traveled
    print("BFS: ")
    print(bfs)


def DFS(graph):
    # Traveled is a list that stores already visited nodes
    traveled = []
    # Stack
    stack = Stack()
    # Starts at vertex 1 - push to stack
    stack.push(1)
    traveled.append(1)
    # Actual Path
    dfs = []
    # While Stack not empty
    while not stack.isEmpty():  
        i = stack.pop()  # pops off top of stack
        dfs.append(i)  # Adds to path
        for m in graph[i]:  # For each connected vertex
            if m not in traveled:  # If it has not been visited
                stack.push(m)  # Push to stack
                traveled.append(m)  # add to traveled
    print("DFS: ")
    print(dfs)


def main():

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
