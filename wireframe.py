import math

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

    def findCenter(self):
        num_nodes = len(self.nodes)
        meanX = sum([node.x for node in self.nodes]) / num_nodes
        meanY = sum([node.y for node in self.nodes])/ num_nodes
        meanZ = sum([node.z for node in self.nodes])/ num_nodes

        return(meanX, meanY, meanZ)
    
    def rotateX(self, c, radians):
        cx, cy, cz = c
        for node in self.nodes:
            y      = node.y - cy
            z      = node.z - cz
            d      = math.hypot(y, z)
            theta  = math.atan2(y, z) + radians
            node.z = cz + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)
            
    def rotateY(self, c, radians):
        cx, cy, cz = c
        for node in self.nodes:
            x      = node.x - cx
            z      = node.z - cz
            d      = math.hypot(x, z)
            theta  = math.atan2(x, z) + radians
            node.z = cz + d * math.cos(theta)
            node.x = cx + d * math.sin(theta)

    def rotateZ(self, c, radians):    
        cx, cy, cz = c    
        for node in self.nodes:
            x      = node.x - cx
            y      = node.y - cy
            d      = math.hypot(y, x)
            theta  = math.atan2(y, x) + radians
            node.x = cx + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

if __name__ == "__main__":
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0, 8, 2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    cube.outputNodes()
    cube.outputEdges()