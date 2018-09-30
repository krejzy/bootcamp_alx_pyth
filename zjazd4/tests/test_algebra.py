import sys

import numpy as np




from mathematica.algebr import matrics


def test_add_matrics():
    a = [
        [1,2,3],
        [4,5,6]
    ]
    b = [
        [7,8,9]
        [10,11,12]
    ]
    result = matrices.add_matrices(a, b)
    expected = [
        [8, 10, 12]
        [14, 16, 18]
    ]
    assert result == expected





