path = []

def search_path(row, col, mall_layout, visited, max_rows, max_cols, path, remaining_items):
    if not (0 <= row < max_rows and 0 <= col < max_cols):
        return False
    if mall_layout[row][col] == '1' or visited[row][col]:
        return False
    
    visited[row][col] = True
    path.append((row, col))

    if mall_layout[row][col] == '2':
        remaining_items -= 1

    if row == max_rows - 1 and col == max_cols - 1 and remaining_items == 0:
        return True

    if (search_path(row + 1, col, mall_layout, visited, max_rows, max_cols, path, remaining_items) or
        search_path(row, col + 1, mall_layout, visited, max_rows, max_cols, path, remaining_items) or
        search_path(row, col - 1, mall_layout, visited, max_rows, max_cols, path, remaining_items) or
        search_path(row - 1, col, mall_layout, visited, max_rows, max_cols, path, remaining_items)):
        return True

    visited[row][col] = False
    path.pop()
    if mall_layout[row][col] == '2':
        remaining_items += 1
    return False

cols, rows = map(int, input().split())
mall_layout = [list(input().strip()) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
item = 0
for r in range(rows):
    for c in range(cols):
        if mall_layout[r][c] == '2':
            item += 1
path_found = search_path(0, 0, mall_layout, visited, rows, cols, path, item)

if path_found:
    output_layout = [row[:] for row in mall_layout]
    for r, c in path:
        if output_layout[r][c] != '1':
            output_layout[r][c] = '*'
    
    for row in output_layout:
        print(''.join(row))
