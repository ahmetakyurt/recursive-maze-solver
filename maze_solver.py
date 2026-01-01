def maze_solver(maze, location=(), currentPath=[], visited = set()):
        
    r, c = len(maze), len(maze[0])

    

    if not location:
        for i in range(r):
            for j in range(c):
                if maze[i][j] == "S":
                    return maze_solver(maze, (i, j), [(i, j)])
        
    else:
        if location in visited:
            return False
        
        rl, cl = location[0], location[1]
        
        visited.add(location)
        if maze[rl][cl] == "#":
        
            return False
            
        currentPath.append(location) 
        if maze[rl][cl] == "E":
            print("Absolute movement: ", currentPath)
            return True
        
        if rl >0:
            if maze_solver(maze, (rl-1, cl), currentPath, visited):
                return True
        if cl >0:
            if maze_solver(maze, (rl, cl-1), currentPath, visited):
                return True
        if rl <r-1:
            if maze_solver(maze, (rl+1, cl), currentPath, visited):
                return True
        if cl <c-1:
            if maze_solver(maze, (rl, cl+1), currentPath, visited):
                return True
            
        currentPath.pop()
            
def main():
    with open("sample_maze.txt", "r") as file:
        maze = [list(line.strip()) for line in file]
    
    maze_solver(maze)

if __name__ == "__main__":
    main()