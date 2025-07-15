"""Helper functions for the football board simulation."""

from __future__ import annotations

import math

r = 3
"""Radius of the board."""

a = 0.1
"""Offset factor used by the board profile."""


def f(xs: float) -> float:
    """Profile of the football board used by :func:`gradf`."""
    if xs >= a * r:
        return math.sqrt(r**2 - ((xs - a * r) ** 2))
    elif -a * r < xs < a * r:
        return r
    else:
        return math.sqrt(r**2 - ((xs + a * r) ** 2))


def gradf(x: float, y: float) -> tuple[float, float]:
    """Return the outward normal of the board at ``(x, y)`` as a unit vector."""
    if x >= a * r:
        gradient = (2 * (x - a * r), 2 * y)
    elif -a * r < x < a * r and f(x) >= 0:
        gradient = (0, 1)
    elif -a * r < x < a * r and f(x) < 0:
        gradient = (0, -1)
    else:
        gradient = (2 * (x + a * r), 2 * y)
    norm = math.sqrt(gradient[0] ** 2 + gradient[1] ** 2)
    return (gradient[0] / norm, gradient[1] / norm)


def vout(vx: float, vy: float, x: float, y: float) -> tuple[float, float]:
    """Return velocity after reflection at ``(x, y)``."""
    gx, gy = gradf(x, y)
    dot = vx * gx + vy * gy
    voi = (dot * gx, dot * gy)
    vpi = (vx - voi[0], vy - voi[1])
    vof = (-voi[0], -voi[1])
    vpf = vpi
    vf = (vof[0] + vpf[0], vof[1] + vpf[1])
    return vf


if __name__ == "__main__":
    # The original simulation relied on ``numpy`` and ``matplotlib``. That code
    # has been removed to keep the module lightweight and importable without
    # external dependencies.
    pass
