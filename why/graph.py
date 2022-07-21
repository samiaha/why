# HOMEWORK: unfold edges. Generate a list of tuples from the folded edges dictionary
# HOMEWORK: create a github account and remember your password somehow 
# do git stuff at beginning of next class

def fold_edges(edges):
    fold = {}
    for edge in edges:
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

    print(graph.fold)


if __name__ == '__main__':
    test_graph()
