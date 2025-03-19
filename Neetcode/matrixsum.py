from typing import List

def matrixSum(matrix: List[List[int]]) -> int:
    """
    """
    score = 0
    index = 0

    print(len(matrix))

    while index < len(matrix)-1:

        temp = []

        for row in matrix:

            x = max(row)
            temp.append(max(row))
            row.remove(x)

        score += max(temp)
        print(temp)
        index += 1

    return score





print(matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))



