from maze_solver import maze_solver
def test_multiple_paths():
    maze = [
        list("###E###"),
        list("#S...E#"),
        list("#######")
    ]
    maze_solver(maze)

test_multiple_paths()