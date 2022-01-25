"""
Main entry point function for the various plane fitting functions
"""

from vtk import vtkXMLPolyDataWriter #pylint:disable=no-name-in-module
import numpy as np
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgerycore.configuration.configuration_manager import (
        ConfigurationManager
        )
from glenoidplanefitting.algorithms import plane_fitting, friedman, vault
from glenoidplanefitting.widgets.visualisation import vis_planes, vis_fried, \
        vis_vault
from glenoidplanefitting.algorithms.models import make_plane_model, \
        make_friedman_model, make_vault_model

#pylint: disable=too-many-locals
def run_demo(model_file_name, planes="", fried_points="", vault_points="",
             corr_fried="", output="", visualise = False, config_file = None):
    """
    :param planes: File name pointing to file containing points for
        planes method.
        First three points are for scapula plane in the order
        of medial border, inferior tip, glenoid center.
        For left shoulder latter three points are in order of superior
        glenoid, left inferior glenoid, right inferior glenoid.
        For right shoulder latter three points are in order of superior
        glenoid, right inferior glenoid, left inferior glenoid.

    :param fried_points: File name pointing to a file containing
        points for the Friedman method.
        If left shoulder, points in order of, right glenoid tip,
        left glenoid tip, scapula tip.
        If right shoulder, points in order of left glenoid tip,
        right glenoid tip, scapula tip.

    :param vault_points: File name pointing to a file containing
        points for the vault method.
        If left shoulder, points in order of, right glenoid tip,
        left glenoid tip, vault tip.
        If right shoulder, points in order of, left glenoid tip,
        right glenoid tip, vault tip.

    :param corr_fried: File name pointing to a file containing points
        for the corrected Friedman method.
        Input file: If left shoulder, points in order of, right glenoid tip,
        left glenoid tip, vault tip.
        If right shoulder, points in order of, left glenoid tip,
        right glenoid tip, vault tip.

    :param output: Output filename, can be planes.vtp, friedman.vtp,
        or vault.vtp
        Choosing planes.vtp Writes the transverse plane into a file
        used as the new axial
        slice for picking
        the new landmark points for the 3D corrected Friedman method.

    :param config_file: We can pass a configuration file, currently
        focusing on visualisation parameters
    """
    configuration = {}
    if config_file is not None:
        configurer = ConfigurationManager(config_file)
        configuration = configurer.get_copy()
    model_colour = configuration.get('model colour',
            [0.89, 0.86, 0.79]) #bone from https://www.colorhexa.com/e3dac9
    plane_resolution = configuration.get('plane resolution', 1)
    plane_size =  configuration.get('plane size' , 200.0)
    vary_plane_colour = configuration.get('vary plane colour', True)
    point_size =  configuration.get('point size', 3.0)
    line_width =  configuration.get('line width', 5)

    model = VTKSurfaceModel(model_file_name, model_colour)
    version = None
    if planes != "":

        points = np.genfromtxt(planes, delimiter=",")


        points1 = [points[0,1:4],points[1,1:4], points[2,1:4]]
        points2 = [points[3,1:4],points[4,1:4], points[5,1:4]]

        return_meta1 = True
        result = plane_fitting.fit_plane_to_points_scapula(points1,return_meta1)

        return_meta2 = True
        result2 = plane_fitting.fit_plane_to_points_glenoid(points2,
                                                            return_meta2)

        points3 = [points[0,1:4],points[2,1:4]]

        return_meta3 = True
        result3 = plane_fitting.fit_plane_transverse(points1, points3,
                                                     return_meta3)

        if visualise:
            vis_planes(model, [result, result2, result3], points1, points2,
                    plane_resolution, plane_size, vary_plane_colour,
                    point_size)


    if fried_points != "":

        axial = np.genfromtxt(fried_points, delimiter=",")

        anterior_glenoid = axial[0,1:4]
        posterior_glenoid = axial[1,1:4]
        glenoid_centre = axial[2,1:4]

        result = friedman.create_friedman_line(anterior_glenoid,
                posterior_glenoid)
        if visualise:
            vis_fried(model, anterior_glenoid, posterior_glenoid,
                    glenoid_centre, result, line_width = line_width)


    if vault_points !="":

        axial = np.genfromtxt(vault_points, delimiter=",")
        anterior_glenoid = axial[0,1:4]
        posterior_glenoid = axial[1,1:4]
        glenoid_centre = axial[2,1:4]

        result = vault.create_vault_line(anterior_glenoid,posterior_glenoid)
        if visualise:
            vis_vault(model, anterior_glenoid, posterior_glenoid,
                    glenoid_centre, result, line_width = line_width)

    if corr_fried !="":

        axial = np.genfromtxt(corr_fried, delimiter=",")
        anterior_glenoid = axial[0,1:4]
        posterior_glenoid = axial[1,1:4]
        glenoid_centre = axial[2,1:4]
        raise NotImplementedError("Corrected Friedman is not implemented")
        result = corrected_friedman.create_friedman_line(#pylint:disable=undefined-variable,unreachable
                anterior_glenoid,posterior_glenoid)
        if visualise:
            vis_fried(model,anterior_glenoid,posterior_glenoid,
                      glenoid_centre,result)

    if output == "planes.vtp":

        plane3 = make_plane_model(result3[1], result3[2], resolution = 100)

        writer = vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(plane3.GetOutput())
        plane3.Update()
        writer.Write()

        version = plane_fitting.planes_version(result[2], result2[2])
        print("version=", version)

    if output == "friedman.vtp":

        glenoid_line = make_friedman_model(anterior_glenoid,posterior_glenoid)
        friedman_line = make_friedman_model(glenoid_centre,result)

        writer = vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(glenoid_line.GetOutput())
        writer.SetInputData(friedman_line.GetOutput())
        glenoid_line.Update()
        friedman_line.Update()
        writer.Write()

        version = friedman.friedman_version(posterior_glenoid,result,
                                            glenoid_centre)
        print("version=",version)

    if output == "vault.vtp":

        glenoid_line = make_vault_model(anterior_glenoid,posterior_glenoid)
        vault_line = make_vault_model(glenoid_centre, result)

        writer = vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(glenoid_line.GetOutput())
        writer.SetInputData(vault_line.GetOutput())
        glenoid_line.Update()
        vault_line.Update()
        writer.Write()

        version = vault.vault_version(posterior_glenoid,result,glenoid_centre)
        print("version=",version)

    return version
