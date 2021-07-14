graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')



    # def solve_matrix(self, starting_node):
    #     print(f"\nENTERING SOLVE MATRIX {starting_node.start_coords}\n----------------------")
    #     print(f"POTENTIAL MOVES: {starting_node.potential_moves}")
    #     print(f"STARTING NODE LINEAGE: {starting_node.get_lineage()}")
    #     print(f"GENERATION COUNT for {starting_node}:", starting_node.generation_count())

    #     # breakpoint()
    #     for neighbor in starting_node.potential_moves:
    #         neighbor_node = Node(neighbor, self)
    #         if starting_node.generation_count() < 8:
    #             starting_node.adopt_node(neighbor_node)
    #             self.solve_matrix(neighbor_node)
    #         else:
    #             self.solve_matrix(starting_node)
    #             print("One Combination")