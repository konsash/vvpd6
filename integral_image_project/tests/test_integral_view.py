import pytest
from integral_image_project.integral_image_functions import integral_view


@pytest.mark.parametrize("image, expected_result", [([[106, 62], [72, 220]], [[0, 0, 0], [0, 106, 168], [0, 178, 460]]),
                                                    ([[74, 22, 223], [248, 38, 58], [137, 52, 46]], [[0, 0, 0, 0],
                                                    [0, 74, 96, 319], [0, 322, 382, 663], [0, 459, 571, 898]]
                                                    )])
def test_integral_view_good(image, expected_result):
    assert integral_view(image) == expected_result


@pytest.mark.parametrize("image, expected_exception", [("a", TypeError), (4, TypeError), ({1, 2, 3, 4, 5}, TypeError),
                                                       ([1, [1, 2, 3]], TypeError), ([[1, 2], [[5]]], TypeError),
                                                       ([[1, 2, 3], [1]], IndexError), ([1, 2], TypeError), ([[1, 2],
                                                        ["a", "b"]], TypeError), ([{1, 2}, 1], TypeError)])
def test_integral_view_with_error(image, expected_exception):
    with pytest.raises(expected_exception):
        integral_view(image)
