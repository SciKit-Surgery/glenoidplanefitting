# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting

def run_demo(model_file_name, output=""):
    """ Run the application """
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    points = [[-57.8, 190.2, -76.9],[-117.7, 112.4, -96.8],[-92.5, 219.2, -162.1]]
    return_meta = True
    result = plane_fitting.fit_plane_to_points(points,return_meta)
                                                     
                                                     
                                                     

    print("Result is {}".format(result))

    if output != "":

        plane = vtk.vtkPlaneSource()
        plane.SetCenter(result[1]) #result of center calc
        plane.SetNormal(result[2]) #result of normal vector
        plane.SetXResolution(600)
        plane.SetYResolution(600)
        
        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(plane.GetOutput())
        plane.Update()
        writer.Write()
