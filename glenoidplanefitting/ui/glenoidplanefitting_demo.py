# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
import numpy as np
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting
from glenoidplanefitting.widgets.visualisation import vis_widget
from glenoidplanefitting.algorithms.models import make_plane_model

def run_demo(model_file_name, points="", output="", visualise = False):


    if points != "":

        scapula = np.genfromtxt(points, delimiter=",")
        points1 = [scapula[0,1:4],scapula[1,1:4], scapula[2,1:4]]
        points2 = [scapula[3,1:4],scapula[4,1:4], scapula[5,1:4]]
        
    """ Run the application """
    
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    return_meta1 = True
    result = plane_fitting.fit_plane_to_points(points1,return_meta1)
    
    return_meta2 = True
    result2 = plane_fitting.fit_plane_to_points_glenoid(points2,return_meta2)
                                                                                                       
    print("Result is {}".format(result))
    print("Result2 is {}".format(result2))

    if output != "":
        
        plane = make_plane_model(result[1], result[2], resolution = 100)
        plane2 = make_plane_model(result2[1], result2[2], resolution = 100)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(plane.GetOutput())
        writer.SetInputData(plane2.GetOutput())
        plane.Update()
        plane2.Update()
        writer.Write()

        math = vtk.vtkMath
        radians = math.AngleBetweenVectors(result[2],result2[2])
        angle = math.DegreesFromRadians(radians)
        print("angle=", angle)
    
    if visualise:
        vis_widget(model, [result, result2])

        
