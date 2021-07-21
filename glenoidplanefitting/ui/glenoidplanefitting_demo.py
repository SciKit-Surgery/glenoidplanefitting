# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting

def run_demo(model_file_name, output=""):
    """ Run the application """
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    points = [[-125.21, 122.57, -90.34],[-91.80, 226.94, -159.55],[-61.77, 193.93, -75.36]]
    return_meta = True
    result = plane_fitting.fit_plane_to_points(points,return_meta)
                                                     
                                                     
                                                     

    print("Result is {}".format(result))

    if output != "":

        plane = vtk.vtkPlaneSource()
        plane.SetOrigin(-100,-100,0)
        plane.SetPoint1(-100,100,0)
        plane.SetPoint2(100,-100,0)
        plane.SetCenter(result[1]) #result of center calc
        plane.SetNormal(result[2]) #result of normal vector
        plane.SetXResolution(100)
        plane.SetYResolution(100)
        
        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(plane.GetOutput())
        plane.Update()
        writer.Write()
