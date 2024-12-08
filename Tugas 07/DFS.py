def flood_fill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == color:
        return image
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image

