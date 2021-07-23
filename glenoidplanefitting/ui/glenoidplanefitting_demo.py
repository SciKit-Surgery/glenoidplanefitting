# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
import numpy as np
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting

def run_demo(model_file_name, points="", output=""):


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

        plane = vtk.vtkPlaneSource()
        plane.SetOrigin(-100,-100,0)
        plane.SetPoint1(-100,100,0)
        plane.SetPoint2(100,-100,0)
        plane.SetCenter(result[1]) #result of center calc
        plane.SetNormal(result[2]) #result of normal vector
        plane.SetXResolution(100)
        plane.SetYResolution(100)
        
        plane2 = vtk.vtkPlaneSource()
        plane2.SetOrigin(-100,-100,0)
        plane2.SetPoint1(-100,100,0)
        plane2.SetPoint2(100,-100,0)
        plane2.SetCenter(result2[1]) #result of center calc
        plane2.SetNormal(result2[2]) #result of normal vector
        plane2.SetXResolution(100)
        plane2.SetYResolution(100)


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


        
