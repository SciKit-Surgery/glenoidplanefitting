"""
Functions to create vtk models for visualisation of
results
"""
import vtk

def make_plane_model(plane_centre, normal_vector, resolution = 10):
    """
    Makes a vtk plane source, with centre and normal vector
    :param plane_centre: a point on the plane
    :param normal_vector: the plane normal vector

    :returns: The plane
    """
    plane = vtk.vtkPlaneSource()
    plane.SetOrigin(-100,-100,0)
    plane.SetPoint1(-100,100,0)
    plane.SetPoint2(100,-100,0)
    plane.SetCenter(plane_centre)
    plane.SetNormal(normal_vector)
    plane.SetXResolution(resolution)
    plane.SetYResolution(resolution)
    return plane

def make_friedman_model(point1, point2):

    """
    Makese a vtk line source from two set points
    :param point1: one end of the line
    :param point2: other end of the line

    :returns: The line
    """

    line = vtk.vtkLineSource()
    line.SetPoint1(point1)
    line.SetPoint2(point2)
    return line


def make_vault_model(point1,point2):

    """
    Makese a vtk line source from two set points
    :param point1: one end of the line
    :param point2: other end of the line

    :returns: The line
    """

    line = vtk.vtkLineSource()
    line.SetPoint1(point1)
    line.SetPoint2(point2)
    return line
    
