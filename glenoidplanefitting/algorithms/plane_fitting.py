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


scapula = fit_plane_to_points([[-119.27, 106.61, -79.12],[-133.93, 129.15, -90.41],[-123.9, 119.51, -102.4]],True)
glenoid = fit_plane_to_points_glenoid([[-125.21, 122.57, -90.34],[-91.80, 226.94, -159.55],[-61.77, 193.93, -75.36]],True)

math = vtk.vtkMath
radians = math.AngleBetweenVectors(scapula[2],glenoid[2])
angle = math.DegreesFromRadians(radians)

print("angle=", angle)

print("scapula=", scapula)

print("glenoid=", glenoid)


