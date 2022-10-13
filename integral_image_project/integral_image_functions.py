from typing import List


def integral_view(image: List[List]) -> List[List]:
    n = len(image)
    m = len(image[0])
    integral_image = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            else:
                integral_image[i][j] = image[i-1][j-1] - integral_image[i-1][j-1] + integral_image[i-1][j]\
                                       + integral_image[i][j-1]
    return integral_image


def rect_sum(image: List[List], x1: int, y1: int, x2: int, y2: int) -> int:
    if x1 < 0 or x2 <0 or y1 < 0 or y2 < 0:
        sum = "Координаты должны быть введены как положительные числа"
    else:
        integral_image = integral_view(image)
        sum = integral_image[y1 -1 + 1][x1 -1 + 1] + integral_image[y2 + 1][x2 + 1] - integral_image[y1][x2 + 1]\
          - integral_image[y2 + 1][x1]
    return sum
