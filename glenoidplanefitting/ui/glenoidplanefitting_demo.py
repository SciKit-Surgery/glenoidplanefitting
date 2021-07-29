# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
import numpy as np
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting
from glenoidplanefitting.algorithms import friedman
from glenoidplanefitting.widgets.visualisation import vis_widget
from glenoidplanefitting.algorithms.models import make_plane_model
from glenoidplanefitting.algorithms.models import make_friedman_model

def run_demo(model_file_name, points="", output="", visualise = False):


    if points != "landmark_friedman.fcsv":

        all_points = np.genfromtxt(points, delimiter=",")
        points1 = [all_points[0,1:4],all_points[1,1:4], all_points[2,1:4]]
        points2 = [all_points[3,1:4],all_points[4,1:4], all_points[5,1:4]]


        """ Run the application """
    
        model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
        return_meta1 = True
        result = plane_fitting.fit_plane_to_points(points1,return_meta1)
    
        return_meta2 = True
        result2 = plane_fitting.fit_plane_to_points_glenoid(points2,return_meta2)


    if points == "landmark_friedman.fcsv":
        
        axial = np.genfromtxt(points, delimiter=",")
        p1 = axial[0,1:4]
        p2 = axial[1,1:4]
        p3 = axial[2,1:4]

        model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
        result = friedman.createFriedmanLine(p1,p2,p3)
                                                                                                   

    if output != "friedman.vtp":
        
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
        angle = (math.DegreesFromRadians(radians))-90
        print("angle=", angle)

    if output == "friedman.vtp":

        glenoid_line = make_friedman_model(p1,p2)
        friedman_line = make_friedman_model(p3,result)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(glenoid_line.GetOutput())
        writer.SetInputData(friedman_line.GetOutput())
        glenoid_line.Update()
        friedman_line.Update()
        writer.Write()

        angle = friedman.FriedmanAngle(p2,result,p3)
        print("angle=",angle-90)
    
    if visualise:
        vis_widget(model, [result, result2])


        
