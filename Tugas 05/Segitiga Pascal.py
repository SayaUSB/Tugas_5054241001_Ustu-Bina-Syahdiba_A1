if __name__ == "__main__":
    n = int(input())
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    triangle = triangle[::-1]
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle[0])))