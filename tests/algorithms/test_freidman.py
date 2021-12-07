"""
Unit tests for the Friedman module
"""
import math
import pytest
import glenoidplanefitting.algorithms.friedman as frd


def test_creat_friedman_line():
    """
    Tests that the create_friedman_line returns the midpoint
    """
    anterior_margin = [3.0, 5.0, 9.0]
    posterior_margin = [11.0, 13.0, 17.0]

    with pytest.raises(ValueError):
        friedman_point = frd.create_friedman_line(anterior_margin,
                                                  posterior_margin)

    posterior_margin = [11.0, 13.0, 9.0]
    friedman_point = frd.create_friedman_line(anterior_margin, posterior_margin)
    assert friedman_point[0] == 7.0
    assert friedman_point[1] == 9.0
    assert friedman_point[2] == anterior_margin[2]


def test_friedman_version():
    """
    Tests that friedman_version correctly returns the version
    This is a slightly dodgy regression test, I haven't actually
    though about the numbers here.
    """
    anterior_margin = [3.0, 5.0, 9.0]
    friedman_point0 = [11.0, 13.0, 17.0]
    friedman_point1 = [19.0, 23.0, 29.0]

    version = frd.friedman_version(anterior_margin,
            friedman_point1, friedman_point0 )

    assert math.isclose(version, -85.90928830690325,
            rel_tol = 1e-09, abs_tol = 0.0)
