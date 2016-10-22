#Given the maze:

maze = [[0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [3, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0]]

#3: the goal cell
#1: the wall cell
#0: the current (empty) cell
#2: the visited cell

def investigate(x, y):
    if maze[x][y] == 3:
        print ('%d,%d is the exit' % (x, y))
        return True
    elif maze[x][y] == 1:
        print ('%d,%d is a wall' % (x, y))
        return False
    elif maze[x][y] == 2:
        print ('%d,%d has been passed again' % (x, y))
        return False

    print ('%d,%d is investigated' % (x, y))
	

    # mark as visited
    maze[x][y] = 2

    # investigate surrounding blocks starting with the bottom one and
    # continue anti-clockwise 
    if ((x < len(maze)-1 and investigate(x+1, y))
        or (y > 0 and investigate(x, y-1))
        or (x > 0 and investigate(x-1, y))
        or (y < len(maze)-1 and investigate(x, y+1))):
        return True

    return False

investigate(1,3)
