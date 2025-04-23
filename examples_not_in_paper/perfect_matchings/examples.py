class Examples:
    
    def __init__(self):
        self.examples = []
        
        example1 = {"attributes": ["x", "y", "z"], "relations": [["x", "y"], ["y", "z"], ["z", "x"]], "fds": []}
        example2 = {"attributes": ["A", "B", "C", "D", "E", "F", "G", "H"], "relations": [["A","B","C","D"], ["A","B","E","F"], ["C","D","E","F"], ["A","B","G","H"], ["C","D","G","H"]], "fds": []}
        example3 = {"attributes": ["x", "y", "z"], "relations": [["x", "y"], ["y", "z"]], "fds": []}
        example4 = {"attributes": ["x", "y", "z", "u"], "relations": [["x", "y"], ["y", "z"], ["z", "u"]], "fds": []}
        example5 = {"attributes": ["x", "y", "z", "u"], "relations": [["x", "y"], ["y", "z"], ["z", "u"], ["u", "x"]], "fds": []}
        example6 = {"attributes": ["A", "B", "C", "D", "E"], "relations": [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "fds": []}
        example7 = {"attributes": ["x", "y", "z", "u"], "relations": [["x", "y"], ["y", "z"], ["z", "u"]], "fds": [[["x", "z"], ["u"]], [["y", "u"], ["x"]]]}
        example8 = {"attributes": ["A", "B", "C", "D", "E", "F", "G", "H"], "relations": [["A","B","C","D"], ["A","B","E","F"], ["C","D","E","F"], ["A","B","G","H"], ["C","D","G","H"]], "fds": [[["E","F","G","H"], ["A","B","C","D"]], 
           [["A","B","C","E"], ["D","F","G","H"]], 
           [["B","C","D","G"], ["A","E","F","H"]]]}
        
        self.examples.append(example1)
        self.examples.append(example2)
        self.examples.append(example3)
        self.examples.append(example4)
        self.examples.append(example5)
        self.examples.append(example6)
        self.examples.append(example7)
        self.examples.append(example8)
        
    def get_example(self, index):
        return self.examples[index]