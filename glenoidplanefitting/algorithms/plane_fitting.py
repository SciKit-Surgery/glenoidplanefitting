
"""

This is an implementation of a two plane method, see
A. Ganapathi, J. McCarron, Chen, J. Iannotti.
Predicting normal glenoid version from the pathologic scapula:
a comparison of 4 methods in 2- and 3-dimensional models
J Shoulder Elbow Surg (2011) 20, 234-244

"""

import numpy as np
import pyvista
import vtk


def fit_plane_to_points_scapula(points1, return_meta1=False):
    """
    Fit a plane to a set of manually selected points on the scapula

    :param points1: np.ndarray, size n by 3 array of the following points, inferior tip of scapula
    medial border of scapula, and center of glenoid fossa.
    :param return_meta: If true, also returns the center and normal used to generate the plane

    :return: the fitted plane through the scapula
    
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


    """
    Fit a plane to a set of manually selected points on the glenoid face

    :param points1: np.ndarray, size n by 3 array of the following points, one superior on the glenoid face,
    two inferior on the glenoid face left and right side
    :param return_meta: If true, also returns the center and normal used to generate the plane

    :return: the fitted plane of the glenoid face
    
    """
    
    data2 = np.array(points2)
    center2 = data2.mean(axis=0)
    result2 = np.linalg.svd(data2 - center2)
    normal2 = np.cross(result2[2][0], result2[2][1])
    plane2 = pyvista.Plane(center=center2, direction=normal2)
    if return_meta2:
        return plane2, center2, normal2

    return plane2




