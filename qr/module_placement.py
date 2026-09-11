def set_finder_pattern(matrix, reserved, x, y):
    for dy in range(-3,4,1):
        for dx in range(-3,4,1):
            if (dx == -3 or dx == 3) or (dy == -3 or dy == 3):
                matrix[y+dy][x+dx] = 1
            elif (dx == -2 or dx == 2) or (dy == -2 or dy == 2):
                matrix[y+dy][x+dx] = 0
            else:
                matrix[y+dy][x+dx] = 1
            reserved[y+dy][x+dx] = True
    

def set_finder_patterns(matrix, reserved, version):
    x1 = 3
    y1 = 3

    x2 = ((((version-1)*4)+21) - 7) + 3
    y2 = 3

    x3 = 3
    y3 = ((((version-1)*4)+21) - 7) + 3

    set_finder_pattern(matrix,reserved,x1,y1)
    set_finder_pattern(matrix,reserved,x2,y2)
    set_finder_pattern(matrix,reserved,x3,y3)


