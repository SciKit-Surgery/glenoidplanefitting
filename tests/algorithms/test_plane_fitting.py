"""
Unit tests for the fit plane module
"""
import numpy as np
from vtk import vtkPolyData #pylint:disable=no-name-in-module
import glenoidplanefitting.algorithms.plane_fitting as plnf


def test_fit_plane_to_scapula():
    """
    Tests for fitting a plane to scapula points
    """
    inferior_scapula = np.array([-50.0, -50.0, 0.0], ndmin =2)
    medial_scapula = np.array([-50.0, 50.0, 0.0], ndmin = 2)
    glenoid_fossa = np.array([-50.0, 0.0, 0.0], ndmin = 2)

    scapula_points = np.concatenate((inferior_scapula,
                                      medial_scapula,
                                      glenoid_fossa), axis = 0)

    plane = plnf.fit_plane_to_points_scapula(scapula_points)

    assert not isinstance(plane, tuple)
    assert isinstance(plane, vtkPolyData)

    plane = plnf.fit_plane_to_points_scapula(scapula_points,
            return_meta1 = True)

    assert isinstance(plane, tuple)
    assert isinstance(plane[0], vtkPolyData)
    assert np.array_equal(plane[1], np.array([-50.0, 0.0, 0.0]))
    assert np.allclose(plane[2], np.array([1.0, 0.0, 0.0]))


def test_fit_plane_to_glenoid():
    """
    Tests for fitting a plane to the glenoid face
    """
    superior_glenoid = np.array([-50.0, -50.0, 0.0], ndmin =2)
    inferior_glenoid_right = np.array([-50.0, 50.0, 0.0], ndmin = 2)
    inferior_glenoid_left = np.array([50.0, 50.0, 0.0], ndmin = 2)

    glenoid_points = np.concatenate((superior_glenoid,
                                     inferior_glenoid_right,
                                     inferior_glenoid_left), axis = 0)

    plane = plnf.fit_plane_to_points_glenoid(glenoid_points)

    assert not isinstance(plane, tuple)
    assert isinstance(plane, vtkPolyData)

    plane = plnf.fit_plane_to_points_glenoid(glenoid_points,
            return_meta2 = True)

    assert isinstance(plane, tuple)
    assert isinstance(plane[0], vtkPolyData)
    assert np.allclose(plane[1], np.array([-16.66666667, 16.66666667, 0.]))
    assert np.allclose(plane[2], np.array([0.0, 0.0, -1.0]))


def test_fit_plane_transverse():
    """
    Tests for transverse plane fitting
    """
    inferior_scapula = np.array([-50.0, -50.0, 0.0], ndmin =2)
    medial_scapula = np.array([-50.0, 50.0, 0.0], ndmin = 2)
    glenoid_fossa = np.array([-50.0, 0.0, 0.0], ndmin = 2)

    scapula_points = np.concatenate((inferior_scapula,
                                      medial_scapula,
                                      glenoid_fossa), axis = 0)


    medial_scapula1 = np.array([-40.0, 40.0, 0.0], ndmin = 2)
    glenoid_fossa1 = np.array([-40.0, 0.0, 0.0], ndmin = 2)

    glenoid_points = np.concatenate((inferior_scapula,
                                      medial_scapula1,
                                      glenoid_fossa1), axis = 0)

    plane = plnf.fit_plane_transverse(scapula_points, glenoid_points)

    assert not isinstance(plane, tuple)
    assert isinstance(plane, vtkPolyData)

    plane = plnf.fit_plane_transverse(scapula_points, glenoid_points,
            return_meta3 = True)

    assert isinstance(plane, tuple)
    assert isinstance(plane[0], vtkPolyData)
    assert np.allclose(plane[1], np.array([-45.0, -5.0, 0.0]))
    assert np.allclose(plane[2], np.array([0.0, 0.0, 90.0]))


def test_two_plane_version():
    """
    Tests for version measurement using two planes method.
    """

    plane_normal1 = (0.0, 1.0, 0.0)
    plane_normal2 = (-0.5, -0.5, 0.0)

    version = plnf.planes_version(plane_normal1, plane_normal2)

    assert version == 45.0
