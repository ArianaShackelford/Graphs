"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        # add starting node to stack
        s = Stack()
        s.push(starting_vertex)

        visited = set()
        # while stack isn't empty:
        while s.size() > 0:
            # pop the first vert
            v = s.pop()
            # if that vert isn't visited:
            if v not in visited:
                #print v
                print(v)
                # mark as visited
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                #push all it's unvisited neighbors to the stack
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # add a visited parameter to the funtion that can be passed in via recursion
        #if visited is none
        if visited is None:
            #set visited
            visited = set()
        #add the starting_vertex to visited
        visited.add(starting_vertex)
        # print the starting_vertex
        print(starting_vertex)
        #get the connected nodes from the starting vertex
        connected = self.get_neighbors(starting_vertex)
        #while connected is greater than 0
        while len(connected) > 0:
            #for each connection
            for connection in connected:
                # if that connection has not been visited
                if connection not in visited:
                    # recursively run through the function again passing in the connection as the starting_vertex, and the visited list
                    self.dfs_recursive(connection, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

        #create a Queue to hold the path
        path = Queue()
        #add starting_vertex to the queue
        path.enqueue(starting_vertex)
        #set visited
        visited = set()
        #while the path is not empty
        while path.size() > 0:
            # remove the first vert from the path and set as current path
            current_path = path.dequeue()
            # grab the last vert in the queue (path)
            last_in_path = current_path[-1]
            #if that vert is not in visited
            if last_in_path not in visited:
                #check to see if it is the destination_vertex
                if last_in_path == destination_vertex:
                    #it is so return the current path
                    return current_path
                #else mark it as visited
                else:
                    visited.add(last_in_path)
                    #get the connected verts
                    connected = self.get_neighbors(last_in_path)
                    #make new versions of the current path and add the connected verts to them
                    #for each connection in connected
                    for connection in connected:
                        #duplicate the path
                        path_copy = current_path[:]
                        #add the connection
                        path_copy.append(connection)
                        #and add the path to the queue
                        path.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        #create a new stack called path
        path = Stack()
        #add starting vertex into path
        path.push(starting_vertex)
        #set visited
        visited = set()
        #while the path is not empty
        while path.size() > 0:
            #set the current path by removing it from the list
            current_path = path.pop()
            #grab the last vertex in the current path
            last_in_path = current_path[-1]
            #if that hasn't been visited
            if last_in_path not in visited:
                #check to see if it's the destination
                if last_in_path == destination_vertex:
                #and return the path
                    return current_path
            #if not mark it as visited
            else:
            #add to visited
                visited.add(last_in_path)
            #get the connected vertices
                connected = self.get_neighbors(last_in_path)
            #for each connection
                for connection in connected:
                #make a copy
                    path_copy = current_path[:]
                #add the connection
                    path_copy.append(connection)
                #add the copy to path
                    path.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #create a new stack called path
        path = Stack()
        #add starting vertex into path
        path.push(starting_vertex)
        #set visited
        visited = set()
        #set the current path by removing it from the list
        current_path = path.pop()
        #grab the last vertex in the current path
        last_in_path = current_path[-1]

        if current_path == None:
            #make current path starting_vertex
            current_path = [starting_vertex]
            #if that hasn't been visited
        if last_in_path not in visited:
            #add it to visited
            visited.add(last_in_path)
            #get the connected vertices
            connected = self.get_neighbors(last_in_path)
            #for each connection
            for connection in connected:
                #check to see if it's the destination
                if last_in_path == destination_vertex:
                    #add the connection
                    current_path.append(connection)
                #and return the path
                    return current_path
                 #make a copy
                path_copy = current_path[:]
                #add the connection
                path_copy.append(connection)
                #add the copy to path
                path.push(path_copy)

            #run through function until destination is found
            return self.dfs_recursive(starting_vertex, destination_vertex, visited)
        
        
           
           
            

            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
