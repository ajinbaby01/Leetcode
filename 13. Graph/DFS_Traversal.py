res = []

def printGraph(matrix):
    for i in range(len(matrix)):
      print()
      for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

def dfs(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def traverse(i, j):
        if (
           (i, j) in visited or
           i not in range(rows) or
           j not in range(cols)
        ):
           return

        visited.add((i, j))
        res.append(matrix[i][j])

        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            traverse(next_i, next_j)

    for i in range(rows):
       for j in range(cols):
          traverse(i, j)

matrix = [["1","2","3","4","5"],["6","7","8","9","10"],["11","12","13","14","15"],["16","17","18","19","20"]]
dfs(matrix)
print(res)
