class Cmap:
    def __init__(self):
        self.caves = []
        self.connections = {"start": []}
        self.small = {}
        self.visited = {}
        self.start = "start"

    def connect(self, id1, id2):
        if id1 not in self.caves:
            self.caves.append(id1)
            self.small[id1] = id1.islower()
            self.visited[id1] = 0
            self.connections[id1] = []
        if id2 not in self.caves:
            self.caves.append(id2)
            self.small[id2] = id2.islower()
            self.visited[id2] = 0
            self.connections[id2] = []

        if id1 != "end" and id2 != "start":
            self.connections[id1].append(id2)
        if id2 != "end" and id1 != "start":
            self.connections[id2].append(id1)

    def reset(self):
        for id in self.caves:
            self.caves[id].visited = False

def traverse(connections, small, visited, cave, path=[], double_visit=False):
    lpath = path.copy()
    lpath.append(cave)
    lvisited = visited.copy()
    lvisited[cave] += 1
    if small[cave] and lvisited[cave] == 2:
        double_visit = True
    if cave == "end":
        return [lpath]
    else:
        paths = []
        for dest in connections[cave]:
            can_visit = True
            if double_visit:
                can_visit = not (small[dest] and visited[dest] > 0)
            else:
                can_visit = not (small[dest] and visited[dest] > 1)
            if can_visit:
                paths.extend(traverse(connections, small, lvisited, dest, lpath, double_visit))
        return paths

cave_map = Cmap()

with open("day12.in", "r") as f:
    for line in f:
        cave_map.connect(*line.strip().split("-"))

#print(cave_map.connections)

paths = list(traverse(cave_map.connections, cave_map.small, cave_map.visited, cave_map.start, double_visit=True))
print(len(paths))

paths = list(traverse(cave_map.connections, cave_map.small, cave_map.visited, cave_map.start))
# for path in paths:
#     print(path)
print(len(paths))
