import pytest
from integral_image_project.integral_image_functions import rect_sum


@pytest.mark.parametrize("image, x1, y1, x2, y2, sum", [([[31, 180, 248], [93, 240, 7], [82, 222, 192]], 0, 0, 1, 1,
                                                        544), ([[8, 211, 27, 199], [197, 30, 206, 120], [103, 235, 150,
                                                         90], [21, 25, 152, 192]], 0, 0, 1, 1, 446), ([[179, 73, 23],
                                                        [227, 244, 3], [76, 19, 156]], -2, 0, -1, -3,
                                                        "Координаты должны быть введены как положительные числа")])
def test_rect_sum_good(image, x1, y1, x2, y2, sum):
    assert rect_sum(image, x1, y1, x2, y2) == sum


@pytest.mark.parametrize("image, x1, y1, x2, y2, expected_exception", [([[248, 84, 160], [161, 163, 199], [243, 87, 50]]
                                                                        , 0, 0, 1, "a", TypeError), ([1, 2, 3], 0, 0, 1,
                                                                        1, TypeError), ([[1, 2, 3], 4, 5, 6], 0, 0, 1,
                                                                        1, TypeError), ([[1, 2, 3], [[1]]], 0, 0, 1, 1,
                                                                        TypeError), ([[1, 2, 2], [1]], 0, 0, 1, 1,
                                                                        IndexError), ([[248, 84, 160], [161, 163, 199],
                                                                        [243, 87, 50]], 0, 0, 1, 0.4, TypeError)])
def test_rect_sum_with_error(image, x1, y1, x2, y2, expected_exception):
    with pytest.raises(expected_exception):
        rect_sum(image, x1, y1, x2, y2)
