# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
import numpy as np
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting, friedman, vault
from glenoidplanefitting.widgets.visualisation import vis_planes, vis_fried, vis_vault
from glenoidplanefitting.algorithms.models import make_plane_model, make_friedman_model, make_vault_model


def run_demo(model_file_name, planes="", fried_points="", vault_points="", output="", visualise = False):


    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    if planes != "":

        points = np.genfromtxt(planes, delimiter=",")
        """
        Input file: first three points are for scapula plane,
        latter three points are for glenoid plane
        """
        points1 = [points[0,1:4],points[1,1:4], points[2,1:4]]
        points2 = [points[3,1:4],points[4,1:4], points[5,1:4]]

        return_meta1 = True
        result = plane_fitting.fit_plane_to_points_scapula(points1,return_meta1)
        print("result=", result[1])
    
        return_meta2 = True
        result2 = plane_fitting.fit_plane_to_points_glenoid(points2,return_meta2)


        points3 = [points[0,1:4],points[2,1:4]]
        
        
        return_meta3 = True
        result3 = plane_fitting.fit_plane_transverse(points1, points3, return_meta3)

        if visualise:
            vis_planes(model, [result, result2, result3])


    if fried_points != "":
        
        axial = np.genfromtxt(fried_points, delimiter=",")
        p1 = axial[0,1:4]
        p2 = axial[1,1:4]
        p3 = axial[2,1:4]

        result = friedman.createFriedmanLine(p1,p2)
        if visualise:
            vis_fried(model, p1, p2, p3, result)


    if vault_points !="":
        
        axial = np.genfromtxt(vault_points, delimiter=",")
        p1 = axial[0,1:4]
        p2 = axial[1,1:4]
        p3 = axial[2,1:4]

        result = vault.createVaultLine(p1,p2)
        if visualise:
            vis_vault(model, p1, p2, p3, result)


                                                                                                   

    if output == "planes.vtp":
        
        plane = make_plane_model(result[1], result[2], resolution = 100)
        plane2 = make_plane_model(result2[1], result2[2], resolution = 100)
        plane3 = make_plane_model(result3[1], result3[2], resolution = 100)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(plane3.GetOutput())
        plane3.Update()
        writer.Write()

        math = vtk.vtkMath
        radians = math.AngleBetweenVectors(result[2],result2[2])
        version = (math.DegreesFromRadians(radians))-90
        print("version=", version)

        

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

        version = friedman.FriedmanVersion(p2,result,p3)
        print("version=",version)



    if output == "vault.vtp":

        glenoid_line = make_vault_model(p1,p2)
        vault_line = make_vault_model(p3, result)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(glenoid_line.GetOutput())
        writer.SetInputData(vault_line.GetOutput())
        glenoid_line.Update()
        vault_line.Update()
        writer.Write()

        version = vault.VaultVersion(p2,result,p3)
        print("version=",version)
        



    


        
