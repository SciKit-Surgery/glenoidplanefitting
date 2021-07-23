# coding=utf-8
""" Module for fitting a plane to a list of 3D points """
import numpy as np
import pyvista
import vtk


def fit_plane_to_points(points1, return_meta1=False):
    """Fit a plane to a set of points.

    Parameters
    ----------
    points : np.ndarray
        Size n by 3 array of points to fit a plane through

    return_meta : bool
        If true, also returns the center and normal used to generate the plane

    """

    data = np.array(points1)
    center = data.mean(axis=0)
    result = np.linalg.svd(data - center)
    normal = np.cross(result[2][0], result[2][1])
    plane = pyvista.Plane(center=center, direction=normal)
    if return_meta1:
        return plane, center, normal

    return plane


def fit_plane_to_points_glenoid(points2, return_meta2=False):
    
    data2 = np.array(points2)
    center2 = data2.mean(axis=0)
    result2 = np.linalg.svd(data2 - center2)
    normal2 = np.cross(result2[2][0], result2[2][1])
    plane2 = pyvista.Plane(center=center2, direction=normal2)
    if return_meta2:
        return plane2, center2, normal2

    return plane2




