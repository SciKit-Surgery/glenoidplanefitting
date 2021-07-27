"""
Functions to create vtk models for visualisation of 
results
"""
import vtk

def make_plane_model(plane_centre, normal_vector, resolution = 10):
    plane = vtk.vtkPlaneSource()
    plane.SetOrigin(-100,-100,0)
    plane.SetPoint1(-100,100,0)
    plane.SetPoint2(100,-100,0)
    plane.SetCenter(plane_centre)
    plane.SetNormal(normal_vector)
    plane.SetXResolution(resolution)
    plane.SetYResolution(resolution)
    return plane
