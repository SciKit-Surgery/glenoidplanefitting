"""
Functions to create vtk models for visualisation of
results
"""
from vtk import vtkPlaneSource, vtkLineSource, vtkSphereSource #pylint:disable=no-name-in-module

def make_plane_model(plane_centre, normal_vector, resolution = 10,
        plane_size = 200.0):
    """
    Makes a vtk plane source, with centre and normal vector

    :param plane_centre: a point on the plane
    :param normal_vector: the plane normal vector

    :returns: The plane
    """
    plane = vtkPlaneSource()
    plane.SetOrigin(-plane_size/2.,-plane_size/2.,0)
    plane.SetPoint1(-plane_size/2.,plane_size/2.,0)
    plane.SetPoint2(plane_size/2.,-plane_size/2.,0)
    plane.SetCenter(plane_centre)
    plane.SetNormal(normal_vector)
    plane.SetXResolution(resolution)
    plane.SetYResolution(resolution)
    return plane

def make_friedman_model(point1, point2):

    """
    Makes a vtk line source from two set points

    :param point1: one end of the line
    :param point2: other end of the line

    :returns: The line
    """

    line = vtkLineSource()
    line.SetPoint1(point1)
    line.SetPoint2(point2)
    return line


def make_vault_model(point1,point2):

    """
    Makes a vtk line source from two set points

    :param point1: one end of the line
    :param point2: other end of the line

    :returns: The line
    """

    line = vtkLineSource()
    line.SetPoint1(point1)
    line.SetPoint2(point2)
    return line

def make_sphere_model(point, radius = 5.0):
    """
    Make a sphere source which we can use to represent a landmark
    point

    :param point: the point

    :returns the vtkPointSource
    """
    sphere_source = vtkSphereSource()
    sphere_source.SetCenter(point)
    sphere_source.SetThetaResolution(12)
    sphere_source.SetPhiResolution(12)
    sphere_source.SetRadius(radius)
    return sphere_source
