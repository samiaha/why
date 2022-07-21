# here we are making a class
class Diagram():
    def __init__(self, nodes, arrows):
        # currently nodes and arrows are just arguments to __init__
        # self.nodes creates nodes as an attribute of self
        self.nodes = nodes 
        self.arrows = arrows

    def propagate(self, state):
        # we want to assign a value to each node given a state
        result = {key: None for key in self.nodes}
        # END OF LESSON START HERE!!!!!!!! figure out how to propagate state thru network and get new state woooo
        
# __name__ is a special variable that python adds to your file
# when you call python in the terminal, this if __name__ thing below - whatever is under it happens
# the class Diagram can now now be imported in other files.
# when Diagram is imported, the whole file is actually imported. 
# the if-name-main thing only happens when this file is called directly from the command line 
# this if-name-main thing prevents the code beneath it from being executed in the file that imported Diagram
        
def test_diagram():
    nodes = ['whale', 'tree', 'fire']
    # keys will be where the arrow is from and values will be where the arrow is going to
    arrows = { 
        'whale': ['tree'],
        'tree': ['fire'],
    }
    
    # ctrl n ctrl a ctrl o tab makes a new line tabbed 
    # this is how we create a new instance of the Diagram class
    diagram = Diagram(nodes, arrows) 
    print(diagram.nodes)
    print(diagram.arrows)
    print("why")
    

if __name__ == '__main__':
    test_diagram()
