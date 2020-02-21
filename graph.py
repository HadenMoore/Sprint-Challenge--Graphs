class Graph:
    def __init__(self):
        self.rooms = {}
    
    def add_room(self, room_id, exits):
        self.rooms[room_id] = {}
        for direction in exits:
            self.rooms[room_id][direction] = '?'

    def reverse(self, direction):
        if direction == 'n':
            return 's'
        if direction == 's':
            return 'n'
        if direction == 'e':
            return 'w'
        if direction == 'w':
            return 'e'
        else:
            print('not a valid direction')

    def add_connection(self, prev_room, cur_room, direction):
        self.rooms[prev_room][direction] = cur_room
        self.rooms[cur_room][self.reverse(direction)] = prev_room
        # print(self.rooms)

    def check_for_unexplored(self, room_id):
        unexplored = []
        for door in self.rooms[room_id]:
            if self.rooms[room_id][door] == '?':
                unexplored.append(door)

        if len(unexplored) > 0:
            return unexplored
        else:
            return None


    def bfs_paths(self, room_id):
        
        q = Queue()
        exits = []
        for direction in self.rooms[room_id]:
            if direction == '?':
                exits.append(direction)
        direction = exits[0]
        q.enqueue([direction])
        visited = {}

        while q.size() > 0:
            path = q.dequeue()
            room = path[-1]

            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(friend)
                    if friend not in visited:
                        q.enqueue(new_path)

        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    stack.push(next_vert)

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = list()
        queue.append([starting_vertex])
        visited = set()
        path = []
        while len(queue) > 0:
            node_list = queue.pop(0)
            vertex = node_list[-1]
            if vertex not in visited:
                for key in self.rooms[vertex]:
                    if self.rooms[vertex][key] == '?':
                        print(f'bfs: {path}')
                        return path
                for next_vert in self.rooms[vertex]:
                    if self.rooms[vertex][next_vert] not in visited:
                        new_node_list = list(node_list)
                        path.append(next_vert)
                        new_node_list.append(self.rooms[vertex][next_vert])
                        queue.append(new_node_list)
                visited.add(vertex)
                print(f'vertex: {vertex}, next vert: {next_vert}, visited: {visited}')