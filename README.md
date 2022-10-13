# Project "translation to integral image representation"
**translation to integral representation** - это небольшой проект, который позволяет из матрицы изображения получить его интегральное матричное представление, а также рассчитать яркость определённого участка изображения.
## Реализация
Основная часть программы - это две функции `integral_image()` и `rect_sum()`. 
### Реализация функции `integral_image`:
```python
def integral_view(image: List[List]) -> List[List]:
    '''
    Функция получает матрицу изображения, возвращает интегральное представление изображения
    Args:
        image (List[List]): param

    Returns:
        integral_image (List[List]): интегральное отображение полученного изображения
    Raises:
        TypeError: если передадим не двумерный массив
    '''
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
```
### Реализация функции `rect_summ`:
```python
def rect_sum(image: List[List], x1: int, y1: int, x2: int, y2: int) -> int:
    '''
    Функция получает на вход матрицу, а также координаты (x1, y1) - верхнего левого угла прямоугольника и (x2, y2) -
    нижнего правого угла прямоугольника, возвращает сумму элементов внутри этого прямоугольника
    Args:
        image (List[List]): матрица
        x1 (int): координата верхнего левого угла
        y1 (int): координата верхнего левого угла
        x2 (int): координата нижнего правого угла
        y2 (int): координата нижнего правого угла

    Returns:
         sum (int): сумма элементов в прямоугольнике
    Raises:
        TypeError: передали некорректное значение (можно лишь: List[List] и int)
        IndexError: длина вложенных списков различна, а должна быть одинакова
    '''
    if x1 < 0 or x2 <0 or y1 < 0 or y2 < 0:
        sum = "Координаты должны быть введены как положительные числа"
    else:
        integral_image = integral_view(image)
        sum = integral_image[y1 -1 + 1][x1 -1 + 1] + integral_image[y2 + 1][x2 + 1] - integral_image[y1][x2 + 1]\
          - integral_image[y2 + 1][x1]
    return sum
```
## Применение
Интегральное изображение использутся для быстрого вычисления яркости заданных участков изображения ( в вейвлет-преобразованиях, фильтрах Хаара, рассчёте дескрипторов). Более подробно об этом можно почитать [здесь.](https://russianblogs.com/article/17821863559/)
