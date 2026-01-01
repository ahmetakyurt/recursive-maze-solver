from maze_solver import maze_solver
def test_no_exit():
    maze = [
        list("#####"),
        list("#S###"),
        list("#####")
    ]
    maze_solver(maze)
    
test_no_exit()