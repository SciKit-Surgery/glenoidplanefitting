
"""

This is an implementation of a two plane method, see

A. Ganapathi, J. McCarron, Chen, J. Iannotti.
`Predicting normal glenoid version from the pathologic scapula:
a comparison of 4 methods in 2- and 3-dimensional models
<https://doi.org/10.1016/j.jse.2010.05.024>`_
J Shoulder Elbow Surg (2011) 20, 234-244

"""

import math
import numpy as np
import vtk
from glenoidplanefitting.algorithms.models import make_plane_model


def fit_plane_to_points_scapula(points1, return_meta1=False):
    """
    Fit a plane to a set of manually selected points on the scapula

    :param points1: np.ndarray, size n by 3 array of the following points,
        inferior tip of scapula, medial border of scapula, and center
        of glenoid fossa.
    :param return_meta: If true, also returns the center and normal
        used to generate the plane

    :return: the fitted plane through the scapula
    """

    data = np.array(points1)
    center = data.mean(axis=0)
    result = np.linalg.svd(data - center)
    normal = np.cross(result[2][0], result[2][1])
    planesource = make_plane_model(center, normal)
    if return_meta1:
        return planesource.GetOutput(), center, normal

    return planesource.GetOutput()


def fit_plane_to_points_glenoid(points2, return_meta2=False):


    """
    Fit a plane to a set of manually selected points on the glenoid face

    :param points1: np.ndarray, size n by 3 array of the following points,
        one superior on the glenoid face,
        two inferior on the glenoid face left and right side
    :param return_meta: If true, also returns the center and normal
        used to generate the plane

    :return: the fitted plane of the glenoid face
    """

    data2 = np.array(points2)
    center2 = data2.mean(axis=0)
    result2 = np.linalg.svd(data2 - center2)
    normal2 = np.cross(result2[2][0], result2[2][1])
    planesource2 = make_plane_model(center2, normal2)
    if return_meta2:
        return planesource2.GetOutput(), center2, normal2

    return planesource2.GetOutput()

def fit_plane_transverse(points1, points3, return_meta3=False):

    """
    Fit a transverse plane perpendicular to the scapular plane and
    passing through the scapular axis.

    :param points1: np.ndarray, size n by 3 array of the following points,
        inferior tip of scapula medial border of scapula,
        and center of glenoid fossa.
    :param points3: np.ndarray, size n by 3 of the following points,
        center of glenoid fossa, and medial border
    :param return_meta: If true, also returns the center and normal
        used to generate the plane

    :return: the fitted transverse plane
    """

    data = np.array(points1)
    center = data.mean(axis=0)
    result = np.linalg.svd(data - center)
    normal = np.cross(result[2][0], result[2][1])
    normal1 = np.array(normal)

    data3 = np.array(points3)
    x_mid = (data3[0,0] + data3[1,0])/2
    y_mid = (data3[0,1] + data3[1,1])/2
    z_mid = (data3[0,2] + data3[1,2])/2
    vector = np.array(data3[0] - data3[1])
    center3 = (x_mid, y_mid, z_mid)
    normal3 = np.cross(vector, normal1)
    planesource3 = make_plane_model(center3, normal3)
    if return_meta3:
        return planesource3.GetOutput(), center3, normal3

    return planesource3.GetOutput()


def planes_version(normal_plane1, normal_plane2):

    """
    Determines the glenoid version using the two planes method.

    :param normal_plane1: The normal vector of the scapula plane.
    :param normal_plane2: The normal vector of the glenoid plane.

    :returns: The glenoid version (positive value indicates retroversion)
    """

    radians = vtk.vtkMath().AngleBetweenVectors(#pylint:disable=no-member
            normal_plane1, normal_plane2)
    version = math.degrees(radians) - 90

    return version
