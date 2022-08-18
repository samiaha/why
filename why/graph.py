# HOMEWORK: graph traversal algorithms!
# path_exists(a, b) returns TRUE if you can get to b from a along edges

import copy

def unfold_edges(fold):
    edges = []
    for source in fold:
        targets = fold[source]
        for target in targets:
            edge = (source, target)
            edges.append(edge)
    return edges

def fold_edges(edges):
    fold = {}
    for edge in edges:
        #source = edge[0]
        #target = edge[1]
        #the 2 lines above are equivalent to the line below. 
        source, target = edge
        if source not in fold:
            fold[source] = []
        fold[source].append(target)
        
    return fold

# we are gonna create a graph class
class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        # self is a container. a dict is a container. you can add arbitrary attributes into self like you
        # can add keys in a dict
        self.fold = fold_edges(self.edges)
        self.values = {
            node: None
            for node in nodes}

    def get_value(self, key):
        return self.values[key]

    def set_value(self, key, value):
        self.values[key] = value
        
    def find_paths(self, start, end, visited=None):
        visited = visited or {}
        visited[start] = True
        if start == end:
            return [(start,)]
        targets = self.fold.get(start, [])
        paths = []
        for target in targets:
            if target == end:
                paths.append((start, end))
            elif target not in visited:
                target_visited = copy.deepcopy(visited)
                target_paths = self.find_paths(
                    target,
                    end,
                    target_visited)
                if not len(target_paths) == 0:
                    paths.extend([
                        (start,) + path
                        for path in target_paths])
        return paths
        
        

def test_graph():
    nodes = ['M41', 'milky way', 'andromeda', 'spork', 'dirt', 'flap', 'stillness']
    edges = [
        ('M41', 'milky way'),
        ('M41', 'andromeda'),
        ('andromeda', 'M41'),
        ('spork', 'milky way'),
        ('milky way', 'andromeda'),
        ('stillness', 'dirt'),
        ('stillness', 'flap'),
        ('flap', 'M41'),
        ('flap', 'spork'),
        ('spork', 'stillness')]
        
    graph = Graph(nodes, edges)

    unfold = unfold_edges(graph.fold)
    print(graph.edges)
    print(graph.fold)
    print(unfold)

    graph.set_value('M41', 1000)
    graph.set_value('milky way', 3489347)
    graph.set_value('stillness', 8)
    graph.set_value('andromeda', 13131313)
    graph.set_value('spork', 71)
    graph.set_value('dirt', 19)
    graph.set_value('flap', 99999)

    print(graph.values)
    print(graph.get_value('andromeda'))
    print(graph.find_paths('stillness', 'andromeda'))

if __name__ == '__main__':
    test_graph()
