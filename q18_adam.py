
if __name__=="__main__":
    triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    tri_grid = triangle.split("\n")
    tri_grid_rows = []
    for row in tri_grid:
        tri_grid_rows.append(row.split(" "))
    tri_grid = tri_grid_rows
    tri_grid = [list(map(int, lst)) for lst in tri_grid]
    height = len(tri_grid)

    for cur_height in range(height - 1, 0, -1):
        row_len = cur_height
        row = tri_grid[cur_height]
        for i in range(row_len):
            max_val = max(row[i], row[i + 1])
            tri_grid[cur_height - 1][i] += max_val

    print(tri_grid[0][0])
