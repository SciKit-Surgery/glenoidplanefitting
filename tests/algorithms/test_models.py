"""
Unit tests for the Friedman module
"""
import math
import numpy as np
import vtk
import glenoidplanefitting.algorithms.models as mdl

def test_make_plane_model():
    """
    Tests that make_plane_model returns a plane centred on the
    plane centre with the correct normal vector
    """
    plane_centre = [1.0, 3.0, 5.0]
    plane_normal = [7.0, 11.0, 13.0]
    plane_size = 200.0
    plane_resolution = 20

    plane = mdl.make_plane_model(plane_centre, plane_normal,
            plane_resolution, plane_size)

    assert isinstance (plane, vtk.vtkPlaneSource)#pylint:disable=no-member

    assert np.array_equal(np.array(plane.GetCenter()),
                          np.array(plane_centre))

    denormalised_normal = np.linalg.norm(np.array(plane_normal)) \
                                         * np.array(plane.GetNormal())

    assert np.allclose(denormalised_normal, np.array(plane_normal))

    assert plane.GetXResolution() == plane_resolution
    assert plane.GetYResolution() == plane_resolution

    actual_plane_size = np.linalg.norm(np.array(plane.GetPoint1()) -
                                       np.array(plane.GetPoint2()))
    expected_plane_size = math.sqrt(2 * (plane_size * plane_size))
    assert math.isclose(actual_plane_size, expected_plane_size)


def test_friedman_model():
    """
    Tests that make Friedman model returns the appropriate line
    """
    point1 = (2.0, 3.0, 5.0)
    point2 = (7.0, 11.0, 13.0)

    line = mdl.make_friedman_model(point1, point2)

    assert isinstance(line, vtk.vtkLineSource)#pylint:disable=no-member
    assert line.GetPoint1() == point1
    assert line.GetPoint2() == point2


def test_vault_model():
    """
    Tests that make vault model returns the appropriate line
    """
    point1 = (1.0, 1.0, 2.0)
    point2 = (3.0, 5.0, 8.0)

    line = mdl.make_vault_model(point1, point2)

    assert isinstance(line, vtk.vtkLineSource)#pylint:disable=no-member
    assert line.GetPoint1() == point1
    assert line.GetPoint2() == point2
