from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = Graph()

unexplored = []
unexplored.append(player.current_room)
visited = set()
path = []
while len(unexplored) > 0:
    room = unexplored[-1] 
    if room.id not in visited:
        graph.add_room(room.id, room.get_exits())
    
    visited.add(room.id)

    # Move to Unexplored Room
    direction = graph.check_for_unexplored(room.id)
    if direction is not None and room is player.current_room: 
        player.travel(direction[0])
        traversal_path.append(direction[0])
        # Add to Path, Add Connections
        path.append(direction[0])

        if player.current_room.id not in visited:
            graph.add_room(player.current_room.id, player.current_room.get_exits())
            visited.add(player.current_room.id)
        graph.add_connection(room.id, player.current_room.id, direction[0])
        
    else:
        # Reverse Path Until Direction is Not None
        while graph.check_for_unexplored(player.current_room.id) is None:
          
            if len(path) > 0:
                backtrack = graph.reverse(path.pop())
                player.travel(backtrack)
                traversal_path.append(backtrack)
            else:
                break
    
    if graph.check_for_unexplored(room.id) is None:
        unexplored.pop()

    if graph.check_for_unexplored(player.current_room.id) is not None: 
        if player.current_room not in unexplored:
            unexplored.append(player.current_room)

num_moves = len(traversal_path)  
print(num_moves)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
