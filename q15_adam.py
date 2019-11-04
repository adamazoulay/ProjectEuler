if __name__=="__main__":
    n = 20

    # Number of vertices is just n + 1
    n += 1
    range_n = range(n)

    # Let's build a grid
    grid = []
    for y in range_n:
        grid.append([0] * n)

    # Initialize top left square with number of paths
    grid[0][0] = 1

    # Now loop through all rows in order and sum the paths
    for row in range_n:
        for col in range_n:
            if row > 0:
                grid[row][col] += grid[row - 1][col]

            # Also check above
            if col > 0:
                grid[row][col] += grid[row][col - 1]


    # Print at -1 since we made n+=1 at start
    print(grid[n - 1][n - 1])
