from integral_image_functions import integral_view, rect_sum
from typing import List
from random import randint


def create_matrix(n: int, m: int) -> List[List]:
    image = [[randint(0, 255) for j in range(m)] for i in range(n)]
    return image


def print_matrix(matrix: List[List]):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print("%4d" % matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    n = 3
    m = 3
    image = create_matrix(n, m)
    print("Исходная матрица")
    print("-" * 50)
    print_matrix(image)
    print("-" * 50)
    integral_image = integral_view(image)
    print("Интегральное представление изображения")
    print_matrix(integral_image)
    print("-" * 50)
    print("Сумма пикселей прямоугольника")
    print(rect_sum(image, -2, 0, -1, -3))