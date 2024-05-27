class Topology:
    def __init__(self):
        self.topology = {}

    def addLine(self, u, v):
        self._addLineHelper(u, v)
        self._addLineHelper(v, u)  # Undirected topology, so add both directions

    def _addLineHelper(self, u, v):
        if u not in self.topology:
            self.topology[u] = []
        if v not in self.topology[u]:
            self.topology[u].append(v)

    def openLineOdd(self, u, v):
        if u in self.topology and v in self.topology[u]:
            self.topology[u].remove(v)
            self.topology[v].remove(u)
        if not self._searchTopology(v, 0):
            self._removeBus(v)
        if not self._searchTopology(u, 0):
            self._removeBus(u)
    
    def openLineEven(self, u, v):
        self.openLineOdd(u, v)
        self.addLine(u, v)
            

    def _removeBus(self, bus):
        if bus in self.topology:
            self._removeSubBuses(bus)
            

    def _removeSubBuses(self, root):
        visited = set()
        self._dfs(root, visited)
        for bus in visited:
            if bus in self.topology:
                del self.topology[bus]

    def _dfs(self, bus, visited):
        visited.add(bus)
        if bus in self.topology:
            for neighbor in self.topology[bus]:
                if neighbor not in visited:
                    self._dfs(neighbor, visited)

    def _searchTopology(self, start, target):
        visited = set()
        return self._dfsSearch(start, target, visited)

    def _dfsSearch(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        if current in self.topology:
            for neighbor in self.topology[current]:
                if neighbor not in visited:
                    if self._dfsSearch(neighbor, target, visited):
                        return True
        return False

    def printTopology(self):
        for bus in self.topology:
            print(bus, "->", " -> ".join(map(str, self.topology[bus])))

    def printTopology2(self):
        for bus in self.topology:
            print(f'bus: {bus} = {self.topology[bus]}')

# Example usage:
if __name__ == "__main__":
    topology = Topology()
    topology.addLine(1, 2)
    topology.addLine(1, 3)
    topology.addLine(2, 3)
    topology.addLine(3, 4)
    topology.addLine(4, 5)
    topology.addLine(5, 6)
    topology.addLine(6, 2)

    print("topology before removing line 1 -> 3:")
    topology.printTopology2()

    topology.openLine(1, 3)

    print("\ntopology after removing line 1 -> 3:")
    topology.printTopology2()

    topology.openLine(2, 3)

    print("\ntopology after removing line 2 -> 3:")
    topology.printTopology2()

    topology.openLine(6, 2)

    print("\ntopology after removing line 6 -> 2:")
    topology.printTopology2()









    
