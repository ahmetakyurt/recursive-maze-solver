from maze_solver import maze_solver

def test_simple_maze():
    maze = [
        list("#####"),
        list("#S.E#"),
        list("#####")
    ]
    maze_solver(maze)

test_simple_maze()