# HOMEWORK: graph traversal algorithms!
# path_exists(a, b) returns TRUE if you can get to b from a along edges
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
    

if __name__ == '__main__':
    test_graph()
