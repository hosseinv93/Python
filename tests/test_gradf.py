import math
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from football_board import gradf

@pytest.mark.parametrize("x,y", [
    (0, 0),
    (1.0, 0.5),
    (-2.5, -1.0),
    (3.1, 2.0),
    (-3.1, -2.0),
])
def test_gradf_unit_length(x, y):
    gx, gy = gradf(x, y)
    norm = math.hypot(gx, gy)
    assert math.isclose(norm, 1.0, rel_tol=1e-9), f"gradf({x}, {y}) not unit"
