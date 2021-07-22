# coding=utf-8

"""Uses plane fitting to fit to vtk model"""
import vtk
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from glenoidplanefitting.algorithms import plane_fitting

def run_demo(model_file_name, output=""):
    
    """ Run the application """
    
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    points1 = [[-119.27, 106.61, -79.12],[-133.93, 129.15, -90.41],[-123.9, 119.51, -102.4]]
    return_meta1 = True
    result = plane_fitting.fit_plane_to_points(points1,return_meta1)

    points2 =[[-125.21, 122.57, -90.34],[-91.80, 226.94, -159.55],[-61.77, 193.93, -75.36]]
    return_meta2 = True
    result2 = plane_fitting.fit_plane_to_points_glenoid(points2,return_meta2)
                                                     
 #points_scap = [-125.21, 122.57, -90.34],[-91.80, 226.94, -159.55],[-61.77, 193.93, -75.36]                                                   

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
        plane.Update()
        writer.SetInputData(plane2.GetOutput())
        plane2.Update()
        writer.Write()




        
