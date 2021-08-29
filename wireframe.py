class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class Wireframe:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))
    
    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))

    def outputNodes(self):
        print("-----Nodes-----")
        for i, node in enumerate(self.nodes):
            print(f"{i} ({float(node.x)},{float(node.y)}, {float(node.z)})")
    
    def outputEdges(self):
        print("\n-----Edges-----")
        for i, edge in enumerate(self.edges):
            print(f"{i} ({float(edge.start.x)}, {float(edge.start.y)}, {float(edge.start.z)})")
            print(f"to ({float(edge.stop.x)}, {float(edge.stop.y)}, {float(edge.stop.z)})")

    def translate(self, axis, d):
        if axis in ['x', 'y', 'z']:
            for node in self.nodes:
                setattr(node, axis, getattr(node, axis) + d)
    
    def scale(self, center, scale):
        """ Scale the wireframe from the centre of the screen """
        center_x, center_y = center
        for node in self.nodes:
            node.x = center_x + scale * (node.x - center_x)
            node.y = center_y + scale * (node.y - center_y)
            node.z *= scale
# my_wireframe = Wireframe()
# my_wireframe.addNodes([(0,0,0), (1,2,3), (3,2,1)])
# my_wireframe.addNodes([(1,2)])

if __name__ == "__main__":
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0, 8, 2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    cube.outputNodes()
    cube.outputEdges()