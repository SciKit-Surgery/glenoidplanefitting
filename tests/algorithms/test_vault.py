"""
Unit tests for the Friedman module
"""
import math
import glenoidplanefitting.algorithms.vault as vlt


def test_creat_vault_line():
    """
    Tests that the create_friedman_line returns the midpoint
    """
    anterior_margin = [3.0, 5.0, 9.0]
    posterior_margin = [11.0, 13.0, 17.0]

    vault_point = vlt.create_vault_line(anterior_margin, posterior_margin)

    assert vault_point[0] == 7.0
    assert vault_point[1] == 9.0
    assert vault_point[2] == anterior_margin[2] #is this right, issue #15.


def test_vault_version():
    """
    Tests that vault_version correctly returns the version
    This is a slightly dodgy regression test, I haven't actually
    though about the numbers here.
    """
    anterior_margin = [3.0, 5.0, 9.0]
    vault_point0 = [11.0, 13.0, 17.0]
    vault_point1 = [19.0, 23.0, 29.0]

    version = vlt.vault_version(anterior_margin,
            vault_point1, vault_point0 )

    assert math.isclose(version, -85.90928830690325,
            rel_tol = 1e-09, abs_tol = 0.0)
