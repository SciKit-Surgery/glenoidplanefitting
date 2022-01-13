"""
Widgets for show the results of plane fitting.
"""
import vtk
from glenoidplanefitting.algorithms.models import make_plane_model, \
        make_friedman_model, make_vault_model, make_sphere_model

def renderer_common(bone, background_colour = [0.9, 0.9, 0.9]):
    """
    Initialises a vtk renderer and adds the bone model
    """

    renderer = vtk.vtkRenderer() #pylint:disable=no-member
    renderer.SetBackground(background_colour)

    bone.actor.GetProperty().SetAmbient(1)
    bone.actor.GetProperty().SetDiffuse(1)
    bone.actor.GetProperty().SetSpecular(1)
    renderer.AddActor(bone.actor)

    return renderer

def render_window_common(renderer, window_name):
    """
    Creates and starts a render window and interactor.

    :param renderer: A vtk renderer to add to the render window
    :param window_name: A name for the window
    """

    render_window = vtk.vtkRenderWindow() #pylint:disable=no-member
    render_window.SetWindowName(window_name)
    render_window.AddRenderer(renderer)

    render_window_interactor = vtk.vtkRenderWindowInteractor() #pylint:disable=no-member
    render_window_interactor.SetRenderWindow(render_window)
    render_window_interactor.Start()

    render_window.Finalize()
    del render_window_interactor, render_window

def add_vtk_source(renderer, source, linewidth = 1.0, opacity = 1.0, wireframe = False):
    """
    simplifies adding a vtk geometry source to a renderer

    :param renderer: a vtk renderer to add to
    :param source: a vtk geometry source
    """
    mapper = vtk.vtkPolyDataMapper() #pylint:disable=no-member
    mapper.SetInputConnection(source.GetOutputPort())
    actor = vtk.vtkActor() #pylint:disable=no-member
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(linewidth)
    actor.GetProperty().SetOpacity(opacity)
    if wireframe:
        actor.GetProperty().SetRepresentationToWireframe()
    else:
        actor.GetProperty().SetRepresentationToSurface()

    renderer.AddActor(actor)

def vis_planes(bone, planes, points = [], resolution = 1, plane_size = 200.0):
    """
    Visualisation for plane fitting methods

    :param bone: The model surface model
    :param planes: a list of planes, as returned by the
        plane fitting methods in algorithms.plane_fitting

    """
    renderer = renderer_common(bone)
    for plane in planes:
        plane_source = make_plane_model(plane[1], plane[2], resolution, plane_size)
        add_vtk_source(renderer, plane_source, opacity = 0.3)
        add_vtk_source(renderer, plane_source, linewidth = 2, opacity = 1.0, wireframe = True)

    for point in points:
        sphere_source = make_sphere_model(point)
        add_vtk_source(renderer, sphere_source)

    render_window_common(renderer, "Fitted Planes")

def vis_fried(bone, cross1, cross2, glenoid1, result, resolution = 1, plane_size = 200.0):
    """
    Visualise the lines resulting from the friedman
    method.

    :param cross1, cross2: The end points of the line crossing the glenoid
    :param glenoid1, result: The end points of the line defining the glenoid
        version
    """
    renderer = renderer_common(bone)

    glenoid_line = make_friedman_model(cross1,cross2)
    add_vtk_source(renderer, glenoid_line, linewidth = 10 )

    friedman_line = make_friedman_model(glenoid1,result)
    add_vtk_source(renderer, friedman_line)

    render_window_common(renderer, "Friedman Lines")


def vis_vault(bone, cross1, cross2, glenoid1, result, resolution = 1, plane_size = 200.0):
    """
    Visualise the lines resulting from the vault
    method.

    :param cross1, cross2: The end points of the line crossing the glenoid
    :param glenoid1, result: The end points of the line defining the glenoid
        version
    """
    renderer = renderer_common(bone)

    glenoid_line = make_vault_model(cross1,cross2)
    add_vtk_source(renderer, glenoid_line)

    vault_line = make_vault_model(glenoid1, result)
    add_vtk_source(renderer, vault_line)

    render_window_common(renderer, "Vault Lines")
